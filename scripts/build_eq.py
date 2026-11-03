"""Build Wavelet GraphicEQ files, PEQ tables and plots for the Kiwi Ears Cadenza 2.

Inputs (all IEC 60318-4 / "711" rig, see README):
  data/cadenza2_711_consensus.csv   median of 27 squig.link 711 measurements
  data/targets/*.csv                711 targets (AutoEq CSV: frequency,raw)

Requires AutoEq 4.1.2 (Python 3.8-3.11):  pip install autoeq==4.1.2
Run from the repo root:                   python scripts/build_eq.py
"""
import csv
import json
import math
import os

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator, FuncFormatter, NullLocator
import numpy as np
from autoeq.frequency_response import FrequencyResponse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FS = 48000                 # Android / USB DAC output rate
MAX_GAIN = 6.0             # AutoEq default positive-gain ceiling
TREBLE_F_LOWER = 5000.0    # treble region where EQ strength is reduced ...
TREBLE_F_UPPER = 10000.0
TREBLE_GAIN_K = 0.5        # ... to 50 % at 10 kHz and above (log-sigmoid from 5 kHz) -> gentle treble
TREBLE_FROM = 5000.0       # "treble" for the limits below
TREBLE_MAX_BOOST = 3.0     # treble boosts capped at +3 dB
TREBLE_MAX_CUT = -4.0      # treble cuts capped at -4 dB
NO_BOOST_FROM = 10000.0    # no positive gain at or above this frequency
BOOST_TAPER_START = 8500.0 # positive gain fades to 0 dB between 8.5 and 10 kHz
HEADROOM = 0.5             # extra safety margin on top of the largest boost (dB)

TARGETS = [
    dict(name='IEF Preference 2025', csv='IEF Preference 2025 (711).csv',
         label='IEF Preference 2025 (711)', source='Crinacle, 711 version as hosted on squig.link'),
    dict(name='Harman IE 2019v2', csv='Harman IE 2019v2.csv',
         label='Harman IE 2019v2', source='Harman / Olive et al., 711 version as hosted on squig.link'),
    dict(name='Thieaudio Monarch MK3', csv='IEM Thieaudio Monarch MK3.csv',
         label='Thieaudio Monarch MK3 (711, rig-matched)',
         source='median of same-site (Monarch MK3 - Cadenza 2) deltas from 8 squig.link 711 databases'),
]

PEQ_CONFIG = {
    'optimizer': {'min_std': 0.008},
    'filters': [
        {'type': 'LOW_SHELF', 'fc': 105.0, 'q': 0.7},
        {'type': 'HIGH_SHELF', 'fc': 10000.0, 'q': 0.7, 'max_gain': 0.0},  # cut-only treble shelf
    ] + [{'type': 'PEAKING', 'max_q': 3.0, 'max_fc': 5000.0} for _ in range(4)]   # bass / mids / presence
      + [{'type': 'PEAKING', 'min_fc': 4000.0, 'max_fc': 9000.0, 'max_q': 1.5,    # broad, bounded treble filters
          'min_gain': TREBLE_MAX_CUT, 'max_gain': TREBLE_MAX_BOOST} for _ in range(2)],
}

# Reference palette (dataviz skill, light mode)
INK, INK2, MUTED, GRID, SURFACE = '#0b0b0b', '#52514e', '#8a8984', '#e4e3df', '#fcfcfb'
BLUE, ORANGE, AQUA = '#2a78d6', '#eb6834', '#1baf7a'


def read_fr(path, name):
    fr = FrequencyResponse.read_csv(path)
    fr.name = name
    return fr


def limit_treble_boost(f, eq):
    """Gentle treble: +3/-4 dB limits from 5 kHz, and no boost >= 10 kHz (positive gain fades out from 8.5 kHz)."""
    tr = f >= TREBLE_FROM
    eq = eq.copy()
    eq[tr] = np.clip(eq[tr], TREBLE_MAX_CUT, TREBLE_MAX_BOOST)
    taper = np.clip((np.log(NO_BOOST_FROM) - np.log(f)) / (np.log(NO_BOOST_FROM) - np.log(BOOST_TAPER_START)), 0, 1)
    pos = np.clip(eq, 0, None)
    eq = eq - pos + pos * taper
    tmp = FrequencyResponse(name='tmp', frequency=f, raw=eq)
    tmp.smoothen(window_size=1 / 6, treble_window_size=1 / 6)
    eq = tmp.smoothed
    hi = f >= NO_BOOST_FROM
    eq[hi] = np.minimum(eq[hi], 0.0)
    eq[tr] = np.clip(eq[tr], TREBLE_MAX_CUT, TREBLE_MAX_BOOST)
    return eq


def remove_treble_leak(peqs, f):
    """Peaking-filter skirts can leak a few tenths of a dB above 10 kHz; deepen the cut-only shelf to cancel it."""
    shelf = [flt for p in peqs for flt in p.filters if flt.__class__.__name__ == 'HighShelf'][0]
    for _ in range(50):
        leak = float(np.max(peq_response(peqs, f)[f >= NO_BOOST_FROM]))
        if leak <= 0.0:
            break
        shelf.gain = shelf.gain - (leak + 0.05)


def preamp_for(curve):
    return -math.ceil((max(float(np.max(curve)), 0.0) + HEADROOM) * 10) / 10


def peq_response(peqs, f):
    total = np.zeros(len(peqs[0].f))
    for p in peqs:
        total += p.fr
    return np.interp(np.log(f), np.log(peqs[0].f), total)


def log_axis(ax):
    ax.set_xscale('log')
    ax.set_xlim(20, 20000)
    ticks = [20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]
    ax.xaxis.set_major_locator(FixedLocator(ticks))
    ax.xaxis.set_minor_locator(NullLocator())
    ax.xaxis.set_major_formatter(FuncFormatter(lambda v, _: f'{v / 1000:g}k' if v >= 1000 else f'{v:g}'))
    ax.grid(True, color=GRID, lw=0.8)
    for s in ('top', 'right'):
        ax.spines[s].set_visible(False)
    for s in ('left', 'bottom'):
        ax.spines[s].set_color(MUTED)
    ax.tick_params(colors=INK2, labelsize=9)
    ax.axvspan(NO_BOOST_FROM, 20000, color='#f0efec', zorder=0)


def plot_target(t, fr, eq, gfx_points, peq_curve, preamp, peq_preamp, peqs, out):
    f = fr.frequency
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 7.6), sharex=True, gridspec_kw={'height_ratios': [3, 2]},
                                   facecolor=SURFACE)
    for ax in (ax1, ax2):
        ax.set_facecolor(SURFACE)
        log_axis(ax)
    eqd = fr.raw + eq
    ax1.plot(f, fr.target, color=INK2, lw=2, ls=(0, (5, 3)), label=f'Target: {t["label"]}', zorder=3)
    ax1.plot(f, fr.raw, color=BLUE, lw=2, label='Cadenza 2 raw (711 consensus, 27 sites)', zorder=4)
    ax1.plot(f, eqd, color=ORANGE, lw=2, label="Cadenza 2 EQ'd (GraphicEQ file)", zorder=5)
    lo = min(np.min(fr.raw[f < 16000]), np.min(fr.target[f < 16000]), np.min(eqd[f < 16000]))
    hi = max(np.max(fr.raw), np.max(fr.target), np.max(eqd))
    ax1.set_ylim(math.floor((lo - 2) / 5) * 5, math.ceil((hi + 2) / 5) * 5)
    ax1.set_ylabel('Level (dB, normalized)', color=INK2, fontsize=10)
    ax1.text(NO_BOOST_FROM * 1.05, ax1.get_ylim()[1] - 1, 'no boosts\n≥10 kHz', va='top', ha='left', fontsize=8,
             color=INK2)
    ax1.legend(loc='lower left', frameon=False, fontsize=9, labelcolor=INK)
    m = (f >= 20) & (f <= 10000)
    before = np.sqrt(np.mean((fr.raw - fr.target)[m] ** 2))
    after = np.sqrt(np.mean((eqd - fr.target)[m] ** 2))
    ax1.set_title(f'Kiwi Ears Cadenza 2 → {t["label"]}', loc='left', fontsize=13, color=INK, fontweight='bold',
                  pad=24)
    ax1.text(0.0, 1.015, f'Error vs target, 20 Hz–10 kHz: {before:.2f} dB RMS raw → {after:.2f} dB RMS with EQ'
             f'  ·  curves shown without preamp so they overlay the target', transform=ax1.transAxes, fontsize=9,
             color=INK2, va='bottom')

    ax2.axhline(0, color=MUTED, lw=1)
    ax2.plot(f, eq + preamp, color=ORANGE, lw=2, label=f'GraphicEQ file (preamp {preamp:+.1f} dB built in)')
    ax2.plot(gfx_points[0], gfx_points[1], 'o', ms=2.2, color=ORANGE, alpha=0.6)
    ax2.plot(f, peq_curve + peq_preamp, color=BLUE, lw=2, ls=(0, (5, 3)),
             label=f'PEQ table, {len([p for p in peqs if abs(p.gain) >= 0.05])} filters (preamp {peq_preamp:+.1f} dB)')
    ax2.set_ylabel('EQ gain (dB)', color=INK2, fontsize=10)
    ax2.set_xlabel('Frequency (Hz)', color=INK2, fontsize=10)
    lo2 = min(np.min(eq + preamp), np.min(peq_curve + peq_preamp))
    ax2.set_ylim(math.floor(lo2 - 1), 1.5)
    ax2.legend(loc='lower left', frameon=False, fontsize=9, labelcolor=INK)
    fig.tight_layout()
    fig.savefig(out, dpi=200, facecolor=SURFACE)
    plt.close(fig)


def main():
    for d in ('wavelet', 'peq', 'plots'):
        os.makedirs(os.path.join(ROOT, d), exist_ok=True)
    summary = []
    for t in TARGETS:
        fr = read_fr(os.path.join(ROOT, 'data', 'cadenza2_711_consensus.csv'), 'Kiwi Ears Cadenza 2')
        target = read_fr(os.path.join(ROOT, 'data', 'targets', t['csv']), t['label'])
        fr.process(target=target, min_mean_error=True, max_gain=MAX_GAIN, treble_f_lower=TREBLE_F_LOWER,
                   treble_f_upper=TREBLE_F_UPPER, treble_gain_k=TREBLE_GAIN_K)
        f = fr.frequency
        eq = limit_treble_boost(f, fr.equalization)
        fr.equalization = eq
        fr.equalized_raw = fr.raw + eq
        preamp = preamp_for(eq)

        # Wavelet / AutoEq GraphicEQ (127 bands, preamp baked into every band)
        gfx = fr.eqapo_graphic_eq(normalize=False, preamp=preamp)
        with open(os.path.join(ROOT, 'wavelet', f'{t["name"]}.txt'), 'w', encoding='utf-8') as fh:
            fh.write(gfx + '\n')
        pts = [p.split(' ') for p in gfx.replace('GraphicEQ: ', '').split('; ')]
        gfx_f = np.array([float(a) for a, _ in pts])
        gfx_g = np.array([float(b) for _, b in pts])
        assert len(pts) == 127 and gfx_g.max() <= -HEADROOM + 0.05, (len(pts), gfx_g.max())
        assert gfx_g[gfx_f >= NO_BOOST_FROM].max() <= preamp + 0.05  # nothing above 10 kHz is boosted

        # Parametric EQ approximation of the same curve
        peqs = fr.optimize_parametric_eq(json.loads(json.dumps(PEQ_CONFIG)), FS)
        remove_treble_leak(peqs, f)
        filters = [flt for p in peqs for flt in p.filters]
        peq_curve = peq_response(peqs, f)
        peq_preamp = preamp_for(peq_curve)
        m = (f >= 20) & (f <= 10000)
        fit_rms = float(np.sqrt(np.mean((peq_curve - eq)[m] ** 2)))
        peq_max_above_10k = float(np.max(peq_curve[f >= NO_BOOST_FROM]))
        kinds = {'Peaking': 'PK', 'LowShelf': 'LSC', 'HighShelf': 'HSC'}
        rows = [dict(type=kinds[flt.__class__.__name__], fc=round(float(flt.fc)), gain=round(float(flt.gain), 1),
                     q=round(float(flt.q), 2)) for flt in filters if abs(flt.gain) >= 0.05]
        rows.sort(key=lambda r: r['fc'])
        with open(os.path.join(ROOT, 'peq', f'{t["name"]}.csv'), 'w', newline='') as fh:
            wr = csv.writer(fh)
            wr.writerow(['filter', 'type', 'frequency_hz', 'gain_db', 'q'])
            wr.writerow(['preamp', '', '', f'{peq_preamp:.1f}', ''])
            for i, r in enumerate(rows, 1):
                wr.writerow([i, r['type'], r['fc'], f'{r["gain"]:.1f}', f'{r["q"]:.2f}'])
        with open(os.path.join(ROOT, 'peq', f'{t["name"]} ParametricEQ.txt'), 'w', encoding='utf-8') as fh:
            fh.write(f'Preamp: {peq_preamp:.1f} dB\n')
            for i, r in enumerate(rows, 1):
                fh.write(f'Filter {i}: ON {r["type"]} Fc {r["fc"]} Hz Gain {r["gain"]:.1f} dB Q {r["q"]:.2f}\n')

        plot_target(t, fr, eq, (gfx_f, gfx_g), peq_curve, preamp, peq_preamp, filters,
                    os.path.join(ROOT, 'plots', f'{t["name"]}.png'))
        eqd = fr.raw + eq
        summary.append(dict(
            name=t['name'], label=t['label'], source=t['source'], preamp=preamp, peq_preamp=peq_preamp,
            max_boost=float(eq.max()), max_cut=float(eq.min()),
            max_boost_above_10k=float(eq[f >= NO_BOOST_FROM].max()),
            peq_max_above_10k=peq_max_above_10k, peq_fit_rms=fit_rms, peq=rows,
            err_before=float(np.sqrt(np.mean((fr.raw - fr.target)[m] ** 2))),
            err_after=float(np.sqrt(np.mean((eqd - fr.target)[m] ** 2))),
            eq_at={str(k): round(float(np.interp(np.log(k), np.log(f), eq)), 1)
                   for k in (20, 50, 100, 200, 300, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000,
                             10000, 12000, 15000)}))
        print(f'{t["name"]:24s} preamp {preamp:+.1f} dB | EQ +{eq.max():.1f}/{eq.min():.1f} dB | '
              f'boost>=10k {eq[f >= NO_BOOST_FROM].max():+.2f} | error {summary[-1]["err_before"]:.2f}->'
              f'{summary[-1]["err_after"]:.2f} dB | PEQ fit {fit_rms:.2f} dB, PEQ max>=10k {peq_max_above_10k:+.2f}')
    with open(os.path.join(ROOT, 'peq', 'summary.json'), 'w') as fh:
        json.dump(summary, fh, indent=1)


if __name__ == '__main__':
    main()

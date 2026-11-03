"""Overview charts: the 711 measurement consensus and the target 'EQ effort' ranking."""
import csv
import os

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

from build_eq import BLUE, GRID, INK, INK2, MUTED, ORANGE, AQUA, ROOT, SURFACE, log_axis

# first set (blue) and the non-Harman second set (orange)
CHOSEN = {'IEF Preference 2025 (711)': BLUE, 'Harman IE 2019v2': BLUE, 'IEM: Thieaudio Monarch MK3': BLUE,
          'Δ JM-1 −10dB tilt (711)': ORANGE, 'HBB Bad Guy 2022': ORANGE, 'IEM: Truthear Hexa': ORANGE}


def consensus_plot():
    rows = list(csv.reader(open(os.path.join(ROOT, 'data', 'cadenza2_711_all_measurements.csv'))))
    head, data = rows[0], np.array(rows[1:], dtype=float)
    f = data[:, 0]
    used = {(r['site'], r['file']) for r in csv.DictReader(open(os.path.join(ROOT, 'data', 'sources.csv')))
            if r['used_in_consensus'] == 'yes'}
    cons = np.array([list(map(float, r)) for r in list(csv.reader(open(os.path.join(ROOT, 'data', 'cadenza2_711_consensus.csv'))))[1:]])
    fig, ax = plt.subplots(figsize=(10, 5.2), facecolor=SURFACE)
    ax.set_facecolor(SURFACE)
    log_axis(ax)
    n = 0
    for j, h in enumerate(head[1:], 1):
        site, file = h.split(' | ', 1)
        if (site, file) in used:
            ax.plot(f, data[:, j], color=MUTED, lw=0.8, alpha=0.55, zorder=2)
            n += 1
    ax.plot(cons[:, 0], cons[:, 1], color=BLUE, lw=2.2, zorder=3)
    ax.plot([], [], color=MUTED, lw=1, label=f'Individual measurements ({n} squig.link 711 databases, stock tips)')
    ax.plot([], [], color=BLUE, lw=2.2, label='Median used for EQ')
    ax.set_ylim(-20, 15)
    ax.set_xlabel('Frequency (Hz)', color=INK2)
    ax.set_ylabel('Level (dB, 300 Hz–3 kHz mean = 0)', color=INK2)
    ax.set_title('Kiwi Ears Cadenza 2 on IEC 60318-4 (711) couplers', loc='left', fontsize=13, color=INK,
                 fontweight='bold', pad=22)
    ax.text(0, 1.015, 'Shaded: ≥10 kHz, where 711 couplers stop agreeing (insertion depth / coupler resonance)',
            transform=ax.transAxes, fontsize=9, color=INK2, va='bottom')
    ax.legend(loc='lower left', frameon=False, fontsize=9, labelcolor=INK)
    fig.tight_layout()
    fig.savefig(os.path.join(ROOT, 'plots', '00 Cadenza 2 711 measurements.png'), dpi=200, facecolor=SURFACE)
    plt.close(fig)


def ranking_plot():
    rows = list(csv.DictReader(open(os.path.join(ROOT, 'data', 'target_ranking.csv'))))
    skip = {'Diffuse Field (711)', 'Etymotic', 'IEM: Kiwi Ears Cadenza (original)'}  # references / same family
    rows = [r for r in rows if r['target'] not in skip]
    rows.sort(key=lambda r: float(r['rms_eq_needed_db_20-10k']))
    names = [r['target'].replace('IEM: ', '') + ('  (IEM)' if r['target'].startswith('IEM: ') else '') for r in rows]
    vals = [float(r['rms_eq_needed_db_20-10k']) for r in rows]
    air = [float(r['air_boost_wanted_above_10k_db']) for r in rows]
    cols = [CHOSEN.get(r['target'], '#c9c8c2') for r in rows]
    fig, ax = plt.subplots(figsize=(10, 10.5), facecolor=SURFACE)
    ax.set_facecolor(SURFACE)
    y = np.arange(len(rows))[::-1]
    ax.barh(y, vals, height=0.68, color=cols, edgecolor=SURFACE, linewidth=2, zorder=3)
    for yi, v, a, r in zip(y, vals, air, rows):
        ax.text(v + 0.04, yi, f'{v:.2f}' + (f'   wants +{a:.1f} dB air >10 kHz' if a >= 1.5 else ''),
                va='center', fontsize=8, color=INK2)
    ax.set_yticks(y)
    ax.set_yticklabels(names, fontsize=8.5, color=INK)
    for lbl, r in zip(ax.get_yticklabels(), rows):
        if r['target'] in CHOSEN:
            lbl.set_fontweight('bold')
    ax.set_xlim(0, max(vals) * 1.45)
    ax.set_ylim(-0.7, len(rows) - 0.3)
    ax.grid(True, axis='x', color=GRID, lw=0.8, zorder=0)
    for s in ('top', 'right', 'left'):
        ax.spines[s].set_visible(False)
    ax.spines['bottom'].set_color(MUTED)
    ax.tick_params(axis='x', colors=INK2, labelsize=9)
    ax.tick_params(axis='y', length=0)
    ax.set_xlabel('EQ needed to reach target: RMS of (target − Cadenza 2), 20 Hz–10 kHz, 1/6-oct, mean-aligned (dB)',
                  color=INK2, fontsize=9)
    ax.set_title('How far each 711 target is from a stock Cadenza 2', loc='left', fontsize=13, color=INK,
                 fontweight='bold', pad=22)
    ax.text(0, 1.008, 'Shorter = less EQ. Blue = first set of picks, orange = non-Harman set. "(IEM)" = another IEM\'s '
            'tuning, built from same-site measurements.', transform=ax.transAxes, fontsize=9, color=INK2, va='bottom')
    fig.tight_layout()
    fig.savefig(os.path.join(ROOT, 'plots', '01 Target EQ-effort ranking.png'), dpi=200, facecolor=SURFACE)
    plt.close(fig)


if __name__ == '__main__':
    consensus_plot()
    ranking_plot()

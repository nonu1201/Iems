"""Package the Wavelet presets into a genre-organised zip: dist/Cadenza 2 Wavelet EQ.zip

Run from the repo root after build_eq.py:  python scripts/make_zip.py
"""
import os
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOP = 'Cadenza 2 Wavelet EQ'

# preset key -> file stem in wavelet/, peq/ and plots/
PRESETS = {
    'HBB': 'HBB Bad Guy 2022',
    'IEF': 'IEF Preference 2025',
    'JM1': 'Delta JM-1 -10dB Tilt',
    'HEXA': 'Truthear Hexa',
    'MK3': 'Thieaudio Monarch MK3',
    'HARMAN': 'Harman IE 2019v2',
}

# (folder name, short label used in file names, ranking best -> worst)
GENRES = [
    ('Pop', 'Pop', ['HBB', 'IEF', 'HEXA', 'HARMAN', 'MK3', 'JM1']),
    ('Hip-hop, Rap, Trap', 'Hip-hop', ['HBB', 'HEXA', 'IEF', 'HARMAN', 'MK3', 'JM1']),
    ('EDM, House, Dubstep, DnB', 'EDM', ['HEXA', 'HBB', 'HARMAN', 'MK3', 'IEF', 'JM1']),
    ('R&B, Soul', 'R&B', ['IEF', 'HBB', 'JM1', 'HEXA', 'HARMAN', 'MK3']),
    ('Rock, Indie, Alternative', 'Rock', ['HBB', 'HEXA', 'MK3', 'IEF', 'HARMAN', 'JM1']),
    ('Metal', 'Metal', ['HEXA', 'HBB', 'MK3', 'IEF', 'JM1', 'HARMAN']),
    ('Jazz', 'Jazz', ['JM1', 'IEF', 'HEXA', 'MK3', 'HARMAN', 'HBB']),
    ('Classical, Orchestral, Film scores', 'Classical', ['JM1', 'IEF', 'HEXA', 'MK3', 'HARMAN', 'HBB']),
    ('Acoustic, Folk, Singer-songwriter', 'Acoustic', ['JM1', 'IEF', 'HEXA', 'HARMAN', 'MK3', 'HBB']),
    ('Vocal, Ballads, OST', 'Vocal', ['IEF', 'JM1', 'HARMAN', 'HEXA', 'HBB', 'MK3']),
    ('K-pop, J-pop, Anime', 'K-pop J-pop', ['IEF', 'HBB', 'HEXA', 'JM1', 'MK3', 'HARMAN']),
    ('Country, Blues, Americana', 'Country', ['IEF', 'HBB', 'JM1', 'HEXA', 'HARMAN', 'MK3']),
    ('Reggae, Dub, Reggaeton, Latin', 'Reggae Latin', ['HBB', 'HEXA', 'IEF', 'HARMAN', 'MK3', 'JM1']),
    ('Lo-fi, Chill, Ambient', 'Lo-fi', ['IEF', 'HBB', 'JM1', 'HEXA', 'MK3', 'HARMAN']),
    ('Mixed playlist (shuffle)', 'Shuffle', ['HBB', 'IEF']),
]

# flat copies, named by what each preset is for
FLAT_NAMES = {
    'HBB': 'HBB Bad Guy 2022 - best for Pop, Hip-hop, Rock, Reggae-Latin, Shuffle',
    'IEF': 'IEF Preference 2025 - best for R&B, Vocal, K-pop J-pop, Country, Lo-fi',
    'JM1': 'Delta JM-1 -10dB Tilt - best for Jazz, Classical, Acoustic',
    'HEXA': 'Truthear Hexa - best for EDM, Metal',
    'HARMAN': 'Harman IE 2019v2 - try for EDM, Vocal',
    'MK3': 'Thieaudio Monarch MK3 - try for Rock, Metal',
}

DESCRIPTIONS = {
    'HBB': 'punchy mid-bass, relaxed upper mids (-1 to -2 dB at 1-5 kHz), a little sparkle. Fun but never shouty.',
    'IEF': 'stock bass, vocals a bit forward (+1.6 dB at 3 kHz), less sibilance (-2 dB at 5-6 kHz). The smoothest.',
    'JM1': 'about 3 dB less sub-bass, fuller lower mids (+1 dB at 200-500 Hz). The most natural.',
    'HEXA': 'deep sub-bass kept, less glare at 2 and 5 kHz, crisp 7-8 kHz. Clean and tidy.',
    'MK3': 'stock bass, slightly scooped mids, extra 5-8 kHz sparkle. Leans slightly toward Harman treble.',
    'HARMAN': 'stock sub-bass, leaner lower mids, most 3-7 kHz energy (+1.4 to +3 dB). The brightest.',
}

ORD = ['1st', '2nd', '3rd', '4th', '5th', '6th']


def guide_text():
    w = 34
    lines = [
        'KIWI EARS CADENZA 2 - WAVELET EQ PRESETS',
        '=' * 44, '',
        'HOW TO USE',
        '- Pick the folder for what you are listening to in "By genre".',
        '  File "1" is my first choice for that genre, "6" my last.',
        '- In Wavelet, open AutoEq and use its import option to load the .txt.',
        '- The preamp is already built into every file (loudest band is -0.5 dB',
        '  or lower), so it cannot clip. Do not add extra gain.',
        '- Turn off Dolby Atmos / Adapt Sound / other EQs while comparing.',
        '- Players that use exclusive or "bit-perfect" USB output bypass Wavelet;',
        '  use normal Android output.',
        '- "All presets" has the same six files once each, named by what they are for.',
        '- "PEQ (other apps)" has the same EQs as parametric filters for apps that',
        '  import EqualizerAPO-style PEQ. "Plots" shows raw vs EQd vs target.',
        '',
        'THE SIX PRESETS',
    ]
    for k in ['HBB', 'IEF', 'JM1', 'HEXA', 'MK3', 'HARMAN']:
        lines.append(f'- {PRESETS[k]}: {DESCRIPTIONS[k]}')
    lines += ['', 'GENRE RANKING (best -> worst)', '']
    short = {'HBB': 'HBB', 'IEF': 'IEF', 'JM1': 'JM-1', 'HEXA': 'Hexa', 'MK3': 'MK3', 'HARMAN': 'Harman'}
    for folder, _, rank in GENRES:
        lines.append(f'{folder:<{w}} ' + ' > '.join(short[k] for k in rank))
    lines += [
        '', 'TIPS',
        '- One preset for everything: HBB Bad Guy 2022 (or IEF Preference 2025 if',
        '  you mostly play vocal or acoustic music).',
        '- Listening loud? Move one step toward HBB or IEF.',
        '- A harsh-sounding album? Try IEF whatever the genre.',
        '- Wide-bore stock tips sound about 1-2 dB darker in the treble than narrow.',
        '- Rankings are reasoned from what each EQ changes, not a listening test.',
        '  Trust your ears.',
        '',
        'All EQs: AutoEq 4.1.2 on the median of 27 squig.link IEC 711 measurements;',
        'treble changes capped at +3/-4 dB from 5 kHz, no boosts at or above 10 kHz.',
        'Full write-up: README.md in the repo.',
    ]
    return '\n'.join(lines) + '\n'


def main():
    out_dir = os.path.join(ROOT, 'dist')
    os.makedirs(out_dir, exist_ok=True)
    out = os.path.join(out_dir, f'{TOP}.zip')
    n = 0
    with zipfile.ZipFile(out, 'w', compression=zipfile.ZIP_DEFLATED) as z:
        z.writestr(f'{TOP}/README - which EQ for which genre.txt', guide_text())
        for folder, label, rank in GENRES:
            for i, k in enumerate(rank, 1):
                src = os.path.join(ROOT, 'wavelet', f'{PRESETS[k]}.txt')
                z.write(src, f'{TOP}/By genre/{folder}/{label} {i} - {PRESETS[k]}.txt')
                n += 1
        for k, name in FLAT_NAMES.items():
            z.write(os.path.join(ROOT, 'wavelet', f'{PRESETS[k]}.txt'), f'{TOP}/All presets/{name}.txt')
            z.write(os.path.join(ROOT, 'peq', f'{PRESETS[k]} ParametricEQ.txt'),
                    f'{TOP}/PEQ (other apps)/{PRESETS[k]} PEQ.txt')
            z.write(os.path.join(ROOT, 'plots', f'{PRESETS[k]}.png'), f'{TOP}/Plots/{PRESETS[k]}.png')
            n += 3
    print(f'wrote {out} ({n + 1} files, {os.path.getsize(out) / 1024:.0f} KB)')


if __name__ == '__main__':
    main()

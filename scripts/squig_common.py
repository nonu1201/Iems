import re, numpy as np
F = 20 * 1.01 ** np.arange(int(np.ceil(np.log(20000/20)/np.log(1.01))) + 1)
F = F[F <= 20000]

def parse_squig(path):
    fs, ss = [], []
    with open(path, 'rb') as fh:
        txt = fh.read().decode('utf-8', 'replace')
    for line in txt.splitlines():
        parts = [p for p in re.split(r'[,\t; ]+', line.strip()) if p]
        if len(parts) < 2: continue
        try:
            f = float(parts[0]); s = float(parts[1])
        except ValueError:
            continue
        if f <= 0 or not np.isfinite(s): continue
        fs.append(f); ss.append(s)
    fs, ss = np.array(fs), np.array(ss)
    o = np.argsort(fs); fs, ss = fs[o], ss[o]
    fs, idx = np.unique(fs, return_index=True); ss = ss[idx]
    return fs, ss

def to_grid(f, s, grid=F):
    y = np.interp(np.log(grid), np.log(f), s, left=np.nan, right=np.nan)
    # extend flat at edges if data slightly short
    first = np.where(~np.isnan(y))[0]
    if len(first):
        y[:first[0]] = y[first[0]]; y[first[-1]+1:] = y[first[-1]]
    return y

def norm_at(y, f0=500, grid=F, band=None):
    if band is None:
        return y - np.interp(np.log(f0), np.log(grid), y)
    m = (grid >= band[0]) & (grid <= band[1])
    return y - np.mean(y[m])

def smooth_oct(y, frac=1/12, grid=F):
    # simple fractional-octave moving average on log grid (1.01 step)
    step = np.log2(1.01)
    w = max(1, int(round(frac / step)))
    k = np.ones(2*w+1) / (2*w+1)
    yp = np.pad(y, w, mode='edge')
    return np.convolve(yp, k, mode='valid')

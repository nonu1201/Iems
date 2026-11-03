# Kiwi Ears Cadenza 2: Wavelet EQ presets (IEC 711 rig)

Chain: **Kiwi Ears Cadenza 2 → D07 USB DAC → Samsung Galaxy S23 → Wavelet**.
Data collected from squig.link on 2026-11-03. EQs generated with **AutoEq 4.1.2** (Python library).

| Target | Wavelet file (import this) | PEQ (reference) | Plot | EQ range | Preamp |
|---|---|---|---|---|---|
| **Thieaudio Monarch MK3** (IEM tuning) | [`wavelet/Thieaudio Monarch MK3.txt`](wavelet/Thieaudio%20Monarch%20MK3.txt) | [csv](peq/Thieaudio%20Monarch%20MK3.csv) · [APO](peq/Thieaudio%20Monarch%20MK3%20ParametricEQ.txt) | [png](plots/Thieaudio%20Monarch%20MK3.png) | +1.9 / −1.1 dB | −2.5 dB |
| **IEF Preference 2025** (711) | [`wavelet/IEF Preference 2025.txt`](wavelet/IEF%20Preference%202025.txt) | [csv](peq/IEF%20Preference%202025.csv) · [APO](peq/IEF%20Preference%202025%20ParametricEQ.txt) | [png](plots/IEF%20Preference%202025.png) | +1.6 / −2.1 dB | −2.1 dB |
| **Harman IE 2019v2** | [`wavelet/Harman IE 2019v2.txt`](wavelet/Harman%20IE%202019v2.txt) | [csv](peq/Harman%20IE%202019v2.csv) · [APO](peq/Harman%20IE%202019v2%20ParametricEQ.txt) | [png](plots/Harman%20IE%202019v2.png) | +3.0 / −2.1 dB | −3.5 dB |
| ***Non-Harman set*** | | | | | |
| **HBB Bad Guy 2022** (reviewer target) | [`wavelet/HBB Bad Guy 2022.txt`](wavelet/HBB%20Bad%20Guy%202022.txt) | [csv](peq/HBB%20Bad%20Guy%202022.csv) · [APO](peq/HBB%20Bad%20Guy%202022%20ParametricEQ.txt) | [png](plots/HBB%20Bad%20Guy%202022.png) | +1.9 / −2.4 dB | −2.5 dB |
| **Δ JM-1 −10 dB tilt** (711) | [`wavelet/Delta JM-1 -10dB Tilt.txt`](wavelet/Delta%20JM-1%20-10dB%20Tilt.txt) | [csv](peq/Delta%20JM-1%20-10dB%20Tilt.csv) · [APO](peq/Delta%20JM-1%20-10dB%20Tilt%20ParametricEQ.txt) | [png](plots/Delta%20JM-1%20-10dB%20Tilt.png) | +1.6 / −3.6 dB | −2.1 dB |
| **Truthear Hexa** (IEM tuning) | [`wavelet/Truthear Hexa.txt`](wavelet/Truthear%20Hexa.txt) | [csv](peq/Truthear%20Hexa.csv) · [APO](peq/Truthear%20Hexa%20ParametricEQ.txt) | [png](plots/Truthear%20Hexa.png) | +1.9 / −2.3 dB | −2.4 dB |

**Try first:** if you're not a Harman fan, start with **HBB Bad Guy 2022**. If you're fine with Harman-ish treble, start with Monarch MK3. Reasons are in [§6](#6-comparison-and-which-to-try-first).

---

## 0. Using the files in Wavelet

1. Copy the `.txt` file(s) from `wavelet/` to the phone.
2. In Wavelet, open the **AutoEq** section and use its **import** option to load the GraphicEQ file. Wavelet imports AutoEq's GraphicEQ format, and these files are exactly that format: one `GraphicEQ:` line with 127 bands.
3. **The preamp is already built in.** Every band is offset by the preamp, so the highest band sits at −0.5 dB or lower and the file cannot push the signal past 0 dBFS. Don't add another gain boost. Leaving Wavelet's limiter on is fine as an extra safety net.
4. For a fair comparison, switch off other processing: Samsung's Dolby Atmos, Adapt Sound and the built-in equalizer, plus Wavelet's other modules (bass boost, virtualizer and so on).
5. **USB DAC note:** players that take exclusive or "bit-perfect" control of the USB DAC bypass Android's audio effects, so Wavelet's EQ won't apply. Use normal (shared) Android output in the player. The 2–3.5 dB preamp costs a little volume; a USB dongle has plenty in reserve for an 18 Ω / 106 dB IEM. The Cadenza 2 is a single dynamic driver with a near-flat impedance curve, so the dongle's output impedance shouldn't change the tuning. I'm assuming the D07 is a typical low-output-impedance dongle.

---

## 1. Where the Cadenza 2 is measured on squig.link

I fetched squig.link's own site directory (`squig.link/squigsites.json`) and every **IEM** and **5128** database it lists (121 databases; 120 reachable, 1 returned 404), then searched each phone book. The **Cadenza 2 (a.k.a. Cadenza II) is on 30 databases**. I left out the original Cadenza everywhere, including Ankramutt's "Cadenza S2", which is sample 2 of the *original* Cadenza (same review link and price).

### IEC 60318-4 ("711") databases: 28 sites, 27 usable

squig.link files these under "IEMs", which means a 711-type occluded-ear simulator; most are clones. "Rig" quotes the site's own description where it gives one. *Dev* is each measurement's RMS deviation from the 27-site median (20 Hz–10 kHz, 1/6-oct).

| Site | Entry used (stock tips) | Rig as stated by the site | Dev |
|---|---|---|---|
| [MusiCafé](https://musicafe.squig.link/) | Kiwiears Cadenza 2 | not stated | 0.23 |
| [Bass Audio](https://bassaudio.squig.link/) | Kiwi Ears Cadenza 2 | Clone IEC 60318-4 Coupler | 0.29 |
| [Jaytiss](https://jaytiss.squig.link/) | KiwiCadenza2 | not stated | 0.29 |
| [boizoff](https://boizoff.squig.link/) | Cadenza II (wide stock silicone tips); also narrow, foam, reviewer fit | IEC 60318-4 clone | 0.34 |
| [Lumerion](https://lumerion.squig.link/) | Kiwi Ears Cadenza II | clone IEC 711 | 0.34 |
| [Paul Wasabi](https://pw.squig.link/) | Kiwi Ears Cadenza II | not stated | 0.39 |
| [Dung Le](https://dl.squig.link/) | Cadenza 2 (narrow tips); also wide | not stated | 0.44 |
| [Practiphile](https://practiphile.squig.link/) | Kiwi Ears Cadenza 2 | not stated | 0.50 |
| [ATechReviews](https://atechreviews.squig.link/) | Kiwi Ears Cadenza II; also shallow/deep fit, narrow/wide tips | not stated | 0.53 |
| [aden](https://aden.squig.link/) | KE Cadenza 2 LS (Linsoul unit) | clone 711 coupler, AET07 tips | 0.59 |
| [Audio Amigo](https://audioamigo.squig.link/) | Kiwi Ears Cadenza II | clone IEC 60318-4 | 0.64 |
| [TDL](https://squig.link/lab/tdl/) | Kiwi Ears Cadenza 2 | clone IEC 711 + KB006x ear | 0.65 |
| [AWSMDanny](https://awsmdanny.squig.link/) | Kiwi Ears Cadenza II | not stated | 0.69 |
| [Hawaii Bad Boy](https://hbb.squig.link/) | Ki Cad 2 (right channel only) | not stated | 0.70 |
| [Soundcheck39](https://soundcheck39.squig.link/) | Kiwi Ears Cadenza II | not stated | 0.72 |
| [Precogvision](https://precog.squig.link/) | Kiwiears Cadenza II | not stated | 0.75 |
| [Aftersound](https://aftersound.squig.link/) | KIWI EARS CADENZA 2 | not stated | 0.76 |
| [Fernanda Gunsan](https://squig.link/lab/fernandagunsan/) | Kiwi Ears Cadenza 2; also wide bore | IEC 711 | 0.78 |
| [Kuping Sensi](https://kuping-sensi.squig.link/) | Kiwi Ears Cadenza 2 | clone IEC 711 + KB006x ear | 0.81 |
| [The Audio Store](https://theaudiostore.squig.link/) | Kiwi Ears Cadenza II | not stated | 0.85 |
| [Headphone Zone](https://headphonezone.squig.link/) | Kiwi Cadenza II | IEC60318-4 occluded-ear simulator | 0.91 |
| [Bedrock Reviews](https://bedrock.squig.link/) | Kiwi Ears Cadenza II | not stated | 0.98 |
| [Joyce's Review](https://squig.link/lab/joycesreview/) | Kiwi Ears Cadenza II | not stated (template text left in config) | 1.01 |
| [dvewlsh](https://dvewlsh.squig.link/) | Kiwi Ears Cadenza 2; also stock wide, stock narrow | clone IEC 711 | 1.04 |
| [takeitslow7](https://takeitslow7.squig.link/) | kiwiears cadenza ii narrow (left channel only) | IEC 60318-4 ear simulator | 1.07 |
| [Soundignity](https://soundignity.squig.link/) | Kiwi Ears Cadenza II | clone IEC 711 | 1.12 |
| [Hobby Talk](https://hobbytalk.squig.link/) | Kiwi Ears Cadenza 2 | not stated | 1.95 |
| [SilicaGel](https://silicagel.squig.link/) | Cadenza II narrow / wide tip | IEC 60318-4 (711) | not used: newer graph tool, data path not reachable |

### B&K 5128 databases: 2 sites, not used

| Site | Entry | Why not used |
|---|---|---|
| [Hangout.Audio (Crinacle) 5128](https://graph.hangout.audio/iem/5128/) | Cadenza 2 | Data is served encrypted (premium tier). I did not try to get around that. |
| [Earphones Archive](https://earphonesarchive.squig.link/) | Kiwi Ears Cadenza II (short tip), (long tip) | Downloadable, but it's the only usable 5128 source |

### Rig decision: **IEC 711, used consistently for everything**

* There are 27 independent 711 measurements against 1 usable 5128 measurement.
* Harman IE 2019 and almost every reviewer house target were made for 711.
* The 711 measurements agree closely. Every site is within about 1.1 dB RMS of the median below 10 kHz, except Hobby Talk (1.95). So I used the **27-site median** as "the" Cadenza 2. That averages out unit-to-unit, fit and tip differences instead of betting on one sample. It's within 0.23 dB of MusiCafé's single measurement if you want to check it against one real curve. → [`data/cadenza2_711_consensus.csv`](data/cadenza2_711_consensus.csv), with all curves in [`data/cadenza2_711_all_measurements.csv`](data/cadenza2_711_all_measurements.csv) and metadata in [`data/sources.csv`](data/sources.csv).
* All targets below are 711 versions, and the "other IEM" targets were measured on the **same** 711 rigs as the Cadenza 2.

![Cadenza 2 on 711](plots/00%20Cadenza%202%20711%20measurements.png)

**What the stock Cadenza 2 looks like on 711** (relative to 500 Hz): a **+7.7 dB sub-bass shelf** (single 10 mm titanium-coated-PET dynamic driver, plus Kiwi's "KARS 2.0" sub-bass vent); a **+7.8 dB ear-gain peak around 2.8–3 kHz**; then a smooth fall through 4–8 kHz, a dip near 10 kHz, a peak near 12.5 kHz and roll-off after about 13 kHz. Against Harman IE 2019 that's the same bass, slightly fuller lower mids, and 2–3 dB less energy from 3 to 7 kHz. In other words, a warm, relaxed take on Harman.

**Tips:** five reviewers measured both stock tip types. Below 3 kHz they're the same (±0.2 dB). The **wide-bore tips are about 1 dB lower at 4–5 kHz and about 2 dB lower at 10 kHz** than the narrow ones. The median mixes both, so use whichever tip fits best, and remember that wide-bore makes any EQ sound a touch darker.

---

## 2. Target research (711 versions only)

Every target came from squig.link's own target files, and I compared copies from several sites. Harman IE 2019v2 is identical (≤0.03 dB) on 7 sites, Super 22 comes from Super* Review's site, Bad Guy 2022 from HBB's, and Precog from Precogvision's.

| Target | Author / year | What it is |
|---|---|---|
| **Harman IE 2019v2** | Harman (Olive et al.) | The research reference: bass shelf, big 3 kHz ear gain, raised 3–8 kHz |
| IEF Neutral 2023 | Crinacle | Tilted diffuse field translated to 711; modest bass |
| **IEF Preference 2025 (711)** | Crinacle, Feb 2025 | JM-1-based; +8 dB 105 Hz shelf and −4 dB 2.5 kHz high shelf on 711. A modern, very widely hosted "preference" target |
| Super* Review 22 | Super* Review | House target; little bass. Super* Review now leads with the Δ targets below |
| HBB Bad Guy 2022 | Hawaii Bad Boy | Bassy house target, more upper treble |
| Precogvision, Timmy, Banbeucmas, Antdroid, RikudouGoku, USound1V1 | reviewers / Usound | Older reviewer house targets (Banbeucmas ≈ Harman with less ear gain; Rikudou = basshead) |
| Δ 5128DF −10 dB tilt, Δ JM-1 −10 dB tilt | community (Listener's 5128→711 deltas) | The current "Δ meta": DF-based with a −1 dB/oct tilt |
| Moondrop VDSF | Moondrop | Moondrop house target |
| PEQdB IE | PEQdB, 2025 | Fitted from 455 online listening tests on 711-clone data |
| Δ SoundGuys | SoundGuys (711 delta) | Bassier, less 3–6 kHz, more treble |
| Diffuse Field, Etymotic | references | Neutral references, not preference targets |
| Δ Harman MoA 2025 (711) | Harman 2025 method-of-adjustment study, as a 5128→711 Δ | Harman's newest in-ear result. Hosted on Super* Review's site (not in its menu) and JaRaBa's. Only about +3 dB of bass shelf |

**Newer targets I couldn't use:**
* Headphones.com's IEM DF HRTF ("JM-2", April 2026) only exists on 711 as an untilted Δ DF, which isn't a preference target.
* HiFiEndgame, which topped PEQdB's own online test, isn't hosted on any 711 site I scanned.
* SilicaGel's "Harman IE MoA 2025 (Not Final)" variants are filter presets applied on top of a base curve, not standalone target files.

I also treated **24 well-known IEMs as targets**. These are the "sounds like IEM X" options: Truthear Hexa / Nova / Zero:Red / Gate, Moondrop Blessing 3 / Variations / Aria 2 / Kato / Chu 2, Thieaudio Monarch MK3, Simgot EA500LM / EM6L / EW300, Sennheiser IE 600 / IE 900, Tanchjim Origin, Dunu Kima 2, 7Hz Timeless, Kinera Celest Pandamon 2.0, Letshuoer S12, Kiwi Ears Orchestra Lite, 64 Audio U12t, Moondrop Blessing 2 and Etymotic ER4XR. The last three were measured by fewer than 5 of these sites, so they weren't ranked. The original Cadenza was built the same way, but only as a reference; it isn't a candidate. For each one I took every site that measured **both** that IEM and the Cadenza 2, computed *(IEM − Cadenza 2) on that same rig*, and used the median across sites. Coupler quirks cancel out, so the result is a true same-rig target.

### Ranking by how much EQ each target needs

![Target ranking](plots/01%20Target%20EQ-effort%20ranking.png)

Full numbers are in [`data/target_ranking.csv`](data/target_ranking.csv), including per-region error, largest boost and cut, and how much "air" above 10 kHz each target wants.

**Why most targets are a poor fit for this IEM:** a large share of them want the Cadenza 2's 10 kHz dip filled and more air added above it. That's the region you asked me not to boost. It's also where 711 measurements are least reliable and where a single dynamic driver like this one is already rolling off. So "least EQ" and "suits the driver" both point to targets that are already happy with its top end and its sub-bass shelf.

### The three picks (first set)

1. **IEF Preference 2025 (711): the least-change modern target.** It needs 0.91 dB RMS of correction, with no boost over +1.5 dB and **essentially no air above 10 kHz (0.09 dB)**. Its bass matches the Cadenza 2's KARS shelf within 0.2 dB, so the driver's strongest feature is left alone. The main move is a **1.5–2 dB cut at 5–8 kHz**; cuts are the safest EQ on a single dynamic driver. It also adds about +1.5 dB at 3 kHz and about +1 dB at 500–600 Hz.
   *Version caveat:* Crinacle's own 711 file sits behind his encrypted graph tool, so I used the most widely shared copy, which is identical on three sites (ATechReviews, Fahryst, OB Odio). The PEQdB paper says Crinacle made his 711 version by measuring a 5128-compliant IEM on a 711 clone. That would explain why the copy doesn't exactly equal his published shelves applied to Listener's Δ JM-1: that recipe version is 1.5–3 dB brighter at 6–9 kHz; that version is in [`data/targets/IEF Preference 2025 (711 recipe).csv`](data/targets/IEF%20Preference%202025%20(711%20recipe).csv). Below 5 kHz the two agree within about 1 dB.
2. **Harman IE 2019v2: the research reference, and the brighter option.** You asked for it, and it's the most-studied preference target. The Cadenza 2's **bass already matches Harman better than any other target** (0.47 dB RMS from 20 to 200 Hz). What's missing is Harman's 3–7 kHz energy. So the EQ trims the lower mids (−2 dB at 300 Hz) and lifts the presence and lower treble by 1.5–3 dB. It doesn't need air boosts (0.7 dB). Of the three it's the biggest change (1.40 dB RMS), but it's all in one broad, gentle region.
3. **Thieaudio Monarch MK3 (IEM tuning).** It's the third-closest of the 41 ranked candidates (0.82 dB RMS), built from 8 sites that measured both IEMs. Bass and sub-bass already match within 0.3 dB. To sound like the MK3 below 10 kHz, the Cadenza 2 only needs −1 dB in the lower mids and at 3 kHz, plus +1.5–2 dB at 5–8 kHz. The MK3 is among the most widely praised all-rounder tunings. *Limit:* it also wants about +2 dB of air above 10 kHz from its electrostatic tweeters, which I deliberately left out. So this gives you the MK3's tonal balance, not its upper-treble extension or technicalities.

**Why not Harman's newer 2025 (MoA) target:** on 711 it needs 2.10 dB RMS (32nd of 41). It wants about 4 dB *less* sub-bass than the Cadenza 2 has, so it would undo the KARS shelf, and it wants +4.5 dB at 10 kHz.

**Why not the ones ranked above the MK3:**
* Truthear Gate (0.66) is a $20 single dynamic driver that's already a near-twin of the Cadenza 2, so it changes very little.
* Banbeucmas (0.70) is a 2021 reviewer target that's essentially Harman with less ear gain, so it overlaps the Harman pick.
* **Truthear Zero:Red (0.86) is the best runner-up.** It's dual-DD, neutral with bass, with slightly less sub-bass and more 7–9 kHz. Its target CSV is in `data/targets/`; add it to `TARGETS` in `scripts/build_eq.py` to generate it.

### The non-Harman set (second request)

**Rules:**
* No Harman target: neither IE 2019v2 nor MoA 2025.
* Nothing that is Harman-based or measures like Harman. That rules out USound1V1, which is built on Harman, and Banbeucmas, which sits within 1 dB RMS of Harman.
* The EQ'd Cadenza 2 must end up **further from Harman than the stock Cadenza 2 already is**. The stock unit is 1.49 dB RMS from Harman IE 2019v2 (20 Hz–10 kHz, mean-aligned).

Within those rules: small EQ, suits the single dynamic driver, and three clearly different flavors that don't repeat IEF Preference 2025.

Every remaining candidate went through the same constrained AutoEq run:

| Candidate | EQ range (dB) | Error after EQ | Distance from Harman after EQ | Character of the change |
|---|---|---|---|---|
| **HBB Bad Guy 2022** | +1.9 / −2.4 | 0.86 | **2.03** | more mid-bass, **less 1–5 kHz**, a little 7–9 kHz sparkle |
| **Δ JM-1 −10 dB tilt** | +1.6 / −3.6 | 0.58 | **2.51** | **−3 dB sub-bass**, fuller 200–500 Hz, smoother 5–6 kHz |
| **Truthear Hexa** (IEM, 18 sites) | +1.9 / −2.3 | 0.71 | **1.77** | same sub-bass, less 2 kHz and 4–5 kHz glare, more 7–8 kHz |
| Simgot EW300 (IEM) | +1.8 / −2.2 | 0.45 | 1.88 | warmer: +1.8 dB at 150 Hz, −1.9 dB at 6 kHz (overlaps HBB / IEF) |
| Dunu Kima 2 (IEM, single DD) | +2.0 / −4.5 | 0.28 | 2.44 | same direction as JM-1 but a deeper −4.5 dB cut |
| Kiwi Ears Orchestra Lite (IEM) | +1.1 / −3.3 | 0.54 | 2.26 | darker and more relaxed: −1.7 to −2.3 dB at 3–6 kHz, less sub-bass |
| Moondrop Kato (IEM) | +1.7 / −2.7 | 0.53 | 1.88 | less sub-bass, a little more 7–8 kHz |
| Moondrop Aria 2 (IEM) | +1.9 / −3.6 | 0.54 | 2.08 | less sub-bass, otherwise small |
| 7Hz Timeless (IEM) | +2.0 / −2.8 | 0.60 | 2.03 | −2 to −2.7 dB at 3–4 kHz |
| Δ SoundGuys | +1.7 / −2.6 | 0.96 | 2.07 | fuller lower mids; wants +3.5 dB of air above 10 kHz |
| Precogvision | +2.4 / −4.3 | 0.68 | 2.57 | a big −4.3 dB cut at 3 kHz (too drastic) |
| Timmy, Antdroid | +2.8 / −1.9, +1.4 / −2.2 | 0.72, 0.76 | 1.55, 1.72 | barely away from Harman (Timmy) / older target (Antdroid) |

For reference: IEF Preference 2025 lands at 2.09 from Harman after EQ (it moves away). **Monarch MK3 lands at 1.22, which is slightly *closer* to Harman than stock**, mostly because of its 5–8 kHz lift.

**Why these three:**
1. **HBB Bad Guy 2022: the most direct opposite of Harman's upper mids.** It's Hawaii Bad Boy's own house target. I couldn't find documentation of how it was built, so the "not Harman" claim rests on the measurement: the EQ'd result is 2.03 from Harman.
   * On the Cadenza 2 it takes **1–2.2 dB out of 1–5 kHz**, where Harman's "shouty" ear gain lives. It adds +1 to +1.9 dB of mid-bass punch at 50–200 Hz and keeps the sub-bass.
   * A small +1 to +1.5 dB at 7–9 kHz keeps it from sounding dull.
   * Its error after EQ (0.86) is the highest of the set only because it also wants up to +6 dB at 9–10 kHz, which the no-boost rule removes. Below 9 kHz it tracks the target closely.
2. **Δ JM-1 −10 dB tilt (711): the modern diffuse-field approach.** It's a JM-1 population-average HRTF with a −1 dB/oct tilt, Super* Review's current default, and the base of Crinacle's IEF 2025. It's the **farthest from Harman** of the set (2.51).
   * On the Cadenza 2 it is mainly a **−3 dB sub-bass cut** plus about +1 dB at 200–500 Hz: more natural, fuller mids and less boom. It also trims 5–6 kHz by about 2 dB.
   * It's mostly cuts (largest boost only +1.6 dB). Trade-off: you lose some of the KARS sub-bass slam, and 3 kHz gets relatively a bit more forward (+1.6 dB).
3. **Truthear Hexa (IEM tuning): the neutral benchmark.** It's built from 18 sites that measured both IEMs, the most robust IEM target here, and was the most-selected IEM in PEQdB's listening test.
   * The Cadenza 2 keeps its sub-bass and loses some upper-mid glare (−1.8 dB at 2 kHz, −2.1 dB at 5 kHz), with +1.6–1.7 dB of sparkle at 7–8 kHz.
   * The treble limits mean you get a gentle share of Hexa's 7–9 kHz peak, not the full +4 dB.

**Runners-up**, if one of these three misses:
* Simgot EW300: warm, the lowest effort.
* Dunu Kima 2: another single dynamic driver, the closest match after EQ (0.28 dB), in the same direction as JM-1.
* Kiwi Ears Orchestra Lite: the darkest and most relaxed option.

All three target CSVs are in `data/targets/`.

---

## 3. How the EQ was generated (AutoEq 4.1.2)

The script is [`scripts/build_eq.py`](scripts/build_eq.py). Settings:

* `FrequencyResponse.process(target, min_mean_error=True, max_gain=6, treble_f_lower=5000, treble_f_upper=10000, treble_gain_k=0.5)`, with AutoEq's default smoothing (1/12 octave, widening to 2 octaves in the treble). `min_mean_error` aligns the target to the measurement so that the overall correction is as small as possible.
* **Gentle treble:**
  * EQ strength fades to 50 % from 5 kHz upward.
  * Treble changes at 5 kHz and above are limited to **+3 / −4 dB**.
  * **No boost at or above 10 kHz:** positive gain fades to 0 dB between 8.5 and 10 kHz, and only cuts are allowed above that.
* **Preamp** = −(largest boost + 0.5 dB headroom), rounded down. It's baked into the GraphicEQ file and listed in each PEQ table.
* **PEQ table** (fitted with AutoEq's optimizer at 48 kHz):
  * a 105 Hz low shelf;
  * a 10 kHz high shelf that can only cut;
  * 4 peaking filters up to 5 kHz (Q ≤ 3);
  * 2 broad peaking filters at 4–9 kHz (Q ≤ 1.5, gain from −4 to +3 dB).

  If any filter's skirt leaks boost above 10 kHz, the shelf is deepened automatically to cancel it. Each PEQ matches its GraphicEQ curve within 0.08–0.27 dB RMS (20 Hz–10 kHz), and none of them boosts above 10 kHz.

---

## 4. Results per target

Plots show the stock Cadenza 2 (blue), the EQ'd Cadenza 2 (orange) and the target (dashed). The top panel leaves the preamp out so the curves overlay. The bottom panel shows the EQ curve with the preamp included.

### IEF Preference 2025 (711)

File: [`wavelet/IEF Preference 2025.txt`](wavelet/IEF%20Preference%202025.txt). Error vs target: **1.00 → 0.41 dB RMS**.

| # | Type | Freq (Hz) | Gain (dB) | Q |
|---|---|---|---|---|
| – | **Preamp** | | **−2.4** | |
| 1 | Low shelf | 105 | +0.7 | 0.70 |
| 2 | Peak | 616 | +2.0 | 1.11 |
| 3 | Peak | 1211 | −1.7 | 0.99 |
| 4 | Peak | 3034 | +2.8 | 2.09 |
| 5 | Peak | 4582 | −1.1 | 2.21 |
| 6 | Peak | 5544 | −2.1 | 1.07 |
| 7 | Peak | 6078 | +0.8 | 1.50 |
| 8 | High shelf | 10000 | −0.7 | 0.70 |

![IEF Preference 2025](plots/IEF%20Preference%202025.png)

### Harman IE 2019v2

File: [`wavelet/Harman IE 2019v2.txt`](wavelet/Harman%20IE%202019v2.txt). Error vs target: **1.49 → 0.67 dB RMS**.

| # | Type | Freq (Hz) | Gain (dB) | Q |
|---|---|---|---|---|
| – | **Preamp** | | **−3.5** | |
| 1 | Peak | 103 | −0.6 | 1.76 |
| 2 | Peak | 328 | −2.1 | 1.08 |
| 3 | Peak | 1442 | −1.5 | 1.57 |
| 4 | Peak | 3703 | +1.5 | 0.93 |
| 5 | Peak | 6671 | +3.0 | 1.36 |
| 6 | Peak | 8251 | −0.9 | 1.50 |
| 7 | High shelf | 10000 | −1.3 | 0.70 |

![Harman IE 2019v2](plots/Harman%20IE%202019v2.png)

### Thieaudio Monarch MK3 (711, same-rig)

File: [`wavelet/Thieaudio Monarch MK3.txt`](wavelet/Thieaudio%20Monarch%20MK3.txt). Error vs target: **0.87 → 0.48 dB RMS**.

| # | Type | Freq (Hz) | Gain (dB) | Q |
|---|---|---|---|---|
| – | **Preamp** | | **−2.3** | |
| 1 | Peak | 157 | +0.7 | 0.54 |
| 2 | Peak | 320 | −0.5 | 1.50 |
| 3 | Peak | 336 | −0.9 | 1.04 |
| 4 | Peak | 960 | −0.4 | 0.80 |
| 5 | Peak | 4000 | −1.2 | 0.73 |
| 6 | Peak | 5932 | +2.7 | 1.26 |
| 7 | High shelf | 10000 | −0.8 | 0.70 |

Filters 2 and 3 are AutoEq's fit as-is; together they act as one −1.4 dB dip around 330 Hz.

![Thieaudio Monarch MK3](plots/Thieaudio%20Monarch%20MK3.png)

### HBB Bad Guy 2022 (non-Harman set)

File: [`wavelet/HBB Bad Guy 2022.txt`](wavelet/HBB%20Bad%20Guy%202022.txt). Error vs target: **1.44 → 0.86 dB RMS**.

| # | Type | Freq (Hz) | Gain (dB) | Q |
|---|---|---|---|---|
| – | **Preamp** | | **−2.5** | |
| 1 | Low shelf | 105 | +0.8 | 0.70 |
| 2 | Peak | 174 | +2.0 | 0.96 |
| 3 | Peak | 331 | −1.6 | 1.98 |
| 4 | Peak | 709 | +0.7 | 1.77 |
| 5 | Peak | 1308 | −1.3 | 1.00 |
| 6 | Peak | 4907 | −3.4 | 1.50 |
| 7 | Peak | 6790 | +2.8 | 1.50 |
| 8 | High shelf | 10000 | −1.0 | 0.70 |

![HBB Bad Guy 2022](plots/HBB%20Bad%20Guy%202022.png)

### Δ JM-1 −10 dB tilt (711) (non-Harman set)

File: [`wavelet/Delta JM-1 -10dB Tilt.txt`](wavelet/Delta%20JM-1%20-10dB%20Tilt.txt). Error vs target: **1.87 → 0.58 dB RMS**.

| # | Type | Freq (Hz) | Gain (dB) | Q |
|---|---|---|---|---|
| – | **Preamp** | | **−2.3** | |
| 1 | Peak | 44 | −1.3 | 0.70 |
| 2 | Low shelf | 105 | −2.8 | 0.70 |
| 3 | Peak | 252 | +1.5 | 0.22 |
| 4 | Peak | 1457 | −2.6 | 1.02 |
| 5 | Peak | 3040 | +2.9 | 2.22 |
| 6 | Peak | 5156 | −2.8 | 1.50 |
| 7 | Peak | 6581 | +0.7 | 1.50 |
| 8 | High shelf | 10000 | −0.4 | 0.70 |

![Δ JM-1 −10 dB tilt](plots/Delta%20JM-1%20-10dB%20Tilt.png)

### Truthear Hexa (711, same-rig) (non-Harman set)

File: [`wavelet/Truthear Hexa.txt`](wavelet/Truthear%20Hexa.txt). Error vs target: **1.29 → 0.71 dB RMS**.

| # | Type | Freq (Hz) | Gain (dB) | Q |
|---|---|---|---|---|
| – | **Preamp** | | **−1.9** | |
| 1 | Peak | 51 | −2.7 | 0.67 |
| 2 | Low shelf | 105 | +1.7 | 0.70 |
| 3 | Peak | 191 | +1.4 | 2.07 |
| 4 | Peak | 2030 | −1.9 | 1.38 |
| 5 | Peak | 3224 | +2.9 | 2.86 |
| 6 | Peak | 4887 | −3.6 | 1.36 |
| 7 | Peak | 7170 | +3.0 | 1.50 |
| 8 | High shelf | 10000 | −1.3 | 0.70 |

![Truthear Hexa](plots/Truthear%20Hexa.png)

The `peq/* ParametricEQ.txt` files hold the same filters in EqualizerAPO format, for apps that import PEQ.

---

## 5. What each EQ changes (GraphicEQ curve, before preamp)

| Region | IEF Preference 2025 | Harman IE 2019v2 | Monarch MK3 |
|---|---|---|---|
| Sub-bass 20–50 Hz | +0.2 to +0.9 | 0 | +0.2 to +0.3 |
| Mid-bass 100 Hz | +0.8 | −0.7 | +0.5 |
| Lower mids 300–500 Hz | +0.3 to +1.2 | **−2.0 to −1.3** | −1.1 to −0.6 |
| 1 kHz | −0.8 | −0.7 | −0.6 |
| Ear gain 3 kHz | **+1.6** | +1.4 | −0.8 |
| Presence 4–5 kHz | −0.8 to **−1.9** | **+2.1 to +2.5** | +0.4 to +0.9 |
| Lower treble 6–8 kHz | −1.7 to −0.5 | **+3.0 to +1.3** | **+1.6 to +1.8** |
| ≥10 kHz | cuts only (−1.6 to 0) | 0 to −1.0 | 0 |

Non-Harman set:

| Region | HBB Bad Guy 2022 | Δ JM-1 −10 dB tilt | Truthear Hexa |
|---|---|---|---|
| Sub-bass 20–50 Hz | +0.3 to +1.0 | **−2.9 to −3.2** | +1.2 to −1.0 |
| Mid-bass 100–200 Hz | **+1.1 to +1.6** | −0.9 to +1.4 | −0.4 to +1.0 |
| Lower mids 300–500 Hz | −0.4 to 0 | +0.8 to +1.1 | +0.1 to −0.1 |
| 1–2 kHz | −0.8 to −0.9 | −1.0 to −1.3 | −0.4 to **−1.8** |
| Ear gain 3 kHz | **−1.0** | +1.6 | +0.7 |
| Presence 4–5 kHz | **−1.9 to −2.2** | −0.7 to −2.1 | −1.3 to **−2.1** |
| Lower treble 6–9 kHz | 0 to +1.5 | −1.7 to −0.2 | −0.7 to **+1.7** |
| ≥10 kHz | 0 | cuts only (−1.0 to 0) | 0 |

## 6. Comparison and which to try first

### Non-Harman set

| | **HBB Bad Guy 2022** | **Δ JM-1 −10 dB tilt** | **Truthear Hexa** |
|---|---|---|---|
| Size of change | small (+1.9 / −2.4 dB) | small boosts, one bigger cut (+1.6 / −3.6 dB) | small (+1.9 / −2.3 dB) |
| Distance from Harman (stock = 1.49) | 2.03 | **2.51** (farthest) | 1.77 |
| Sound vs stock | Warmer and punchier; vocals and guitars sit back a little, so it's never shouty; a touch of treble sparkle keeps it clear. The "fun but relaxed" option. | Less sub-bass rumble, fuller and more natural lower mids, smoother lower treble. Sounds more like speakers in a room and less like an IEM with a bass shelf. | Keeps the sub-bass, cleans up upper-mid glare at 2 and 5 kHz, adds crisp sparkle at 7–8 kHz. Neutral, tidy and the most "detailed" of the three. |
| Suits | People who find Harman shouty or fatiguing; rock, pop, hip-hop at moderate volume | People who find Harman's bass shelf boomy or its mids thin; acoustic, jazz, classical, vocals | Neutral/reference fans who want clarity without Harman's 3 kHz push |

**Not a Harman fan: try HBB Bad Guy 2022 first.** It addresses two common complaints about Harman, the upper-mid push and lean lower mids, with small changes, and it keeps the Cadenza 2's bass. Then:
* **want less bass and more natural mids** → **Δ JM-1 −10 dB tilt**;
* **want it cleaner and crisper** → **Truthear Hexa**;
* **want the stock bass with only smoother treble** → **IEF Preference 2025**, from the first set.

One thing to know about the first set: **Monarch MK3 moves the Cadenza 2 slightly toward Harman** (1.22 vs 1.49 stock) because of its 5–8 kHz lift, so skip it if Harman's treble is what bothers you.

### First set

| | **Monarch MK3** | **IEF Preference 2025** | **Harman IE 2019v2** |
|---|---|---|---|
| Size of change | smallest (+1.9 / −1.1 dB) | small (+1.6 / −2.1 dB) | moderate (+3.0 / −2.1 dB) |
| Distance from Harman (stock = 1.49) | 1.22 (slightly toward Harman) | 2.09 | 0.67 (it is Harman) |
| Sound vs stock | Same bass, slightly cleaner lower mids, a touch less 3 kHz push, more 5–8 kHz sparkle. More open and "detailed" without getting shouty. | Same punchy sub-bass, a bit more body in the lower mids, vocals slightly more forward at 3 kHz, smoother and less sibilant at 5–8 kHz. The warmest and most relaxed of the three. | Same sub-bass, leaner lower mids, clearly more 3–7 kHz energy: crisper vocals, guitars and cymbals. The brightest and most "clear", with the most risk of sibilance on hot recordings. |
| Suits | All-rounders who want a bit more clarity and air without changing the Cadenza 2's character | Treble-sensitive listeners, long sessions, loud listening, warm/smooth lovers | People who find the stock Cadenza 2 a little warm, veiled or polite; reference/Harman fans; pop, rock, EDM |

**Try Monarch MK3 first** (if Harman isn't a concern). It's the smallest change of the three. It keeps the Cadenza 2's bass exactly as it is, and it adds the kind of 5–8 kHz sparkle that a single dynamic driver handles comfortably at +2 dB. Then:
* **too bright or sibilant** → switch to **IEF Preference 2025**;
* **vocals still feel a bit distant or the sound a bit warm** → try **Harman IE 2019v2**.

---

## Caveats

* Couplers aren't ears. Your insertion depth, ear canal and tip seal change everything above about 5 kHz, which is why the treble EQ is gentle and nothing is boosted above 10 kHz. Bass depends mostly on seal: if the bass sounds thin, fix the fit before touching the EQ.
* Unit-to-unit variation is small for this IEM (the 27 measurements agree within about 1 dB below 10 kHz), but your unit isn't the median.
* The "IEM" target matches the MK3's frequency response on a 711 coupler below 10 kHz only.

## Reproducing

```bash
python3.11 -m venv .venv && . .venv/bin/activate   # AutoEq 4.1.2 needs Python 3.8–3.11
pip install -r requirements.txt
python scripts/build_eq.py        # wavelet/, peq/, per-target plots
cd scripts && python plot_overview.py   # overview plots
```

* `data/cadenza2_711_consensus.csv`: the measurement used, in AutoEq CSV format (`frequency,raw`, 300 Hz–3 kHz mean = 0).
* `data/cadenza2_711_all_measurements.csv`: all 38 711 curves (defaults plus tip and fit variants), on the same grid.
* `data/targets/*.csv`: every target considered, including the 25 same-rig IEM targets.
* `data/sources.csv`, `data/target_ranking.csv`: metadata and the ranking.

## Sources

* squig.link site directory and databases: [squig.link](https://squig.link/) (`squigsites.json`, each site's `data/phone_book.json`, measurement and target files); full list in `data/sources.csv`
* Crinacle, [The New 2025 IEF Target](https://crinacle.com/2025/02/05/the-new-2025-ief-target/)
* PEQdB, [Comparative Evaluation of Headphone Target Curves](https://peqdb.com/wiki/PEQdB-Comparitive-Evaluation-of-Headphone-Target-Curves.pdf) (vendor-run online test; treat as indicative)
* [IEM EQ Guide: Rigs, Curves & Targets](https://iem-eq-guide.pages.dev/rigs-curves-targets/)
* Kiwi Ears Cadenza II specs: [Linsoul](https://www.linsoul.com/products/kiwi-ears-cadenza-ii), [Headphoneer review](https://www.headphoneer.com/kiwi-ears-cadenza-ii-review/)
* Wavelet GraphicEQ import: [XDA](https://www.xda-developers.com/wavelet-latest-update-more-features-headphones-sound-better/)
* [AutoEq](https://github.com/jaakkopasanen/AutoEq) (PyPI `autoeq` 4.1.2)

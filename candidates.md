# Eksplorasi & Seleksi Kandidat: Warning Label for Humans

## Kriteria Juri (Urutan Prioritas)
1. **On-subject & Laugh**: Benar-benar satu baris label peringatan keselamatan untuk setiap manusia dan cukup lucu untuk mengundang tawa.
2. **Late Turn**: Tawa mendarat dalam satu bacaan, dengan belokan tajam di beberapa kata terakhir (bukan tersebar sepanjang kalimat).
3. **Human Recognition**: Terasa nyata tentang perilaku manusia secara umum, bukan absurditas acak atau klise usang.
4. **Authentic Label Form**: Meniru diksi dan ritme label peringatan tercetak sungguhan sehingga komedi muncul dari bentuknya.
5. **Tight Fit**: <= 160 karakter, satu ide utuh tanpa basa-basi, tanpa ide ganda, dan tanpa pengulangan.

## Daftar Kandidat Awal (10 Kandidat)

| ID | Teks Kandidat | Panjang (char) | Catatan Awal |
|----|---------------|----------------|--------------|
| A | `CAUTION: Do not operate when hungry, tired, or mildly criticized; unit cannot tell the difference.` | 98 | Sangat relatable, ritme alat berat; "mildly criticized" sedikit membocorkan belokan sebelum titik koma. |
| B | `WARNING: Contains no user-serviceable parts; if visibly damaged, unit will insist it is fine.` | 93 | Diksi label elektronik sangat autentik; belokan 5 kata terakhir sangat rapi, premis "I'm fine" cukup klasik. |
| C | `WARNING: Do not leave idle; in the absence of real danger, unit will manufacture its own.` | 89 | Sangat deadpan-klinis sampai akhir; kebenaran universal manusia (overthinking/menciptakan krisis saat tenang). |
| D | `WARNING: Unit will read this safety label in full, nod thoughtfully, and assume it applies to everyone else.` | 108 | Meta-humor tajam, tetapi frasa "nod thoughtfully" lebih naratif daripada diksi label tercetak asli. |
| E | `WARNING: Exposure to a single minor inconvenience may cause unit to reconsider its entire life.` | 95 | Sangat lucu dan tepat sasaran; frasa "minor inconvenience" sedikit menurunkan register klinis di tengah kalimat. |
| F | `WARNING: Unit will ignore all posted warnings, proceed anyway, and blame the manufacturer.` | 90 | Memainkan bentuk label peringatan dengan baik; sedikit terprediksi pada klausa kedua. |
| G | `CAUTION: Contents settle with age and will begin making involuntary noises when standing up.` | 92 | Parodi label kemasan yang rapi dan relatable, tetapi cenderung ke lelucon usia daripada manusia secara keseluruhan. |
| H | `WARNING: Read all instructions before use; unit will not, and will resent anyone who does.` | 90 | Ringkas dan lucu, tetapi belokan terbagi menjadi dua klausa ("will not" lalu "will resent"). |
| I | `CAUTION: Do not leave unattended in a quiet room; unit may replay an awkward remark from 2014.` | 94 | Terlalu dekat dengan meme internet umum dan tahun spesifik ("2014") mengurangi kesan abadi. |
| J | `WARNING: Do not assume unit is functioning normally simply because it insists it is fine.` | 89 | Rapi dan tajam, namun kalah autentik gaya labelnya dibanding B. |

## Simulasi Perbandingan Berpasangan (A vs B)

### Babak Penyisihan (Top 5: A, B, C, D, E)
- **C vs D**: Menang **C** (margin 2). C mempertahankan nada label industri resmi hingga 5 kata terakhir (`unit will manufacture its own`), sedangkan D langsung melanggar nada label resmi lewat `nod thoughtfully`.
- **C vs E**: Menang **C** (margin 2). Keduanya sangat lucu dan universal, tetapi E mulai memicu senyum di tengah kalimat (`single minor inconvenience`), sementara C menjaga ketegangan deadpan penuh sampai ujung kalimat.
- **B vs A**: Menang **A** (margin 1). B memiliki diksi label lebih murni, tetapi A punya wawasan psikologis yang lebih segar dan mengejutkan (manusia tidak bisa membedakan lapar, lelah, dan kritik ringan).
- **C vs A**: Menang **C** (margin 2). C lebih ketat pada kriteria 2 (satu ide dengan belokan murni di akhir) dan kriteria 4 (register label keselamatan tanpa daftar 3 item).
- **C vs B**: Menang **C** (margin 2). Premis "menciptakan bahaya sendiri saat tidak ada bahaya nyata" lebih segar, tajam, dan tidak seklise premis "insist it is fine".

## Kandidat Terpilih Sementara (Milestone 2)
- **Pemenang Milestone 2**: Kandidat **C** (89 karakter, 89 byte UTF-8)
  `WARNING: Do not leave idle; in the absence of real danger, unit will manufacture its own.`

## Revisi & Pemolesan (Milestone 3)

### Uji Penantang Baru (K–O) vs Kandidat C
| ID | Teks Penantang | Panjang (char) | Evaluasi vs C |
|----|----------------|----------------|---------------|
| K | `WARNING: Do not trust unit's self-assessment; unit believes it is an above-average driver, listener, and judge of character.` | 124 | Terlalu panjang dan memakai daftar tiga hal (melanggar kriteria 5). |
| L | `WARNING: May cause sudden confidence in subjects it read one paragraph about; discontinue speaking immediately.` | 111 | Sintaks tengah kurang luwes dibanding ritme label singkat C. |
| N | `WARNING: Do not ask "are you sure?" after unit has already started; unit will double down until catastrophic failure.` | 117 | Lucu, tetapi kutipan dialog awal memecah suara label resmi lebih cepat daripada C. |

### Pemolesan Diksi & Ritme Kandidat C
- **C0 (Milestone 2)**: `WARNING: Do not leave idle; in the absence of real danger, unit will manufacture its own.` (89 char)
- **C1 (Revisi)**: `WARNING: Do not leave unattended; in the absence of real danger, unit will manufacture its own.` (95 char)
- **C2 (Alternatif)**: `WARNING: Do not leave unattended; if no real emergency is present, unit will manufacture one.` (93 char)

**Perbandingan C0 vs C1 vs C2**:
- **C1 vs C0**: Menang **C1** (margin 2). Frasa `WARNING: Do not leave unattended;` adalah kalimat label keselamatan tercetak yang jauh lebih ikonik dan langsung dikenali (Kriteria 4) dibanding `Do not leave idle;`, tanpa mengorbankan kejutan 5 kata terakhir (`unit will manufacture its own.`).
- **C1 vs C2**: Menang **C1** (margin 1). Kata `in the absence of real danger` lebih klinis sekaligus menajamkan kontras psikologis (`real danger` vs `its own`), sehingga pukulan penutupnya lebih padat dan deadpan.

## Kandidat Final Terpilih (Milestone 3)
- **Final**: `WARNING: Do not leave unattended; in the absence of real danger, unit will manufacture its own.`
- **Statistik**: 95 karakter, 95 byte UTF-8, 1 baris utuh tanpa newline, tanpa ide ganda, seluruh baris meniru gaya label keselamatan cetak hingga belokan 5 kata terakhir.


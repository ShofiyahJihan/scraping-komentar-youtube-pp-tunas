from itertools import islice
from youtube_comment_downloader import YoutubeCommentDownloader
import pandas as pd

# ====== ISI BAGIAN INI ======
URL = "https://youtube.com/shorts/hzDavp3DQo4?si=mpprzFPtM_DjH4HQ"  # video tentang PP Tunas / larangan medsos anak
JUMLAH = 300                                          # jumlah komentar yang diambil
# ============================

# Kata kunci untuk text mining kasus PP Tunas
KATA_KUNCI = [
    "roblox", "judi", "hoax", "medsos", "game", "umur", "anak",
    "orang tua", "komdigi", "pemerintah", "akun", "setuju",
    "tidak setuju", "youtube", "tiktok", "pp tunas"
]

def ambil_komentar(url, jumlah):
    """Ambil komentar video YouTube (username tidak disimpan)."""
    downloader = YoutubeCommentDownloader()
    hasil = []
    for c in islice(downloader.get_comments_from_url(url), jumlah):
        hasil.append({
            "waktu": c["time"],                 # contoh: "3 bulan yang lalu"
            "tanggal": c.get("time_parsed"),    # perkiraan tanggal (timestamp)
            "like": c["votes"],
            "komentar": " ".join(c["text"].split()),
        })
    return hasil


def bersihkan(df):
    """Hapus komentar kosong dan duplikat."""
    df = df[df["komentar"].str.strip() != ""]
    df = df.drop_duplicates(subset="komentar")
    return df.reset_index(drop=True)


def hitung_kata_kunci(df):
    """Hitung berapa komentar yang menyebut tiap kata kunci (kata utuh)."""
    hasil = {}
    for k in KATA_KUNCI:
        pola = rf"\b{k}\b"
        hasil[k] = int(df["komentar"].str.contains(pola, case=False, regex=True).sum())
    return hasil


if __name__ == "__main__":
    df = pd.DataFrame(ambil_komentar(URL, JUMLAH))

    # ubah timestamp ke tanggal agar bisa dicek (harus sesudah PP Tunas berlaku, 28 Maret 2026)
    df["tanggal"] = pd.to_datetime(df["tanggal"], unit="s", errors="coerce").dt.date

    bersih = bersihkan(df)

    bersih.to_csv("komentar_pptunas.csv", index=False, sep=";", encoding="utf-8-sig")

    print("Komentar diambil     :", len(df))
    print("Setelah dibersihkan  :", len(bersih))
    print("Rentang tanggal      :", bersih["tanggal"].min(), "sampai", bersih["tanggal"].max())

    print("\nKata kunci:")
    hasil = hitung_kata_kunci(bersih)
    for kata, jumlah in sorted(hasil.items(), key=lambda x: x[1], reverse=True):
        print(" -", kata, ":", jumlah)

    print("\n5 komentar dengan like terbanyak:")
    print(bersih.sort_values("like", ascending=False).head(5)[["like", "komentar"]])
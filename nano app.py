from flask import Flask, render_template_string, request, jsonify
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(32)

# --- إعدادات الحماية القصوى لـ SHADOW ---
MASTER_KEY = "SHADOW_ADMIN_2026"  # غير هذه الكلمة لفتح لوحة التحكم
PORT = 8080

# واجهة التمويه (صفحة المتجر المؤمنة)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <title>Secure Gateway | Back Link</title>
    <style>
        body { background: #0d0d0d; color: #00ff41; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; display: flex; align-items: center; justify-content: center; height: 100vh; margin: 0; overflow: hidden; }
        .terminal { background: rgba(0, 0, 0, 0.9); padding: 30px; border: 1px solid #00ff41; box-shadow: 0 0 20px #00ff41; border-radius: 5px; width: 400px; text-align: center; }
        input { width: 100%; background: transparent; border: 1px solid #333; color: #00ff41; padding: 10px; margin: 15px 0; outline: none; transition: 0.3s; }
        input:focus { border-color: #00ff41; box-shadow: 0 0 5px #00ff41; }
        button { background: #00ff41; color: #000; border: none; padding: 12px 25px; cursor: pointer; font-weight: bold; width: 100%; }
        button:hover { background: #00cc33; }
        .status { font-size: 12px; color: #555; margin-top: 10px; }
    </style>
</head>
<body>
    <div class="terminal">
        <h2>[ SECURE NODE ]</h2>
        <p>الوصول مشفر بنظام AES-256</p>
        <input type="text" placeholder="أدخل رمز التحقق (OTP)" id="otp">
        <button onclick="access()">دخول آمن</button>
        <div class="status">IP Logged: {{ ip }} | SSL: Active</div>
    </div>
    <script>
        function access() {
            alert("فشل التحقق: تم تحويل الطلب عبر بروكسي مشفر.");
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    user_ip = request.remote_addr
    return render_template_string(HTML_TEMPLATE, ip=user_ip)

# لوحة التحكم السرية (لا يمكن تخمينها)
@app.route('/' + MASTER_KEY)
def admin_panel():
    return f"<h1>أهلاً Shadow</h1><p>النظام محمي بالكامل ولا توجد اختراقات حالياً.</p>"

if __name__ == '__main__':
    print(f"--- [ الموقع يعمل بحماية Shadow ] ---")
    app.run(host='0.0.0.0', port=PORT)

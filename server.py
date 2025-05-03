from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Allowed static outbound IPs
STATIC_IPS = 100.20.92.101

# Bot Token
BOT_TOKEN = "7625835407:AAEaQKALtelHl5vysH8tCmd3Phd69jecEyo"

# Set webhook URL
WEBHOOK_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/setWebhook"

@app.before_request
def restrict_ip():
    client_ip = request.remote_addr
    if client_ip not in STATIC_IPS:
        return jsonify({"error": "Access denied from IP: {}".format(client_ip)}), 403

@app.route("/")
def index():
    return jsonify({"message": "Welcome to the Telegram Bot Webhook System!", "short_name": "Infoboy"})

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print(f"Incoming data: {data}")
    return jsonify({"message": "Webhook received!"})

@app.route("/set_webhook", methods=["GET"])
def set_webhook():
    response = requests.get(f"{WEBHOOK_URL}?url=https://<your-server-ip>/webhook")
    if response.status_code == 200:
        return jsonify({"message": "Webhook set successfully!"})
    else:
        return jsonify({"error": "Failed to set webhook", "details": response.text}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=443, ssl_context="adhoc")

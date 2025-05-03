from flask import Flask, request, jsonify

app = Flask(__name__)

# Allowed static outbound IPs
STATIC_IPS = 100.20.92.101

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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=443, ssl_context="adhoc")

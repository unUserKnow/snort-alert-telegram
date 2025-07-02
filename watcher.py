import json
import requests
import time
import os
import socket

# Cargar configuración desde config.json
with open('config.json') as f:
    config = json.load(f)

BOT_TOKEN = config['bot_token']
CHAT_ID = config['chat_id']
ALERT_LOG_PATH = config['alert_log']
TRUSTED_IP = config['trusted_ip']

# Verifica si el analista está presente según su IP
def is_analyst_present():
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return ip_address == TRUSTED_IP
    except:
        return False

# Enviar mensaje a Telegram usando el bot
def send_telegram_alert(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        response = requests.post(url, data=data)
        if response.status_code != 200:
            print("⚠️ Error al enviar mensaje:", response.text)
    except Exception as e:
        print("⚠️ Excepción al enviar mensaje:", e)

# Monitorea el archivo de alertas y detecta nuevas líneas
def monitor_alerts():
    print("📡 Monitoreando alertas de Snort...")
    last_size = 0
    while True:
        try:
            current_size = os.path.getsize(ALERT_LOG_PATH)
            if current_size > last_size:
                with open(ALERT_LOG_PATH, 'r') as f:
                    lines = f.readlines()
                    if lines:
                        new_alert = lines[-1].strip()
                        if not is_analyst_present():
                            send_telegram_alert(f"🚨 *Nueva alerta de Snort:*\n\n{new_alert}")
                        else:
                            print("🟢 Alerta ignorada (analista presente)")
                last_size = current_size
            time.sleep(5)
        except Exception as e:
            print("❌ Error en la monitorización:", e)
            time.sleep(10)

if __name__ == "__main__":
    monitor_alerts()

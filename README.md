<h1 align="center">🔔 Snort + Telegram Alert System</h1>
<p align="center"><em>Un sistema de alertas en tiempo real para detección de amenazas con Snort + Telegram</em></p>

<p align="center">
  <img src="https://img.shields.io/badge/snort-v2.x-red" />
  <img src="https://img.shields.io/badge/python-3.x-blue" />
  <img src="https://img.shields.io/badge/telegram-alerts-success" />
  <img src="https://img.shields.io/github/license/tu-usuario/snort-telegram-alert" />
</p>

---

## 🚀 ¿Qué es este proyecto?

🔍 Este proyecto permite conectar **Snort**, un IDS (Sistema de Detección de Intrusos), con **Telegram**, para recibir alertas de seguridad directamente en tu dispositivo.

Detecta eventos como:
- Escaneos de red (SYN, NULL, XMAS, UDP)
- Posibles ataques DoS
- Conexiones sospechosas

Y te avisa en tiempo real por Telegram.

---

## 📁 Estructura del Proyecto

```plaintext
snort-telegram-alert/
├── watcher.py             # Script principal que monitorea alertas
├── config.json            # Token y chat_id de Telegram
├── requirements.txt       # Librerías necesarias
├── sample_alert.log       # Archivo de muestra (opcional)
├── README.md              # Este documento
└── snort/
    └── custom.rules       # Reglas personalizadas para Snort

⚙️ Requisitos

✅ Snort instalado y funcional en Windows

✅ Python 3.x

✅ Bot de Telegram (creado aquí)

✅ chat_id obtenido desde @userinfobot

🔧 Instalación

git clone https://github.com/tu-usuario/snort-telegram-alert.git
cd snort-telegram-alert
pip install -r requirements.txt

Configura config.json con tu token y chat_id de Telegram:

{
  "telegram_token": "TU_TOKEN_AQUI",
  "chat_id": "TU_CHAT_ID_AQUI"
}

🧪 Ejecución
1. Ejecuta Snort con tus reglas:

snort.exe -i 6 -c C:\Snort\etc\snort.conf -l C:\Snort\log

2. Ejecuta el script de monitoreo:

python watcher.py

3. Lanza un escaneo desde otra máquina (Kali, por ejemplo):

nmap -sS TU_IP_OBJETIVO
Si todo está bien configurado, te llegará una alerta en Telegram como esta:

📡 [RECON] Escaneo SYN detectado
🔍 SID: 1001002
🕒 Fecha: [hora del evento]

🛡️ Reglas Ejemplo (custom.rules)

alert tcp any any -> any any (flags:S; msg:"[RECON] Escaneo SYN detectado"; sid:1001002; rev:1;)
alert udp any any -> any any (msg:"[RECON] Escaneo UDP detectado"; sid:1001004; rev:1;)

📌 Notas

El script monitorea el archivo de log generado por Snort (alert o snort.log.xxxxxxxx)
Este proyecto no requiere configuración compleja, y funciona apenas lo clones y edites el config.json.

🌟 Créditos

Desarrollado con 💻, café ☕ y obsesión por la seguridad por:

<h3 align="center"><code>0xNyx</code> 🥷</h3>
“Hablarle a la nada por primera vez... es el primer hackeo real.”

🐞 ¿Problemas?

¿No llegan alertas? Verifica que:

Estés usando reglas activas en custom.rules
Tu chat_id y token de bot sean correctos
Si todo falla, puedes abrir un issue

⭐ ¿Te gustó el proyecto?
Apóyame dejando una estrella ⭐ y compartiendo el repositorio con otros entusiastas de la ciberseguridad.
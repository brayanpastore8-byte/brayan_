from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# --- CONFIGURAZIONE WEBHOOK ---
# Crea due webhook diversi su Discord e incolla i link qui sotto
WEBHOOK_PRESTITI = "https://discord.com/api/webhooks/1475138698088812746/n4lhO3JH9X0qHlS2W3qQjcPEy6N7PM5Lil-MUrZoaEOX4hvqJSQ7AXyu0otDtOBuUpvO"
WEBHOOK_APPUNTAMENTI = "https://discord.com/api/webhooks/1475139197235892365/fFk96bHCXFm2qOPKIw3T2pQLQ18wKy8CeWmDlQU-52CkKSXceu58QFq5U_lzvqnIo3Gs"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/invia_prestito', methods=['POST'])
def invia_prestito():
    data = request.form
    messaggio = {
        "embeds": [{
            "title": "💰 NUOVA RICHIESTA PRESTITO",
            "color": 3066993,
            "fields": [
                {"name": "🆔 Discord", "value": data['nome_discord'], "inline": True},
                {"name": "👤 Nome RP", "value": f"{data['nome_rp']} {data['cognome_rp']}", "inline": True},
                {"name": "💼 Lavoro", "value": f"{data['lavoro']} (${data['guadagno']})", "inline": False},
                {"name": "💵 Importo", "value": f"${data['cifra']}", "inline": True},
                {"name": "📝 Motivo", "value": data['motivo'], "inline": True}
            ]
        }]
    }
    requests.post(WEBHOOK_PRESTITI, json=messaggio)
    return "SUCCESS_PRESTITO"

@app.route('/invia_appuntamento', methods=['POST'])
def invia_appuntamento():
    data = request.form
    messaggio = {
        "embeds": [{
            "title": "📅 NUOVO APPUNTAMENTO",
            "color": 15105570,
            "fields": [
                {"name": "🆔 Discord", "value": data['nome_discord'], "inline": True},
                {"name": "👤 Soggetto RP", "value": f"{data['nome_rp']} {data['cognome_rp']}", "inline": True},
                {"name": "⏰ Orario Scelto", "value": f"{data['orario']}:00", "inline": False}
            ]
        }]
    }
    requests.post(WEBHOOK_APPUNTAMENTI, json=messaggio)
    return "SUCCESS_APPUNTAMENTO"

if __name__ == '__main__':
    app.run(debug=True)
    
import os
from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Clé secrète pour la session (pas besoin de variable d'env pour la démo)
app.secret_key = "demo_key_portfolio"

# --- ROUTES ---

@app.route('/login', methods=['GET', 'POST'])
def login():
    # DÉMO : On accepte n'importe quel mot de passe !
    if request.method == 'POST':
        session['user_id'] = 1 # On simule un utilisateur connecté
        session['username'] = "Visiteur"
        return redirect(url_for('index'))
    
    return render_template('login.html', demo_mode=True)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/')
def index():
    # Protection simple : si pas connecté, on renvoie au login
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('index.html')

@app.route('/api/save_match', methods=['POST'])
def save_match():
    # DÉMO : On reçoit les données, on les affiche dans la console du serveur,
    # mais on ne les sauvegarde nulle part.
    data = request.json
    print(f"--- [DEMO] Données reçues ---")
    print(f"Match: {data.get('homeName')} vs {data.get('awayName')}")
    print(f"Vainqueur: {data.get('winner')}")
    print(f"Nombre de points: {len(data.get('history', []))}")
    
    # On fait semblant que tout s'est bien passé
    return jsonify({
        "status": "success", 
        "message": "Mode DÉMO : Simulation d'envoi réussie ! (Aucune donnée enregistrée)"
    })

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stock.db'
db = SQLAlchemy(app)

class Produit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100))
    quantite = db.Column(db.Integer)
    prix_unitaire = db.Column(db.Float)

@app.route('/produits', methods=['GET'])
def get_produits():
    produits = Produit.query.all()
    return jsonify([{"id": p.id, "nom": p.nom, "quantite": p.quantite, "prix": p.prix_unitaire} for p in produits])

@app.route('/update_stock', methods=['POST'])
def update_stock():
    data = request.json
    produit = Produit.query.get(data['id'])
    produit.quantite -= data['quantite']
    db.session.commit()
    return jsonify({"message": "Stock mis à jour"})

if __name__ == '__main__':
    # 🟢 إنشاء الجداول داخل سياق التطبيق
    with app.app_context():
        db.create_all()
    
    app.run(host='0.0.0.0', port=5001)

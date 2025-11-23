from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# J'initialise mon application Flask
app = Flask(__name__)

# --- MA CONFIGURATION MYSQL ---
# Je me connecte à la même base de données que celle utilisée dans la partie Spring.
# Note : Je dois penser à vérifier mon mot de passe root ici (par défaut 'root').
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost/db_etudiants'
# Je désactive le tracking des modifications pour économiser des ressources
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# J'initialise l'outil de gestion de BDD (ORM)
db = SQLAlchemy(app)

# --- MON MODÈLE DE DONNÉES ---
# Je définis la structure de ma table Etudiant.
# C'est l'équivalent exact de mon Entité Java annotée avec @Entity.
class Etudiant(db.Model):
    __tablename__ = 'etudiant'
    
    # Je reproduis les mêmes colonnes que dans mon TP Java
    identifiant = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom = db.Column(db.String(100), nullable=False)
    moyenne = db.Column(db.Float, nullable=False)

    # Mon constructeur pour créer facilement un nouvel étudiant
    def __init__(self, nom, moyenne):
        self.nom = nom
        self.moyenne = moyenne

    # Méthode utilitaire : Flask ne convertit pas automatiquement les objets en JSON comme Spring.
    # Je dois donc le faire manuellement ici.
    def to_json(self):
        return {
            'identifiant': self.identifiant,
            'nom': self.nom,
            'moyenne': self.moyenne
        }

# --- MES ROUTES (L'équivalent de mon Controller Java) ---

# 1. Route pour récupérer toute la liste (GET)
@app.route('/etudiants', methods=['GET'])
def get_all_etudiants():
    # Je fais une requête 'SELECT *' via SQLAlchemy
    liste_etudiants = Etudiant.query.all()
    
    # Je transforme ma liste d'objets en liste JSON pour le client
    return jsonify([e.to_json() for e in liste_etudiants])

# 2. Route pour récupérer un seul étudiant via son ID (GET)
@app.route('/etudiants/<int:identifiant>', methods=['GET'])
def get_etudiant(identifiant):
    # Je cherche l'étudiant par sa clé primaire
    etudiant = Etudiant.query.get(identifiant)
    
    if etudiant:
        return jsonify(etudiant.to_json())
    return jsonify({'message': 'Etudiant introuvable'}), 404

# 3. Route pour ajouter un étudiant (POST)
@app.route('/etudiants', methods=['POST'])
def add_etudiant():
    # Je récupère les données envoyées dans le corps de la requête (le JSON)
    data = request.get_json()
    
    # Je crée une nouvelle instance de ma classe Etudiant
    nouvel_etudiant = Etudiant(nom=data['nom'], moyenne=data['moyenne'])
    
    # Je l'ajoute à la session et je valide la transaction (commit)
    db.session.add(nouvel_etudiant)
    db.session.commit()
    
    return jsonify(nouvel_etudiant.to_json()), 201

# 4. Route pour modifier un étudiant existant (PUT)
@app.route('/etudiants/<int:identifiant>', methods=['PUT'])
def update_etudiant(identifiant):
    # D'abord, je vérifie que l'étudiant existe
    etudiant = Etudiant.query.get(identifiant)
    if not etudiant:
        return jsonify({'message': 'Etudiant introuvable'}), 404
    
    data = request.get_json()
    
    # Je mets à jour les champs seulement s'ils sont présents dans la requête
    if 'nom' in data:
        etudiant.nom = data['nom']
    if 'moyenne' in data:
        etudiant.moyenne = data['moyenne']
        
    # Je sauvegarde les modifications en base
    db.session.commit()
    return jsonify(etudiant.to_json())

# 5. Route pour supprimer un étudiant (DELETE)
@app.route('/etudiants/<int:identifiant>', methods=['DELETE'])
def delete_etudiant(identifiant):
    etudiant = Etudiant.query.get(identifiant)
    if not etudiant:
        return jsonify({'message': 'Impossible de supprimer : étudiant introuvable'}), 404
        
    # Je supprime l'objet et je valide
    db.session.delete(etudiant)
    db.session.commit()
    return jsonify({'message': 'Etudiant supprimé avec succès'})

# --- LANCEMENT DE L'APPLICATION ---
if __name__ == '__main__':
    # Au démarrage, je m'assure que la table existe dans MySQL
    with app.app_context():
        db.create_all()
        print("Démarrage de l'API Python : Connexion BDD OK.")
        
    # Je lance le serveur Flask en mode debug pour voir les erreurs
    app.run(debug=True, port=5000)

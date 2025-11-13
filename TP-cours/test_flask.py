
from flask import Flask, jsonify, request, render_template

#créer l'application flask
app=Flask(__name__)
# Dans un premier temps je ne vais pas utiliser de bases de données
# Sauvergarder les étudiants dans une liste... 

students = [
    {"id":0, "prenom":"Samir", "age":31},
    {"id":1, "prenom":"Safa", "age":22}
]

#Definir la racine de l'API
@app.route('/')
def home():
    return render_template("index.html") #pour rendre une page toute faite au lieu d'une ligne

#Methode GET pour la liste des etudiants
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

#Methode GET pour un étudiant en particulier
@app.get('/students/<int:ident>')
def get_student(ident):
    # Trouver le bon etudiant avec le bon ID (ident)
    for student in students:
        if student["id"] == ident:
            return jsonify(student)
    # Si on ne trouve pas, on renvoie 404
    return jsonify({"error": "Student not found"}), 404

#une methode POST
@app.post('/students')
def add_student():
    new_student = request.get_json() #récuperer l'objet
    new_student['id']=len(students) #assigne un ID automatique
    students.append(new_student)
    return jsonify(new_student), 201

# PUT modifier un étudiant existant
@app.put("/students/<int:ident>")
def update_student(ident):
    for student in students:
        if student["id"] == ident:
            data = request.get_json()  # Récupère les nouvelles données
            student.update(data)       # Met à jour les champs existants
            return jsonify(student)
    # Si aucun étudiant trouvé
    return jsonify({"erreur": "Étudiant introuvable"}), 404

#DELETE : supprimer un étudiant
@app.delete("/students/<int:ident>")
def delete_student(ident):
    for student in students:
        if student["id"] == ident:
            students.remove(student)   # Supprime l'étudiant de la liste
            return jsonify({"message": "Étudiant supprimé"})
    # Si aucun étudiant trouvé
    return jsonify({"erreur": "Étudiant introuvable"}), 404

if __name__ == '__main__':
    app.run(debug=True)
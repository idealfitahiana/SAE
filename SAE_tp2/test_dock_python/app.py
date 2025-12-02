from flask import Flask, jsonify, request

#Creer une appli flask 
app = Flask(__name__)
#Dans un prmeier temps je ne vais pas utiliser de bdd
#Sauvegarder les etudiants dans une liste 

students = [
        {"id":1, "prenom":"Samir", "age":31},
        {"id":2, "prenom":"Safa", "age":22},
]

@app.route('/')
def home():
    return "C'est cool Rest !! "

@app.route('/message')
def message():
    return "<h1>Bonjour tout le monde !"

# Ajouter un etudiant, c'est une nouvelle ressource.... POST....
@app.route('/students', methods=['POST'])
def add_student():
    new_student = request.get_json # recuperer l'objet
    new_student['id'] = len(students)+1 # Assigner un ID automatique
    students.append(new_student)
    return jsonify(new_student), 201


# Mise a jour d'un étudiant....
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id) :
    student = next((s for s in students if s['id']==id), None)
    if not student:
        return jsonify({"erreur": "not exist"}), 404
    
    data = request.get_json()
    student.update(data)
    return jsonify(student)

#Affichier un etudiant sachant son id
def get_student(id):
    student = next((s for s in students if s['id']==id), None)
    if student:
        return jsonify(student)
    return jsonify({"erreur" : "L'étudiant n'est pas trouvé"}), 404

def delete_student(id):
    global students
    students = [s for s in students if s['id'] != id]
    return jsonify({"message" : "Ok"}), 200
    
#Cette methode permet de lire 
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)


if __name__=='__main__':
    app.run(host='0.0.0.0', port=80, debug=True)


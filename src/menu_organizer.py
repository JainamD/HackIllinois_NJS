from db import db
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Create a connection to the SQLite database
conn = sqlite3.connect('potential_sidequests.db')

# Define a route that creates a new user
# @app.route('/print', methods=['POST'])
# def test_connect():
#     f = open("temp", "w")
#     f.close()
#     return jsonify("")



# Define a route that creates a new user
@app.route('/register', methods=['POST'])
def create_user():
    #f = open("temp", "w")
    #f.write("Successful test connection!\n")

    if request.method == 'POST':
        user = request.json['user']
        #f.write("got here!\n")

        conn = sqlite3.connect('potential_sidequests.db')
        cursor = conn.cursor()
        s = "INSERT INTO users VALUES ('{}')".format(user) 
        cursor.execute(s)
        conn.commit()
        conn.close()
        #f.write("also got here!\n")
        #f.close()
        
        user = {'user': user}
        return jsonify(user)
    
    # Define a route that creates a new user
@app.route('/login', methods=['POST'])
def login_user():
    #f = open("temp", "w")
    #f.write("Successful test connection!\n")

    if request.method == 'POST':
        user = request.json['user']

        conn = sqlite3.connect('potential_sidequests.db')
        cursor = conn.cursor()
        s = "SELECT COUNT(*) FROM users WHERE name = '{}'".format(user) 
        cursor.execute(s)
        count = cursor.fetchone()[0]
        print(count)
        ret = ""
        if count == 0:
            ret = "USERNAME NOT VALID OR ENTERED INCORRECTLY"
        else:
            ret = "USERNAME IS VALID, LOGGING IN NOW!"
        conn.commit()
        conn.close()
        
        ret_value = {'prompt': ret}
        return jsonify(ret_value)

<<<<<<< Updated upstream
@app.route('/add_quest', methods=['POST'])
def login_user():
=======
@app.route('/add', methods=['POST'])
def add_quest():
>>>>>>> Stashed changes
    #f = open("temp", "w")
    #f.write("Successful test connection!\n")

    if request.method == 'POST':
        name = request.json['name']
        desc = request.json['desc']
        happy = request.json['happy']
        sad = request.json['sad']
        tired = request.json['tired']
        motv = request.json['motv']
        bored = request.json['bored']
        hungy = request.json['hungy']
        mins = request.json['mins']
        finish = request.json['finish']
        user = request.json['user']
        #f.write("got here!\n")

        inst = db()
        inst.add_quest(name, desc, happy, sad, tired, motv, bored, hungy, mins, "0" ,user)
        ret = {'name': name}
        return jsonify(ret)
    
@app.route('/get_random_quest', methods=['GET'])
def add_quest():
    #f = open("temp", "w")
    #f.write("Successful test connection!\n")

    if request.method == 'GET':
        user = request.json['user']
        inst = db(user)
        rand = inst.get_random_quest()
        ret = {'name': rand[1], 'desc': rand[2], 'happy': rand[3], 'sad': rand[4], 'tired': rand[5], 'motv': rand[6], 'bored': rand[7], 'hungy': rand[8], 'time': rand[9], 'finished': rand[10], 'user': rand[11]}
        return jsonify(ret)
'''
# Update an existing db
@app.route('/dbs/<string:name>', methods=['PUT'])
def update_db(name):
    cur = conn.execute('SELECT name FROM dbs WHERE name = ?', (name,))
    db = [{'name': row[0]} for row in cur.fetchall()]
    if len(db) == 0:
        return jsonify({'error': 'DB not found'}), 404
    new_name = request.json['name']
    conn.execute('UPDATE dbs SET name = ? WHERE name = ?', (new_name, name))
    conn.commit()
    db[0]['name'] = new_name
    return jsonify({'db': db[0]})

# Delete a db
@app.route('/dbs/<string:name>', methods=['DELETE'])
def delete_db(name):
    cur = conn.execute('SELECT name FROM dbs WHERE name = ?', (name,))
    db = [{'name': row[0]} for row in cur.fetchall()]
    if len(db) == 0:
        return jsonify({'error': 'DB not found'}), 404
    conn.execute('DELETE FROM dbs WHERE name = ?', (name,))
    conn.commit()
    return jsonify({'result': True})

# Get all dbs
@app.route('/dbs', methods=['GET'])
def get_dbs():
    cur = conn.execute('SELECT name FROM dbs')
    dbs = [{'name': row[0]} for row in cur.fetchall()]
    return jsonify({'dbs': dbs})

# Get a specific db by name
@app.route('/dbs/<string:name>', methods=['GET'])
def get_db(name):
    cur = conn.execute('SELECT name FROM dbs WHERE name = ?', (name,))
    db = [{'name': row[0]} for row in cur.fetchall()]
    if len(db) == 0:
        return jsonify({'error': 'DB not found'}), 404
    return jsonify({'db': db[0]})
'''




# Close the connection to the database
conn.close()

if __name__ == '__main__':
    app.run(host="localhost", port=8081, debug=True)

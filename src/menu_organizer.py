from db import db
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Create a connection to the SQLite database
conn = sqlite3.connect('example.db')


# Define a route that creates a new user
@app.route('/register', methods=['POST'])
def create_user():
    if request.method == 'POST':
        user = request.json['user']
        new_user = db()
        conn = sqlite3.connect('potential_sidequests.db')
        cursor = conn.cursor()
        s = "INSERT INTO users VALUES ('{}')".format(user) 
        cursor.execute(s)
        con.commit()
        con.close()
        
        user = {'user': user}
        return jsonify(user)

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
    app.run()

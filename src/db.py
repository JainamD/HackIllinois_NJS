import sqlite3

# class that represents the data you want to expose through the AP
class db:
    def __init__(self):
        pass

    # Create Table Method (Only excecute to create a fresh table)
    def create_tables(self):
        # if table exists, replaces it
        conn = sqlite3.connect('potential_sidequests.db')
        cursor = conn.cursor()
        s = "DROP TABLE IF EXISTS sidequests"
        cursor.execute(s)
        s = "DROP TABLE IF EXISTS users"
        cursor.execute(s)
        
        # Create a table with the desired columns of TABLE not DATABASE(this is for you nishka)
        s = 'CREATE TABLE sidequests'
        s += '''(id INTEGER PRIMARY KEY,
                    Name TEXT NOT NULL,
                    Description TEXT NOT NULL,
                    Happy INT NOT NULL,
                    Sad INT NOT NULL,
                    Tired INT NOT NULL,
                    Motivated INT NOT NULL,
                    Bored INT NOT NULL,
                    Hungry INT NOT NULL,
                    Minutes INT NOT NULL,
                    Finished INT NOT NULL,
                    Username TEXT NOT NULL);'''
        conn.execute(s)
        s = 'CREATE TABLE users (name TEXT PRIMARY KEY)'
        conn.execute(s)

        # Commit changes and close the connection
        conn.commit()
        conn.close()

    # Add Side Quest
    def add_quest(self, N, D, Ha, S, T, M, B, Hn, Mins, Fin, user):
        conn = sqlite3.connect('potential_sidequests.db')

        # Check Name is not taken
        cursor = conn.cursor()
        s = 'SELECT COUNT(*) FROM sidequests WHERE Name = {} AND Username = {}'.format(N, user)
        cursor.execute(s)
        count = cursor.fetchone()[0]

        if count != 0:
            conn.close()
            #print('NAME TAKEN BISH')
            return('Name taken')

        # Insert data into the table
        s = 'INSERT INTO sidequests (Name, Description, Happy, Sad, Tired, Motivated, Bored, Hungry, Minutes, Finished, Username) '
        s += 'VALUES ({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {})'.format(N, D, Ha, S, T, M, B, Hn, Mins, Fin, user)
        conn.execute(s)

        # Commit changes and close the connection
        conn.commit()
        conn.close()

    # Update Side Quest
    def update_quest(self, N, col, update, user):
        conn = sqlite3.connect('potential_sidequests.db')

        # Update a row in THE table
        s = 'UPDATE sidequests SET {} = {} WHERE Name = {} AND Username = {}'.format(col, update, N, user)
        conn.execute(s)

        # Commit changes and close the connection
        conn.commit()
        conn.close()


    # Delete Side Quest (For testing purposes, user will NOT have this functionality)
    # delete a command given name
    def delete_quest_name(self, N, user):    
        conn = sqlite3.connect('potential_sidequests.db')

        # Delete based on Name
        s = 'DELETE FROM sidequests WHERE Name = "{}" AND Username = {}'.format(N, user)
        conn.execute(s)
        
        # Commit changes and close the connection
        conn.commit()
        conn.close()

    # Delete any command higher than given duration
    def delete_quest_duration(self, D, user):
        conn = sqlite3.connect('potential_sidequests.db')

        # Delete based on Duration
        s = 'DELETE FROM sidequests WHERE Minutes >= {} AND Username = {}'.format(D, user)
        conn.execute(s)

        c# Commit changes and close the connection
        conn.commit()
        conn.close()

    # Search SideQuest (Return randomly based on mood grouping)
    def search_quests_mood(self, M, user):
        conn = sqlite3.connect('potential_sidequests.db')

        # get all the rows where mood is true
        cursor = conn.cursor()
        s = "SELECT * FROM sidequests WHERE {} = 1 AND Username = {}".format(M, user)
        cursor.execute(s)

        rows = cursor.fetchall()
        
        # Commit changes and close the connection
        conn.commit()
        conn.close()
        return(rows)

    # Search SideQuest (Return randomly based on time duration grouping)
    # maybe in a range??
    def search_quests_time(self, D, user):
        conn = sqlite3.connect('potential_sidequests.db')

        # get all the rows where mood is true
        cursor = conn.cursor()
        s = "SELECT * FROM sidequests WHERE Minutes <= {} AND Username = {}".format(D, user)
        cursor.execute(s)

        rows = cursor.fetchall()
        
        # Commit changes and close the connection
        conn.commit()
        conn.close()
        return(rows)





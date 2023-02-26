import sqlite3

# class that represents the data you want to expose through the AP
class db:
    def __init__(self, name):
        self.name = name

    # Create Table Method (Only excecute to create a fresh table)
    def create_table(self):
        # if table exists, replaces it
        conn = sqlite3.connect('potential_sidequests.db')
        cursor = conn.cursor()
        s = "DROP TABLE IF EXISTS sidequests_{}".format(self.name)
        cursor.execute(s)

        # Create a table with the desired columns of TABLE not DATABASE(this is for you nishka)
        s = 'CREATE TABLE sidequests_{}'.format(self.name)
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
                    Finished INT NOT NULL);'''
        conn.execute(s)

        # Commit changes and close the connection
        conn.commit()
        conn.close()

    # Add Side Quest
    def add_quest(self, N, D, Ha, S, T, M, B, Hn, Mins, Fin):
        conn = sqlite3.connect('potential_sidequests.db')

        # Check Name is not taken
        cursor = conn.cursor()
        s = 'SELECT COUNT(*) FROM sidequests_{} WHERE Name = {}'.format(self.name, N)
        cursor.execute(s)
        count = cursor.fetchone()[0]

        if count != 0:
            conn.close()
            print('NAME TAKEN BISH')
            return('Name taken')

        # Insert data into the table
        s = 'INSERT INTO sidequests_{}'.format(self.name)
        s += ' (Name, Description, Happy, Sad, Tired, Motivated, Bored, Hungry, Minutes, Finished) '
        s += "VALUES ({}, {}, {}, {}, {}, {}, {}, {}, {}, {})".format(N, D, Ha, S, T, M, B, Hn, Mins, Fin)
        conn.execute(s)

        # Commit changes and close the connection
        conn.commit()
        conn.close()

    # update quest
    
    def update_quest(self, N, col, update):
        conn = sqlite3.connect('potential_sidequests.db')

        # Update a row in a table
        s = 'UPDATE sidequests_{} SET {} = {} WHERE Name = {}'.format(self.name, col, update, N)
        conn.execute(s)

        # Commit changes and close the connection
        conn.commit()
        conn.close()


    # Delete Side Quest (For testing purposes, user will NOT have this functionality)
    # delete a command given name
    def delete_quest_name(self, N):    
        conn = sqlite3.connect('potential_sidequests.db')

        # Delete based on Name
        s = 'DELETE FROM sidequests_{} WHERE Name = "{}"'.format(self.name, N)
        conn.execute(s)
        
        # Commit changes and close the connection
        conn.commit()
        conn.close()

    # Delete any command higher than given duration
    def delete_quest_duration(self, D):
        conn = sqlite3.connect('potential_sidequests.db')

        # Delete based on Duration
        s = 'DELETE FROM sidequests_{} WHERE Minutes >= {}'.format(self.name, D)
        conn.execute(s)

        c# Commit changes and close the connection
        conn.commit()
        conn.close()

    # Search SideQuest (Return randomly based on mood grouping)
    def search_quests_mood(self, M):
        conn = sqlite3.connect('potential_sidequests.db')

        # get all the rows where mood is true
        cursor = conn.cursor()
        s = "SELECT * FROM sidequests_{} WHERE {} = 1".format(self.name, M)
        cursor.execute(s)

        rows = cursor.fetchall()
        
        # Commit changes and close the connection
        conn.commit()
        conn.close()
        return(rows)

    # Search SideQuest (Return randomly based on time duration grouping)
    # maybe in a range??
    def search_quests_time(self, D):
        conn = sqlite3.connect('potential_sidequests.db')

        # get all the rows where mood is true
        cursor = conn.cursor()
        s = "SELECT * FROM sidequests_{} WHERE Minutes <= {}".format(self.name, D)
        cursor.execute(s)

        rows = cursor.fetchall()
        
        # Commit changes and close the connection
        conn.commit()
        conn.close()
        return(rows)




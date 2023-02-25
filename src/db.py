import sqlite3
class db:
    def __init__(self):
        self.conn = sqlite3.connect('potential_sidequests.db')

    # Create Table Method (Only excecute to create a fresh table)
    def create_table(self):
        # if table exists, replaces it
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS sidequests")

        # Create a table with the desired columns of TABLE not DATABASE(this is for you nishka)
        conn.execute('''CREATE TABLE sidequests
                    (id INTEGER PRIMARY KEY,
                    Name TEXT NOT NULL,
                    Description TEXT NOT NULL,
                    Happy INT NOT NULL,
                    Sad INT NOT NULL,
                    Tired INT NOT NULL,
                    Motivated INT NOT NULL,
                    Bored INT NOT NULL,
                    Hungry INT NOT NULL,
                    Minutes INT NOT NULL,
                    Finished INT NOT NULL);''')

        # Commit changes and close the connection
        conn.commit()
        conn.close()

    # Add Side Quest
    def add_quest(self, N, D, Ha, S, T, M, B, Hn, Mins, Fin):
        conn = sqlite3.connect('potential_sidequests.db')

        # Check Name is not taken
        cursor = conn.cursor()
        s = 'SELECT COUNT(*) FROM sidequests WHERE Name = {}'.format(N)
        cursor.execute(s)
        count = cursor.fetchone()[0]

        if count != 0:
            conn.close()
            print('NAME TAKEN BISH')
            return('Name taken')

        # Insert data into the table
        s = 'INSERT INTO sidequests (Name, Description, Happy, Sad, Tired, Motivated, Bored, Hungry, Minutes, Finished) '
        s += "VALUES ({}, {}, {}, {}, {}, {}, {}, {}, {}, {})".format(N, D, Ha, S, T, M, B, Hn, Mins, Fin)
        conn.execute(s)

        # Commit changes and close the connection
        conn.commit()
        conn.close()

    # update quest
    def update_quest(self, N, col, update):
        conn = sqlite3.connect('potential_sidequests.db')

        #
        s = 'SELECT * FROM sidequests WHERE Name = {}'.format(N)




    # Delete Side Quest (For testing purposes, user will NOT have this functionality)
    # delete a command given name
    def delete_quest_name(self, N):    
        conn = sqlite3.connect('potential_sidequests.db')

        # Delete based on Name
        s = 'DELETE FROM sidequests WHERE Name = "{}"'.format(N)
        conn.execute(s)
        #print('yea u got here')
        conn.commit()
        conn.close()

    # Delete any command higher than given duration
    def delete_quest_duration(self, D):
        conn = sqlite3.connect('potential_sidequests.db')

        # Delete based on Duration
        s = 'DELETE FROM sidequests WHERE Minutes >= {}'.format(D)
        conn.execute(s)

        conn.commit()
        conn.close()

    # Search SideQuest (Return randomly based on mood grouping)
    def search_quests_mood(self, M):
        conn = sqlite3.connect('potential_sidequests.db')

        # get all the rows where mood is true
        cursor = conn.cursor()
        s = "SELECT * FROM sidequests WHERE {} = 1".format(M)
        cursor.execute(s)

        rows = cursor.fetchall()
        
        conn.commit()
        conn.close()
        return(rows)

    # Search SideQuest (Return randomly based on time duration grouping)
    # maybe in a range??
    def search_quests_time(self, D):
        conn = sqlite3.connect('potential_sidequests.db')

        # get all the rows where mood is true
        cursor = conn.cursor()
        s = "SELECT * FROM sidequests WHERE D <= {}".format(D)
        cursor.execute(s)

        rows = cursor.fetchall()
        
        conn.commit()
        conn.close()
        return(rows)


    # RUNNING STUFF
    create_table()

    add_quest('"Clean Closet"', '"Organize everything in my closet"', 0, 0, 0, 1, 1, 0, 40, 0)
    add_quest('"Make a Dessert"', '"Find a recipe online on youtube and make it"', 1, 1, 0, 1, 1, 1, 20, 0)
    add_quest('"Call my friends"', '"Reach out to my highschool friends"', 1, 1, 1, 0, 1, 0, 60, 0)
    add_quest('"Go to Taco Bell"', '"Get food so J does not kill me"', 0, 0, 0, 0, 0, 1, 45, 0)


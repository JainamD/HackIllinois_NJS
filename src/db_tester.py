from db import db
'''
This class is meant for running tests for instances made for db
, and will also help to trouble shoot any problems in working code
'''

person = db() 
person.create_tables()
person.add_quest('"Clean Closet"', '"Organize everything in my closet"', 0, 0, 0, 1, 1, 0, 40, 0, '"Jainam"')
person.add_quest('"Make a Dessert"', '"Find a recipe online on youtube and make it"', 1, 1, 0, 1, 1, 1, 20, 0, '"Jainam"')
person.add_quest('"Call my friends"', '"Reach out to my highschool friends"', 1, 1, 1, 0, 1, 0, 60, 0, '"Nishka"')
person.add_quest('"Go to Taco Bell"', '"Get food so J does not kill me"', 0, 0, 0, 0, 0, 1, 45, 0, '"Nishka"')


print(person.delete_quest_name('"Clean Closet"', '"Jainam"'))

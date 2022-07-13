from mongoimpl import database
import data_agg

db = database().get_database('disc-check')
users = db["users"]


def get_users():
    retval = users.find({})
    return list(retval)

def run():
    add_user()
    objs = data_agg.get_records()
    users = get_users()
    print("Current users: ")
    for u in users:
        print(u)
    for obj in obj:
        if obj.name

def add_user(rec = False):
    if not rec:
        add = input("Would you like to add a user? ")
    if rec or add.lower() == "y":
        name = input("Name: ")
        email = input("Email: ")
        newuser = {"Name": name, "Email": email}
        users.insert_one(newuser)
        print("User added.")
        cont = input("Add another? ")
        if cont.lower() == 'y':
            add_user(True)
        else:
            return
        

    #for obj in objs:
       # print(obj.name)
    

count = 0
while count < 1:
    run()
    count += 1



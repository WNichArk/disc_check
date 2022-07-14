from collections import UserList
from mongoimpl import database
import data_agg
from match import Match
from munch import DefaultMunch

db = database().get_database('disc-check')
dbusers = db["users"]


def get_users():
    retval = dbusers.find({})
    return list(retval)

def run():
    add_user()
    records = data_agg.get_records()
    users = get_users()
    found = []
    for u in users:
        u = DefaultMunch.fromDict(u)
        addl = [r for r in records if r.name.lower() == u["Name"].lower()]
        if any(addl):
            for a in addl:
                found.append(Match(u, a))
    for f in found:
        print(f'Found: {f.user.Name} {f.user.Email} Disc: {f.record.color.strip()} {f.record.disc.strip()}')

def add_user(rec = False):
    if not rec:
        add = input("Would you like to add a user? ")
        print()
    if rec or add.lower() == "y":
        name = input("Name: ")
        email = input("Email: ")
        newuser = {"Name": name, "Email": email}
        dbusers.insert_one(newuser)
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



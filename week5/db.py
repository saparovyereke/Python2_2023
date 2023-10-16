import re

with open('database.txt', 'r') as f: 
    lines = f.readlines() 
    db = {} 
    for line in lines: 
        key, value = line.strip().split(', ') 
        db[key] = value
f.close()

def show_db():
    print(db)

def change_name(old_name, new_name, password):
    while password != db[old_name]:
        password = input('Wrong password! Try again: ')
    
    db[new_name] = db[old_name]
    del db[old_name]
    
def add_user(name, password):
    while name in db.keys():
        name = input('Plz choose another name: ')
    if check_password(password) == True:
        db[name] = password

def check_password(password):
    count = 0
    #[A-Z], [a-z], @#$%^%, len >6, [0-9]
    while count != 2:
        if re.search('[a-zA-Z]', password) and re.search('[@#$%^]', password) and re.search('[0-9]', password) and len(password) > 6:
            break
        else:
            count+=1
            password = input()
    return True

def change_pass(name, new_pass, password):
    while password != db[name]:
        password = input('Wrong password! Try again: ')
    if check_password(new_pass):
        db.update({name: new_pass})

print("Welcome to the users database!")
action = input("What would you like to do? show db/add User/change Name/...")

if action == 'show db':
    show_db()
elif action == 'add User':

    name = input('Enter name: ')
    password = input('enter password: ')
    add_user(name , password)
elif action == 'change Name':

    old_name = input("Enter name: ")
    new_name = input('Enter new name: ')
    password = input('Enter password: ')
    change_name(old_name, new_name, password)
elif action == 'change Password':

    name = input('Enter username: ')
    new_pass = input('Enter new password: ')
    password = input('Enter password: ')
    change_pass(name, new_pass, password)

with open('database.txt', 'w') as f:
    for item in db:
        line = item + ", " +db[item] +"\n"
        f.write(line)
f.close()
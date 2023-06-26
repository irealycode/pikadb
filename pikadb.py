from hashlib import md5
import json
import os
from pathlib import Path
from colorama import Fore, Back, Style
import readline
import random
from cryptography.fernet import Fernet
import base64
from sys import argv

db = ""
db_user = "public"
db_pass = "4c9184f37cff01bcdc32dc486ec36961"
banner = [f""" {Fore.GREEN}

          /  |/  |                      /  |/  |      
  ______  $$/ $$ |   __   ______    ____$$ |$$ |____  
 /      \ /  |$$ |  /  | /      \  /    $$ |$$      \ 
/$$$$$$  |$$ |$$ |_/$$/  $$$$$$  |/$$$$$$$ |$$$$$$$  |
$$ |  $$ |$$ |$$   $$<   /    $$ |$$ |  $$ |$$ |  $$ |
$$ |__$$ |$$ |$$$$$$  \ /$$$$$$$ |$$ \__$$ |$$ |__$$ |
$$    $$/ $$ |$$ | $$  |$$    $$ |$$    $$ |$$    $$/ 
$$$$$$$/  $$/ $$/   $$/  $$$$$$$/  $$$$$$$/ $$$$$$$/  
$$ |                                                  
$$ |                {Fore.RESET}pikadb v1.1 {Fore.GREEN}                           
$$/             {Fore.RESET}made by : {Fore.YELLOW + 'irealycode'+ Fore.RESET}    
            https://github.com/irealycode
""",f""" {Fore.RED}
                                    
              )         (        )  
       (   ( /(     )   )\ )  ( /(  
 `  )  )\  )\()) ( /(  (()/(  )\()) 
 /(/( ((_)((_)\  )(_))  ((_))((_)\  
((_)_\ (_)| |(_)((_)_   _| | | |(_) 
| '_ \)| || / / / _` |/ _` | | '_ \ 
| .__/ |_||_\_\ \__,_|\__,_| |_.__/ 
|_|                                 
{Fore.RESET}
                pikadb v1.1                                                                                   
            made by : {Fore.YELLOW + 'irealycode'+ Fore.RESET}
        https://github.com/irealycode                                     

""",f""" {Fore.WHITE}

 ██▓███   ██▓ ██ ▄█▀▄▄▄      ▓█████▄  ▄▄▄▄   
▓██░  ██▒▓██▒ ██▄█▒▒████▄    ▒██▀ ██▌▓█████▄ 
▓██░ ██▓▒▒██▒▓███▄░▒██  ▀█▄  ░██   █▌▒██▒ ▄██
▒██▄█▓▒ ▒░██░▓██ █▄░██▄▄▄▄██ ░▓█▄   ▌▒██░█▀  
▒██▒ ░  ░░██░▒██▒ █▄▓█   ▓██▒░▒████▓ ░▓█  ▀█▓
▒▓▒░ ░  ░░▓  ▒ ▒▒ ▓▒▒▒   ▓▒█░ ▒▒▓  ▒ ░▒▓███▀▒
░▒ ░      ▒ ░░ ░▒ ▒░ ▒   ▒▒ ░ ░ ▒  ▒ ▒░▒   ░ 
░░        ▒ ░░ ░░ ░  ░   ▒    ░ ░  ░  ░    ░ 
          ░  ░  ░        ░  ░   ░     ░      
                              ░            ░ 
                {Fore.RESET}pikadb v1.1                                                                                   
            made by : {Fore.YELLOW + 'irealycode'+ Fore.RESET}
        https://github.com/irealycode 

"""]


class PikaDB:
    def get_doc(table,doc):
        #checks if doc exists and gets data
        ret = {}
        try:
            k= base64.urlsafe_b64encode(db_pass.encode())
            fr= Fernet(k)
            db_read = open(f'{Path.home()}/.dbs/{db}/{table}/{doc}', 'r')
            f = db_read.read()
            db_read.close()
            f = fr.decrypt(f.encode()).decode()
            ret = json.loads(f)
        except:
            ret = 'none'
        return ret

    def update_doc(table,doc,data):
        #update or add items to doc
        ret = {}
        try:
            k= base64.urlsafe_b64encode(db_pass.encode())
            fr= Fernet(k)
            db_read = open(f'{Path.home()}/.dbs/{db}/{table}/{doc}', 'r')
            f = db_read.read()
            db_read.close()
            f = fr.decrypt(f.encode()).decode()
            z = json.loads(f)
            lst = list(data.keys())
            for i in range(len(lst)):
                z[lst[i]] = data[lst[i]]
            db_write = open(f'{Path.home()}/.dbs/{db}/{table}/{doc}', 'w')
            t = fr.encrypt(json.dumps(z).encode()).decode()
            db_write.write(t)
            ret = 'updated'
        except:
            ret = 'none'
        return ret

    def add_doc(table,doc,data):
        ret = {}
        try:
            db_read = open(f'{Path.home()}/.dbs/{db}/{table}/{doc}', 'r')
            f = db_read.read()
            db_read.close()

            ret = 'already exists, maybe you meant update?'
        except:
            k= base64.urlsafe_b64encode(db_pass.encode())
            f= Fernet(k)
            db_write = open(f'{Path.home()}/.dbs/{db}/{table}/{doc}', 'w')
            enc = f.encrypt(json.dumps(data).encode())
            db_write.write(enc.decode())
            ret = 'added'
        return ret

    def add_db(db_c):
        ret = {}
        try:
            os.mkdir(f'{Path.home()}/.dbs/{db_c}/')
            k= base64.urlsafe_b64encode(db_pass.encode())
            f= Fernet(k)
            ver = f.encrypt((f'/{db_c}+{db_user}/').encode()).decode()
            t = open(f'{Path.home()}/.dbs/{db_c}/catch.zts','w')
            t.write(ver)
            ret = 'db created'
        except:
            ret = 'already exists'
        return ret

    def add_table(db_c,table):
        ret = {}
        try:
            os.mkdir(f'{Path.home()}/.dbs/{db_c}/{table}/')
            ret = 'table created'
        except:
            ret = 'already exists'
        return ret

    def delete_doc(table,doc):
        ret = ''
        try:
            db_read = open(f'{Path.home()}/.dbs/{db}/{table}/{doc}', 'r')
            yn = input(f"are you sure you want to delete {doc} y/n? ")
            if yn == "y":
                f = db_read.read()
                db_read.close()
                z = json.loads(f)
                os.remove(f'{Path.home()}/.dbs/{db}/{table}/{doc}')
                ret = 'deleted'
        except:
            ret = 'doesnt exist'
        return ret

    def dump_table(table):
        ret = {}
        try:
            x=os.listdir(f'{Path.home()}/.dbs/{db}/{table}/')
            x.remove('catch.zts')
            for i in range(len(x)):
                db_read = open(f'{Path.home()}/.dbs/{db}/{table}/{x[i]}', 'r')
                f = db_read.read()
                z = json.loads(f)
                ret[x[i]] = z
        except:
            ret = 'none'
        return ret

    def list_dbs():
        ret = {}
        try:
            x=os.listdir(f'{Path.home()}/.dbs/')
            x.remove("users.zts")
            ret = x
        except:
            ret = 'none'
        return ret

    def db_exists(db):
        ret = 1
        try:
            x=os.listdir(f'{Path.home()}/.dbs/')
            for i in range(len(x)):
                if x[i] == db:
                    ret *= 0
        except:
            ret = 1
        return ret

    def list_tables():
        ret = {}
        try:
            x=os.listdir(f'{Path.home()}/.dbs/{db}/')
            x.remove('catch.zts')
            ret = x
        except:
            ret = 'none1'
        return ret

    def list_docs(table):
        ret = {}
        try:
            x=os.listdir(f'{Path.home()}/.dbs/{db}/{table}/')
            ret = x
        except:
            ret = 'none'
        return ret
    
    def check_owner(db):

        t = open(f'{Path.home()}/.dbs/{db}/catch.zts','r')
        try:
            k= base64.urlsafe_b64encode(db_pass.encode())
            f= Fernet(k)
            f.decrypt(t.read().encode())
            return 1
        except:
            return 0


def register(user:str,pwd:str):
    try:
        global db_user
        global db_pass
        global db
        w = open(f'{Path.home()}/.dbs/users.zts','a')
        w.write(f"{user}:{md5(pwd.encode()).hexdigest()}\n")
        w.close()
        db_user = user
        db_pass = md5(pwd.encode()).hexdigest()
        db = ""
        return 1
    except:
        return 0

def login(user:str,pwd:str):
    try:
        global db_user
        global db_pass
        global db
        w = open(f'{Path.home()}/.dbs/users.zts','r')
        users = w.read().splitlines()
        w.close()
        check = f'{user}:{md5(pwd.encode()).hexdigest()}'
        if check in users:
            db_user = user
            db_pass = md5(pwd.encode()).hexdigest()
            db = ""
            return 1
        else:
            return 0
    except:
        return 0

for i in range(len(argv)-1):
    if "--user=" in argv[i+1]:
        usr = argv[i+1].split("--user=")[1]
        for y in range(3):
            u_pass = input(f"password: {Fore.BLACK}");print(f"{Fore.RESET}",end="")
            if login(usr,u_pass):
                print(f"{Fore.GREEN +'logged in successfuly.'+ Fore.RESET}")
                break
            else:
                print(f"{Fore.RED +'login failed!'+ Fore.RESET}")
    elif argv[i+1] == "--help" or argv[i+1] == "-h":
        print("""usage:
            --help/-h : for usage
    --user=/username/ : login as /username/
       --db=/db name/ : select initial database
""")
        exit()


for i in range(len(argv)-1):
    if "--db=" in argv[i+1] and PikaDB.db_exists(argv[i+1].split("--db=")[1])==0 and PikaDB.check_owner(argv[i+1].split("--db=")[1]):
        db = argv[i+1].split("--db=")[1]



print(banner[random.randint(0,2)])

commands = ["dbs","add","docs","use","dump","exit","help","delete","update","make","register","login","logout"]
special_characters = "'!@#$%^&*()-+?=,\<>/\""




while 1:
    try:
        command = input(f"({Fore.WHITE+db_user+Fore.RESET})pikadb[{Fore.GREEN + db + Fore.RESET}]> ")
        if command == "dbs":
            print(PikaDB.list_dbs())
        elif command == "login":
            user = input("username: ")
            u_pass = input(f"password: {Fore.BLACK}");print(f"{Fore.RESET}",end="")
            if login(user,u_pass):
                print(f"{Fore.GREEN +'logged in successfuly.'+ Fore.RESET}")
            else:
                print(f"{Fore.RED +'login failed!'+ Fore.RESET}")
        elif command == "register":
            user = input("username: ")
            u_pass = input(f"password: {Fore.BLACK}");print(f"{Fore.RESET}",end="")
            cu_pass = input(f"confirm password: {Fore.BLACK}");print(f"{Fore.RESET}",end="")
            if u_pass == cu_pass:
                if register(user,u_pass):
                    print(f"{Fore.GREEN +'registered successfuly.'+ Fore.RESET}")
                else:
                    print(f"{Fore.RED +'registering has failed!'+ Fore.RESET}")
            else:
                print(f"{Fore.RED +'registering has failed!'+ Fore.RESET}")
        elif command == "logout":
            db_user = "public"
            db_pass = "4c9184f37cff01bcdc32dc486ec36961"
            db=""
        elif command == "tables":
            if db != '':
                print(PikaDB.list_tables())
            else:
                print("none")
        elif command.startswith("get "):
            cmd =command.split()
            if db != '' and len(cmd) > 3 :
                table = cmd[3]
                doc = cmd[1]
                if table:
                    print(PikaDB.get_doc(table,doc))
                else:
                    print("table?")
            else:
                print("none")
        elif command.startswith("add "):
            cmd =command.split()
            if db != '' and len(cmd) == 6 :
                table = cmd[3]
                doc = cmd[1]
                data = cmd[5]
                try:
                    data = json.loads(data)
                    if table:
                        print(PikaDB.add_doc(table,doc,data))
                    else:
                        print("table?")
                except:
                    print(f"error: {Fore.RED +'invalid data!'+ Fore.RESET}")
            else:
                print("none")
        elif command.startswith("update "):
            cmd =command.split()
            if db != '' and len(cmd) == 6 :
                table = cmd[3]
                doc = cmd[1]
                data = cmd[5]
                try:
                    data = json.loads(data)
                    if table:
                        print(PikaDB.update_doc(table,doc,data))
                    else:
                        print("table?")
                except:
                    print(f"error: {Fore.RED +'invalid data!'+ Fore.RESET}")
            else:
                print("none")
        elif command.startswith("delete "):
            cmd =command.split()
            if db != '' and len(cmd) > 3 :
                table = cmd[3]
                doc = cmd[1]
                if table:
                    print(PikaDB.delete_doc(table,doc))
                else:
                    print("table?")
            else:
                print("none")
        elif command.startswith("docs "):
            cmd =command.split()
            if db != '' and len(cmd) > 1 :
                table = cmd[1]
                if table:
                    print(PikaDB.list_docs(table))
                else:
                    print("table?")
            else:
                print("none")
        elif command.startswith("use "):  #################  USE
            cmd = command.split()
            if len(cmd) > 1:
                db_c = command.split()[1]
                if PikaDB.db_exists(db_c)==0 and PikaDB.check_owner(db_c):
                    print(f"using {db_c}")
                    db = cmd[1]
                else:
                    print(f"{Fore.RED +'wrong db or ownership!' + Fore.RESET}")
            else:
                print("use what?")
        elif command.startswith("dump "):  ############### DUMP
            cmd = command.split()
            if db != '' and len(cmd) > 1 :
                table_c = command.split()[1]
                if table_c:
                    print(PikaDB.dump_table(table_c))
                else:
                    print("table?")
            else:
                print("none")
        elif command.startswith("make "):
            cmd =command.split()
            if len(cmd) == 3 :
                if cmd[1] == 'db' and not any(c in special_characters for c in cmd[2]):
                    table_db = cmd[2]
                    if table_db:
                        print(PikaDB.add_db(table_db))
                    else:
                        print("table?")
                elif cmd[1] == 'table' and not any(c in special_characters for c in cmd[2]):
                    table_db = cmd[2]
                    if db != '':
                        print(PikaDB.add_table(db,table_db))
                else:
                    print("you have to select either db or table \nyou cant have special characters except _")
                
            else:
                print(f"{Fore.RED +'error in arguments!' + Fore.RESET}")
        elif command == "exit":
            print("bye.")
            exit()
        elif command == "help":
            print(
            """ 
                  help : shows this help menu
                  exit : closes pikadb
                 login : log in your account
              register : sign up for an account
                logout : go back to the "public" account 
          dump /table/ : gets every doc in the table
          docs /table/ : shows all docs in the table
                   dbs : show all dbs
                 table : show all tables in the selected db
              use /db/ : selects /db/ as the current used db
                 make db/table /name/ : creates a new db or table
               get /doc/ from /table/ : displays content of /doc/ from /table/
   add /doc/ to /table/ with {/data/} : adds /doc/ to /table/ with {/data/} inside
update /doc/ to /table/ with {/data/} : updates /doc/ to /table/ with {/data/} inside
            delete /doc/ from /table/ : deletes /doc/ from /table/
            """)
        else:
            try:
                if  command.split()[0] in commands: 
                    print(f"type help to see how to use {command.split()[0]}")
                else:
                    print(f"unknown comand {Fore.RED +command.split()[0] + Fore.RESET}")
            except:
                    print(f"unknown comand")
    except KeyboardInterrupt:
        print("")

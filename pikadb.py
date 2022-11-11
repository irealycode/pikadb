import json
import os
from pathlib import Path
from colorama import Fore, Back, Style
import readline

db = "numbers"

print(""" 

           __  __                        __  __       
          /  |/  |                      /  |/  |      
  ______  $$/ $$ |   __   ______    ____$$ |$$ |____  
 /      \ /  |$$ |  /  | /      \  /    $$ |$$      \ 
/$$$$$$  |$$ |$$ |_/$$/  $$$$$$  |/$$$$$$$ |$$$$$$$  |
$$ |  $$ |$$ |$$   $$<   /    $$ |$$ |  $$ |$$ |  $$ |
$$ |__$$ |$$ |$$$$$$  \ /$$$$$$$ |$$ \__$$ |$$ |__$$ |
$$    $$/ $$ |$$ | $$  |$$    $$ |$$    $$ |$$    $$/ 
$$$$$$$/  $$/ $$/   $$/  $$$$$$$/  $$$$$$$/ $$$$$$$/  
$$ |                                                  
$$ |                pikadb v1.1                            
$$/             made by irealycode                                  

""")

def get_doc(table,doc):
    #checks if doc exists and gets data
    ret = {}
    try:
        db_read = open(f'{Path.home()}/.dbs/{db}/{table}/{doc}', 'r')
        f = db_read.read()
        db_read.close()
        ret = json.loads(f)
    except:
        ret = 'none'
    return ret

def update_doc(table,doc,data):
    #update or add items to doc
    ret = {}
    try:
        db_read = open(f'{Path.home()}/.dbs/{db}/{table}/{doc}', 'r')
        f = db_read.read()
        db_read.close()
        z = json.loads(f)
        lst = list(data.keys())
        for i in range(len(lst)):
            z[lst[i]] = data[lst[i]]
        db_write = open(f'{Path.home()}/.dbs/{db}/{table}/{doc}', 'w')
        db_write.write(json.dumps(z))
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
        z = json.loads(f)
        ret = 'already exists, maybe you meant update?'
    except:
        db_write = open(f'{Path.home()}/.dbs/{db}/{table}/{doc}', 'w')
        db_write.write(json.dumps(data))
        ret = 'added'
    return ret

def delete_doc(table,doc):
    ret = ''
    try:
        yn = input(f"are you sure you want to delete {doc} y/n? ")
        if yn == "y":
            db_read = open(f'{Path.home()}/.dbs/{db}/{table}/{doc}', 'r')
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

commands = ["dbs","add","docs","use","dump","exit","help","delete","update"]

while 1:
    try:
        command = input(f"pikadb[{Fore.GREEN + db + Fore.RESET}]> ")
        if command == "dbs":
            print(list_dbs())
        elif command == "tables":
            if db != '':
                print(list_tables())
            else:
                print("none")
        elif command.startswith("get "):
            cmd =command.split()
            if db != '' and len(cmd) > 3 :
                table = cmd[3]
                doc = cmd[1]
                if table:
                    print(get_doc(table,doc))
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
                        print(add_doc(table,doc,data))
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
                        print(update_doc(table,doc,data))
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
                    print(delete_doc(table,doc))
                else:
                    print("table?")
            else:
                print("none")
        elif command.startswith("docs "):
            cmd =command.split()
            if db != '' and len(cmd) > 1 :
                table = cmd[1]
                if table:
                    print(list_docs(table))
                else:
                    print("table?")
            else:
                print("none")
        elif command.startswith("use "):
            cmd = command.split()
            if len(cmd) > 1:
                db_c = command.split()[1]
                if db_exists(db_c)==0:
                    print(f"using {db_c}")
                    db = cmd[1]
                else:
                    print("none")
            else:
                print("use what?")
        elif command.startswith("dump "):
            cmd = command.split()
            if db != '' and len(cmd) > 1 :
                table_c = command.split()[1]
                if table_c:
                    print(dump_table(table_c))
                else:
                    print("table?")
            else:
                print("none")
        elif command == "exit":
            print("bye.")
            exit()
        elif command == "help":
            print(
            """ 
                  help : shows this help menu
                  exit : closes pikadb
          dump /table/ : gets every doc in the table
          docs /table/ : shows all docs in the table
                   dbs : show all dbs
                 table : show all tables in the selected db
              use /db/ : selects /db/ as the current used db
               get /doc/ from /table/ : displays content of /doc/ from /table/
   add /doc/ to /table/ with {/data/} : adds /doc/ to /table/ with {/data/} inside
update /doc/ to /table/ with {/data/} : updates /doc/ to /table/ with {/data/} inside
            delete /doc/ from /table/ : deletes /doc/ from /table/
            """)
        else:
            if  command.split()[0] in commands: 
                print(f"type help to see how to use")
            else:
                print(f"unknown comand {Fore.RED +command.split()[0] + Fore.RESET}")
    except KeyboardInterrupt:
        print("")

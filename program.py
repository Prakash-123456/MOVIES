import sqlite3 as d

a = d.connect("db.db")
try:
    a.execute("Create table movies(name ,actor ,actress ,director ,year );")
    #def insert(name,act,acts,dir,yr):

except:

     pass

st = ''
while(st != 'q'):
    print("1.) Insert\n2.) show all \n3.) search \nq.) quit ")
    st = input ("ENTER OPTIONS:")
    if(st == '1'):
        name = input ("Enter the name:")
        act = input ("Enter the actor:")
        acts = input ("Enter the actress:")
        dir = input ("Enter the director:")
        yr = input ("Enter the year:")
        a.execute(f'insert into movies values("{name}","{act}","{acts}","{dir}","{yr}");')
        a.commit()
    elif(st == '2'):
        print("name | actor  | actress  |  director  |  year)")
        for i in a.execute("select * from movies;"):
            for j in i:
                print(j +"  | ", end='' )
            print()
    elif(st == '3'):
        c = input("Column name:")
        v = input("Enter value:")
        print("(name, actor, actress, director, year)")
        for i in a.execute(f'select * from movies where {c}="{v}";'):
            print(i)
            
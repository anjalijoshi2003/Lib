import mysql.connector as con1
try:
    c1=con1.connect(host='localhost',user='root',password='',database='facebook')
    cr=c1.cursor()
    print("connection done")
    def insert_val():
        try:
            Id=int(input("enter the id:"))
            name=input("ennter the name:")
            sal=int(input("enter the salary"))
            qr="insert into registration values(%s,%s,%s)"
            val=(Id,name,sal)
            cr.execute(qr,val)
            c1.commit()
            print("data inserted")
        except Exception as e:
            print("something wrong",e)
    def update_val():
        id=input("enter the id")
        name=input("enter the name:")
        sal=input("enter the salary")
        qr="update registration set user_name=%s,user_payment=%s where user_id=%s"
        val=(name,sal,id)
        cr.execute(qr,val)
        c1.commit()
        print("update successfully")
    def delete_val():
        id=int(input("enter the id"))
        qr="delete from registration where user_id=%s "
        val=(id,)
        cr.execute(qr,val)
        c1.commit()
        print("delete  successfully")
    def show_name():
        qr="select * from registration ";
        cr.execute(qr)
        data = cr.fetchall()   
        i=1
        if data:
             for r in data:
                print("----------------------Employee ",i,":----------------------------")
                print("'Name:-",r[0])
                print("\nCity:-",r[1])
                print("\nAge:-",r[2])
                i+=1
        else:
            print("No record found.")
    def show_by_name():
            name=input("enter the name for show_details:-")
            qry='select * from registration where user_name=%s'
            vals=(name,)
            cr.execute(qry,vals)
            data=cr.fetchall()
            print(data)
            c1.commit()
    def total_row():
        qr="select * from registration"
        cr.execute(qr)
        d=cr.fetchall()
        i=0
        for r in d:
            i+=1
        print("number of employee  ",i)
    while True:
        print("Option")
        print("\n1.Insert Data")
        print("\n2.Update Data")
        print("\n3.Delete Data")
        print("\n4.Show Data")
        print("\n5.show_by_name")
        print("\n6.Total_count")
        print("\n7.Exit")
        choice=int(input("Enter the choice:-"))
        match  choice:
            case 1:
                print("----------Insert the Data----------")
                insert_val()
            case 2:
                print("----------Enter data----------")
                update_val()
            case 3:
                print("----------Enter data----------")
                delete_val()
            case 4:
                print("----------Enter data----------")
                show_name()
            case 5:
                print("----------Enter data----------")
                show_by_name()
            case 6:
                print("----------Enter data----------")
                total_row()
            case 7:
                    break  
    
    
    
    
except Exception as e:
        print("comething wrong",e) 
  

 

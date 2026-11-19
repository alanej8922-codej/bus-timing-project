import sqlite3

#connect to database
conn=sqlite3.connect("bus.db")
#create cursor
cursor=conn.cursor()

#create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS buses (
    id INTEGER PRIMARY KEY,
    from_place TEXT,
    to_place TEXT,
    departure_time TEXT
)
""")


#to delete a data from data base

#cursor.execute("DELETE FROM buses WHERE id=7")
#conn.commit()

while True:
    print("\n===== BUS TIMING PROJECT=====")
    print("1.add bus timing")
    print("2.search bus")
    print("3.view all buses")
    print("4.update bus timing")
    print("5.delete bus timing")
    print("6.exit")
    choice=input("Enter your choice:")

    if choice=="1":
        from_place=input("Enter starting place:")
        to_place=input("enter destination:")
        departure=input("enter departure time:")

        cursor.execute("""INSERT INTO buses(from_place,to_place,departure_time)VALUES(?,?,?)""",(from_place,to_place,departure))
        conn.commit()
        print("bus timing added successfully")

    elif choice=="2":
        from_place=input("Enter starting place:")
        to_place=input("Enter destination:")
        cursor.execute("""SELECT*FROM buses WHERE from_place =? AND to_place =?""",(from_place,to_place))

        buses = cursor.fetchall()
        print("\nAvailable buses:")

        for bus in buses:
            print(bus)

    elif choice=="3":
        cursor.execute("SELECT*FROM buses")
        buses=cursor.fetchall()
        print("\nAll buses:")

        for bus in buses:
            print(bus)

    elif choice=="4":
        bus_id=int(input("enter bus id:"))
        new_time=input("Enter new departure time:")
        cursor.execute("UPDATE buses SET departure_time=? WHERE id=?",(new_time,bus_id))
        conn.commit()

        print("bus timing updated successfully")

    elif choice=="5":
        bus_id=int(input("Enter bus id to delete:"))
        cursor.execute("DELETE FROM buses WHERE id=?",(bus_id,))
        conn.commit()
        print("bus timing deleted successfully")

    elif choice=="6":
        print("Tanks you for using bus Timing project!")
        break

conn.close()

#!/usr/bin/python3
"""Write a script that lists all states from the database """


def main():
    """connect to mysql and run query"""
    from sys import argv
    import MySQLdb

    username = str(argv[1])
    password = str(argv[2])
    db_name = str(argv[3])
    state_name = str(argv[4])

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=db_name,
                         charset="utf8")
    if (db):
        """carry out normal procedure"""
        con = db.cursor()
        con.execute(
            "SELECT * FROM states WHERE BINARY \
              name= %s ORDER BY id ASC", (state_name,))
        rows = con.fetchall()
        for row in rows:
            print(row)
        con.close()
        db.close()
    else:
        """terminate"""
        print("Connection unsuccesful")


if __name__ == '__main__':
    main()

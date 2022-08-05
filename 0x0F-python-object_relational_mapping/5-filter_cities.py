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
        sql_q = "SELECT cities.name FROM cities\
          join states ON cities.state_id = states.id \
            WHERE states.name = %s ORDER BY\
            cities.id ASC;"
        con.execute(sql_q, (state_name,))
        rows = con.fetchall()
        """
        print(type(rows))
        print(rows)
        """
        print(', '.join([row[0] for row in rows]))
        con.close()
        db.close()
    else:
        """terminate"""
        print("Connection unsuccesful")


if __name__ == '__main__':
    main()

from sqlalchemy import text
from scriptLogic.engine import engine

# Test db connection
def test_db_connection():
    try:
        with engine.connect() as connection:
            # Führe einen einfachen SQL-Befehl aus
            result = connection.execute(text("SELECT VERSION();"))
            print("Verbindung erfolgreich!")
            print(f"Datenbankversion: {result.scalar()}")
    except Exception as e:
        print(f"Fehler bei der Verbindung: {e}")


# select all places from db
def get_all_locations():
    try:
        with engine.connect() as connection:
            # text constructor to use sql language
            query = text("SELECT Name, Adresse, Zoom, Level FROM ort;")

            # run query on db
            result = connection.execute(query)

            # print results
            print("\nAlle importierten Orte:")
            for row in result:
                # row is a tupel (or row-object), needs to be accessed as following
                print(f"Name: {row.Name}, Adresse: {row.Adresse}, Level: {row.Level}")

    except Exception as e:
        print(f"Fehler bei der Abfrage: {e}")

# Custom SELCT query
def dbQuery(sqlQuery):
    try:
        with engine.connect() as connection:
            query = text(sqlQuery)
            return connection.execute(query)
    except Exception as e:
        print(f"Fehler bei der SQL-Abfrag   e: {e}")
        return None

# Custom INSERT query
# ATTENTION: This is vulnerable to SQL-Injection,
# do not copy paste this function in productive systems
def dbInsertUpdateDelete(sqlQuery):
    try:
        with engine.connect() as connection:
            query = text(sqlQuery)
            connection.execute(query)
            connection.commit()
            print("DBInsertUpdateDetele erfolgreich.")
            return True
    except Exception as e:
        print(f"Fehler bei insert, update oder delete in der DB: {e}")
        return False
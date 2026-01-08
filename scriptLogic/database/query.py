from sqlalchemy import text
from scriptLogic.database.engine import engine

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

# Custom SELCT query
def dbQuery(sqlQuery):
    try:
        with engine.connect() as connection:
            query = text(sqlQuery)
            return connection.execute(query)
    except Exception as e:
        print(f"Fehler bei der SQL-Abfrage: {e}")
        return None

# Custom INSERT query
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

import mysql.connector
from mysql.connector import Error



db_host = "localhost"
db_user = "root"
db_password = "arcadia89"
db_name = "nlp_project"

DB_CONFIG = {
    'host':"localhost",
    'user':db_user,
    'password':db_password,
    'database':db_name,
    'port':3306
}

def create_connection():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            cursor = connection.cursor()
            return connection, cursor
    except Error as e:
        print(f"Error: {e}")
        return None

def close_conn(conn,cursor):
    try:
        cursor.close()
        conn.close()
    except Error as e:
        print(f"Error: {e}")

def selectQuery(queries, fetchType=1):
    """
    Funzione per eseguire una o più query su un database MySQL.

    Args:
        queries (str): Una query SQL o più query separate da punto e virgola.
        fetchType (int): 0 per fetchone, 1 per fetchall.

    Returns:
        list: Lista di risultati per ciascuna query eseguita.
              Ogni risultato può essere una lista di tuple o una singola tupla.
    """
    # Creazione della connessione e cursore
    conns = create_connection()
    conn = conns[0]
    cursor = conns[1]
    
    allResults = []  # Lista per memorizzare i risultati di tutte le query

    try:
        # Esecuzione delle query (supporta query multiple con multi=True)
        for result in cursor.execute(queries, multi=True):
            # Controlla se la query restituisce righe
            if result.with_rows:
                if fetchType == 0:  # Fetch di una sola riga
                    row = result.fetchone()
                    allResults.append(row)
                elif fetchType == 1:  # Fetch di tutte le righe
                    rows = result.fetchall()
                    allResults.append(rows)
                else:
                    print(f"fetchType '{fetchType}' non valido!")
                    return None
            else:
                # Per query che non restituiscono righe (es. INSERT, UPDATE)
                conn.commit()
                print(f"Query eseguita senza righe restituite: {result.statement}")

    except Exception as e:
        print(f"Errore nell'esecuzione delle query: {e}")
        return f"ERROR: {e}"

    finally:
        # Chiusura della connessione e del cursore
        close_conn(conn, cursor)

    # Ritorna tutti i risultati
    return allResults



def commitQuery(q):
    conns = create_connection()
    conn = conns[0]
    cursor = conns[1]     
    try:
        cursor.execute(q)
        conn.commit()
        t = None
        if "INSERT" in q:
            t = "INSERT "
        elif "DELETE" in q:
            t = "DELETE "
        elif "UPDATE" in q:
            t = "UPDATE "
        else:
            t = q
        print(f"Query {t} eseguita")
    except Exception as e:
        print(e)
    finally:
        close_conn(conn,cursor)
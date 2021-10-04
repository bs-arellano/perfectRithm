import psycopg2

db_user = 'postgres'
db_password = 'hyperpro16'

conn = None


def consultar_usuarios():
    try:
        conn = psycopg2.connect(
            f"dbname=Perfect_Rithm user={db_user} password={db_password}")
        cur = conn.cursor()
        cur.execute(
            'SELECT U.username, U.level, U.user_score FROM usuario U ORDER by U.user_score')
        data = cur.fetchall()
        cur.close()
        return data
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def consultar_usuario(username):
    try:
        conn = psycopg2.connect(
            f"dbname=Perfect_Rithm user={db_user} password={db_password}")
        cur = conn.cursor()
        cur.execute(
            f"SELECT U.username, U.level, U.user_score FROM usuario U  WHERE lower(U.username) like ('%{username}%') ORDER by U.user_score")
        data = cur.fetchall()
        cur.close()
        return data
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def consultar_canciones():
    try:
        conn = psycopg2.connect(
            f"dbname=Perfect_Rithm user={db_user} password={db_password}")
        cur = conn.cursor()
        cur.execute(
            'SELECT C.cancion_id, C.cancion_name, C.artista, C.genero FROM cancion C')
        data = cur.fetchall()
        cur.close()
        return data
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def consultar_cancion(cancion):
    try:
        conn = psycopg2.connect(
            f"dbname=Perfect_Rithm user={db_user} password={db_password}")
        cur = conn.cursor()
        cur.execute(
            f"SELECT C.cancion_id, C.cancion_name, C.artista, C.genero FROM cancion C WHERE C.cancion_name like ('%{cancion}%')")
        data = cur.fetchall()
        cur.close()
        return data
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def select_song(song):
    try:
        conn = psycopg2.connect(
            f"dbname=Perfect_Rithm user={db_user} password={db_password}")
        cur = conn.cursor()
        cur.execute(
            f"SELECT C.url_json, C.url_media FROM cancion C WHERE C.cancion_id = '{song}'")
        data = cur.fetchone()
        cur.close()
        return data
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
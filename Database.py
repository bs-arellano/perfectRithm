import psycopg2, uuid

db_user = 'postgres'
db_password = 'hyperpro16'

conn = None

def consultar_usuarios():
    try:
        conn = psycopg2.connect(
            f"dbname=Perfect_Rithm user={db_user} password={db_password}")
        cur = conn.cursor()
        cur.execute(
            'SELECT U.username, U.level, U.user_score FROM usuario U ORDER by U.user_score DESC')
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
            f"SELECT U.username, U.level, U.user_score FROM usuario U  WHERE lower(U.username) like ('%{username}%') ORDER by U.user_score DESC")
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
            f"SELECT C.cancion_id, C.url_json, C.url_media FROM cancion C WHERE C.cancion_id = '{song}'")
        data = cur.fetchone()
        cur.close()
        return data
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def select_user_by_email(email):
    try:
        conn = psycopg2.connect(
            f"dbname=Perfect_Rithm user={db_user} password={db_password}")
        cur = conn.cursor()
        cur.execute(
            f"SELECT * FROM usuario U WHERE U.email = '{email}'")
        data = cur.fetchone()
        cur.close()
        return data
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def select_user_by_id(uid):
    try:
        conn = psycopg2.connect(
            f"dbname=Perfect_Rithm user={db_user} password={db_password}")
        cur = conn.cursor()
        cur.execute(
            f"SELECT * FROM usuario U WHERE U.uid = '{uid}'")
        data = cur.fetchone()
        cur.close()
        return data
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def reg_user(username,email,password):
    uid = str(uuid.uuid5(uuid.NAMESPACE_DNS, username))
    try:
        conn = psycopg2.connect(
            f"dbname=Perfect_Rithm user={db_user} password={db_password}")
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO usuario (uid, username, email, password, level, user_score) VALUES (%s,%s,%s,%s,%s,%s)", (uid,username,email,password,1,0))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def consultar_noticias():
    try:
        conn = psycopg2.connect(
            f"dbname=Perfect_Rithm user={db_user} password={db_password}")
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM news ORDER by news.fecha DESC")
        data = cur.fetchall()
        cur.close()
        return data
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def new_reg(uid, cancion_id, score, acc):
    try:
        conn = psycopg2.connect(
            f"dbname=Perfect_Rithm user={db_user} password={db_password}")
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO record (serial, user_id, cancion_id, score, accuracy, date) VALUES (DEFAULT,%s,%s,%s,%s,CURRENT_DATE)", (uid,cancion_id,score, acc))
        conn.commit()
        cur.execute(f"UPDATE usuario SET user_score = (user_score+{score}) WHERE uid = '{uid}'")
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def select_records_by_uid(uid):
    try:
        conn = psycopg2.connect(
            f"dbname=Perfect_Rithm user={db_user} password={db_password}")
        cur = conn.cursor()
        cur.execute(
            f"SELECT C.cancion_name, R.score, R.accuracy, R.date FROM record R, cancion C WHERE R.user_id = '{uid}' and R.cancion_id = C.cancion_id ORDER by R.score DESC")
        records = cur.fetchall()
        cur.close()
        return records
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
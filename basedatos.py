import sqlite3

def connect():
    con = sqlite3.connect("ejemplo2.db")
    return con

def create_db (con):
    sql = "create table gente (nombre, telefono, id_localidad)"
    con.execute(sql)
    sql = "create table localidades (id_localidad, nombre, provincia)"
    con.execute(sql)
    con.commit()
        
def alta(con, nombre, telefono, id_localidad):
    sql = "insert into gente (nombre, telefono, id_localidad) values (?,?, ?)"
    con.execute(sql, (nombre, telefono, id_localidad))
    con.commit()

def alta_localidad(con, id_localidad, nombre, provincia):
    sql = "insert into localidades (id_localidad, nombre, provincia) values (?,?, ?)"
    con.execute(sql, (id_localidad, nombre, provincia))
    con.commit()

def consulta_loc(con):
    sql = "select id_localidad, nombre, provincia from localidades"
    cur = con.cursor()
    cur.execute(sql)
    print("-" * 30)
    for row in cur.fetchall():
        print(row)


def modificar(con, nombre, telefono, rowid):
    sql = "update gente set nombre = ?, telefono = ? where rowid = ?"
    con.execute(sql, (nombre, telefono, rowid))
    con.commit()
    
def borrar(con, nombre):
    sql = "delete from gente where nombre = ?"
    con.execute(sql, (nombre,))
    con.commit()

    
def consulta(con):
    sql = "select rowid, nombre, telefono, id_localidad from gente order by telefono"
    cur = con.cursor()
    cur.execute(sql)
    print("-" * 30)
    for row in cur.fetchall():
        print(row)

def consulta_comp(con):
    sql = """
        select gente.nombre, gente.telefono, localidades.nombre, localidades.provincia
        from gente inner join localidades
        on gente.id_localidad = localidades.id_localidad
        """
    cur = con.cursor()
    cur.execute(sql)
    print("-" * 30)
    for row in cur.fetchall():
        print(row)


def contar(con):
    sql = "select count(*) from gente"
    cur = con.cursor()
    cur.execute(sql)
    print("cantidad:", cur.fetchone())
    
def agrupar(con):
    sql = "select nombre, count(*) from gente group by nombre"
    cur = con.cursor()
    cur.execute(sql)
    print("*" * 30)
    for row in cur.fetchall():
        print(row)
        
con = connect()
# create_db(con)
# alta_localidad(con, 1, "Resistencia", "Chaco")
# alta_localidad(con, 2, "Corrientes", "Corrientes")
# alta(con, "Karina", "4587")

alta(con, "Olga", "999", 7)
consulta_comp(con)


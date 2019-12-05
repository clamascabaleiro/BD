import sqlite3 as dbapi

print(dbapi.apilevel)
print(dbapi.threadsafety)
print(dbapi.paramstyle)

try:

    bbdd = dbapi.connect("baseDatosProba.dat")
    cursor = bbdd.cursor()

    #cursor.execute("""create table usuarios
     #                   (dni text,
      #                  nome text,
       #                 direccion text)""")

    #cursor.execute("""insert into usuarios
     #               VALUES ('33333333-Z',
      #                      'Paco',
       #                     'Urzaiz')""")

    #cursor.execute("""insert into usuarios
     #                   VALUES ('33333337-B',
      #                          'Anais',
       #                         'Areal')""")

    cursor.execute("""SELECT * FROM usuarios""")

    #print(cursor.fetchmany(2))
    #print(cursor.fetchmany(2))
    #print(cursor.fetchone())

    for usuario in cursor.fetchall():
        print ("Usuario : ", usuario[1])
        print("Dni : ", usuario[0])
        print("Direccion : ", usuario[2])
        print("*********************")

    bbdd.commit()

except dbapi.OperationalError as erroOperacion:
    print("Erro(operationalError : " + str (erroOperacion))
except dbapi.DatabaseError as erroBaseDatos:
    print("Erro(DatabaseError : " + str(erroBaseDatos))
finally:
    cursor.close()
    bbdd.close()
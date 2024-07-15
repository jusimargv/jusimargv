import sqlite3
from pathlib import Path
ROOT_PATH = Path(__file__).parent
con = sqlite3.connect(ROOT_PATH / "my_data.db")
cur = con.cursor()

def ceate_table(con, cur):
    cur.execute(
        "CREATE TABLE clientes(id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(255), email VARCHAR(255), endereco VARCHAR(255))"
        
    )
    con.commit()
    
def set_register(con, cur, nome, email, endereco):   
  data = (
      "Paula karina", "jusimargv@gmail.com"," Rua nra do carmo 505", 2
      )
  cur.execute("INSERT INTO clientes (nome, email, endereco) VALUES (?,?,?);", data) #? = placeholder
  con.commit()
  
  
def update_register(con, cur, nome,email, endereco, id):
  data =( "Giovanna", "gi@gamil.com", "Rua 2", id)
  cur.execute(" UPDATE clientes SET nome = ?, email= ?, endereco =? WHERE  id = ?;", data) #? = placeholder
  con.commit()
  
def delete_register(con, cur,id):
  data =( id,)
  cur.execute(" DELETE FROM clientes WHERE  id = ?;", data) #? = placeholder
  con.commit()
  
def fetch_register( cur,id):
    cur.execute(" SELECT * FROM clientes WHERE  id = ?;", (id,)) #? = placeholder
    return cur.fetchone()
cliente = fetch_register(cur, 3)
print(cliente)

def fetch_registers(cur, id):
     cur.row_factory = sqlite3.Row
     cur.execute(" SELECT * FROM clientes WHERE  id = ?; ", (id,)) #? = placeholder
     return cur.fetchone()

    
    
def set_registers(con, cur, datas):   
  cur.executemany("INSERT INTO clientes (nome, email, endereco) VALUES (?,?,?);", datas) #? = placeholder
  con.commit()
datas = [
      ("Paula karina", "Paulaknascimento@gmail.com"," Rua 11"),
      (" karina", "k@gmail.com"," Rua 5"),
      ("bette", "bette@gmail.com"," Rua 505"),
      ("Ronaldo", "roni@gmail.com"," Rua 10"),
      ("marcio", "marcio@gmail.com"," Rua 23"),
      ("Debora", "debora@gmail.com"," Rua 50"),
      ("Hector", "hector@gmail.com"," Rua 6"),
      ("jusimar Alves", "jusimargv@gmail.com"," Rua 15"),
   ]  
fetch_registers( cur, 5)

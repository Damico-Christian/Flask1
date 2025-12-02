import pymysql

class DatabaseWrapper:

    #costruttore, contiene i dati di connessione al db
    def __init__(self, host, user, password, database, port):
        self.db_config = {
            'host': host,
            'user': user,
            'password': password,
            'database': database,
            'port': port, 
            'cursorclass': pymysql.cursors.DictCursor
        }
        self.create_table()  #chiama il metodo sotto

    #apre la connessione ogni volta che serve
    def connect(self):
        return pymysql.connect(**self.db_config)

    #operazioni INSERT, DELETE (tutte le op di DML e DDL)
    def execute_query(self, query, params=()):
        conn = self.connect()
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            conn.commit()
        conn.close()

    #SELECT (ritorna lista di dizionari)
    def fetch_query(self, query, params=()):
        conn = self.connect()
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            result = cursor.fetchall()
        conn.close()
        return result
    
    #da qui in poi dipende dal progetto
    #prima uguale x ogni progetto

    #qui creiamo la/le tabella/e
    def create_table(self):
        self.execute_query('''
            CREATE TABLE IF NOT EXISTS ListaSpesa (
                id INT AUTO_INCREMENT PRIMARY KEY,
                elemento VARCHAR(100) NOT NULL
            )
        ''')

    #SELECT *
    def get_lista_spesa(self):
        return self.fetch_query("SELECT * FROM ListaSpesa")

    #INSERT
    def aggiungi_elemento(self, elemento):
        self.execute_query(
            "INSERT INTO ListaSpesa (elemento) VALUES (%s)", (elemento,)
            #%s fa da placeholder: "la variabile che passo come parametro prende il valore di %s"
        )
import mysql.connector as mc
import subprocess, os, datetime, logging

# MAKE PATH IT DIR
dirone = os.path.dirname(__file__)
# MAKE THE DIRONE TO USE IT
dirtwo = os.path.join(dirone, "backup")
dirlog = os.path.join(dirone, "logs")

#RESET LOG FILE
try:
            if f"{dirlog}/viewlog.txt":
                os.remove(f"{dirlog}/viewlog.txt")
except:
            pass

#CREATE LOG FILE AND WRITE INTO "CALLBACK LOGGINS"
logging.basicConfig(filename=f"{dirlog}/viewlog.txt", format="%(asctime)s")


#########################################################################################
############################ WIRE DATA LOGIC ############################################
#########################################################################################
val =[
]#**************************************************************************************#
used2 ={ 
}#**************************************************************************************#
c1 ={
}#**************************************************************************************#
used ={
}#**************************************************************************************#
ft = {"number" : 10
}#**************************************************************************************#
where2 =[
]#**************************************************************************************#
columns =[
]#**************************************************************************************#
columns1 =[
]#**************************************************************************************#
where =[
]#**************************************************************************************#


class one:

    def __init__(self, **kwargs):
        self.con = mc.connect(**kwargs)
        self.cur = self.con.cursor(buffered=True)
        self.cp = one.torf(self)

    def xye(fr):
         def xye1(self, *args, **kwargs):
            try:
                fr(self, *args, **kwargs)
            except Exception as e:
                logging.exception(e)
                return e
            finally:
                if one.torf:
                    self.con.commit()
                    one.closed(self)
                    logging.getLevelName("The conection has closed")
            try:       
                return self.reg
            except:
                return None
         return xye1


    def exx(self, sql):
            try:
                self.cur.execute(sql)
                self.reg = self.cur.fetchall()
                return self.reg
            except Exception as e:
                self.texterror = [f"{e}"]
                logging.exception(e)
                return self.texterror
            finally:
                if one.torf:
                    self.con.commit()
                    one.closed(self)

    @xye
    def show(self):
         self.cur.execute("SHOW DATABASES")
         self.reg = self.cur.fetchall()

    @xye
    def drop(self, sql):
         self.cur.execute(f"DROP DATABASE {sql}")
         
    @xye
    def newdatabase(self, sql):
         self.cur.execute(f"CREATE DATABASE IF NOT EXISTS {sql}")
    
    @xye
    def copydb(self, namedb):
            self.formatime = datetime.datetime.now().strftime("%y-%b-%d %H-%M-%S")
            try:
                with open(f"{dirtwo}/{namedb}_{self.formatime}.sql", "w") as out:
                    subprocess.Popen(f'"C:/Program Files/MySQL/MySQL Workbench 8.0/"mysqldump --user={c1["user"]} --password={c1["password"]} --databases {namedb}', shell=True, stdout=out)
            except Exception as e:
                logging.exception(e)

    def uploaddb(namedb):
        try:
            subprocess.Popen(f'"C:/Program Files/MySQL/MySQL Workbench 8.0/"mysql --user={c1["user"]} --password={c1["password"]} <"{dirtwo}/{namedb}.sql"', shell=True)
        except Exception as e:
            logging.exception(e)

    @xye
    def databases(self):
        self.cur.execute("SELECT table_schema, table_name FROM  INFORMATION_SCHEMA.TABLES;")
        self.reg = self.cur.fetchall()
    
    @xye
    def db_inside(self, sql):
        self.cur.execute(f'SELECT table_schema, table_name FROM  INFORMATION_SCHEMA.TABLES WHERE table_schema LIKE "{sql}";')
        self.reg = self.cur.fetchall()

    @xye
    def usedb_deletetable(self, sql, sql2):
            self.cur.execute(f"USE {sql}")
            self.cur.execute(f"DROP TABLE IF EXISTS {sql2}")
    
    @xye
    def show_columns(self, sql, sql2):
         self.cur.execute(f"USE {sql}")
         self.cur.execute(f"SHOW COLUMNS FROM {sql}.{sql2}")
         self.reg = self.cur.fetchall()


    def show_columns_add(self, sql, sql2):
        self.cur.execute(f"USE {sql}")
        self.cur.execute(f"SHOW COLUMNS FROM {sql}.{sql2}")
        self.results = self.cur.fetchall()
        for i in self.results:
             columns.append(i[0])
    @xye
    def show_all_from(self, sql, sql2, ft):
        self.cur.execute(f"USE {sql}")
        self.cur.execute(f"SELECT * FROM {sql2}")
        self.reg = self.cur.fetchmany(ft)
    

    @xye
    def truncate(self, sql, sql2):
        self.cur.execute(f"USE {sql}")
        self.cur.execute(f"TRUNCATE TABLE {sql2}")
    
    @xye
    def insert_record(self, sql, sql2):
        self.cur.execute(f"USE {used["text"]}")
        self.cur.executemany(f"INSERT INTO {used["values"][0]} ({sql}) VALUES ({sql2})", val)

                         
    @xye
    def delete_from(self, sql, sql2):
         self.cur.execute(f"USE {used["text"]}")
         self.cur.execute(f"DELETE FROM {used["text"]} WHERE {sql} = '{sql2}'")

    @xye
    def select_columns_fetch(self, sql2, sql3, ft):
        self.cur.execute(f"USE {used["text"]}")
        self.cur.execute(f"SELECT {sql3} FROM {used["text"]}.{sql2}")
        self.reg = self.cur.fetchmany(ft)
    
    @xye
    def create_table(self, sql, sql2, sql3):
        self.cur.execute(f"USE {sql}")
        self.cur.execute(f"CREATE TABLE {sql2} ({sql3})")

    @xye
    def where(self, sql2, sql3, ft):
        self.cur.execute(f"USE {used["text"]}")
        self.cur.execute(f"SELECT * FROM {used["text"]}.{sql2} WHERE {sql3}")
        self.reg = self.cur.fetchmany(ft)

    @xye
    def alter_table(self, sql):
         self.cur.execute(f"USE {used2["text"]}")
         self.cur.execute(f"alter table {used2['values'][0]} {sql}")
        
    def torf(self):
        return self.con.is_connected()

    def closed(self):
        self.con.close()
        self.cur.close()



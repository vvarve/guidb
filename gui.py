from tkinter import LabelFrame, Label, Button, Entry, Tk, END, Toplevel, Text, ttk, Scrollbar, Menu, Menubutton, StringVar, messagebox
from PIL import Image, ImageTk
from ast import literal_eval
import os
import sqlquery as m1

root = os.path.dirname(__file__)
ima = os.path.join(root, "images")

class login:
    def __init__(self):
        self.interface = Tk()
        self.interface.title("HOME LOGIN MYSQL")
        self.interface.iconbitmap(os.path.join(ima, "icon.ico"))
        self.interface.geometry("500x550")
        self.interface.resizable(False, False)

        #FRAMES
        self.frame = LabelFrame(self.interface, border=0,)
        self.frame.grid(row=0, column=0, padx=30, pady=10)

        #Home IMAGES
        self.image1 = ImageTk.PhotoImage(Image.open(os.path.join(ima, "1.png")).resize((300,300)))
        Label(master=self.frame, text="", image=self.image1).grid(row=0, column=2 , pady=50, padx=0)

        #HOST
        Label(self.frame, text="HOST",).grid(row=1, column=0)
        self.host = Entry(master=self.frame, width=40, fg="grey35", highlightbackground="grey50", highlightcolor="grey50", highlightthickness=1)
        self.host.insert(0, "Localhost or IP Address")
        self.host.bind("<Button-1>", lambda push: self.host.delete(0, END))
        self.host.grid(row=1, column=2, pady=2)

        #USER
        Label(self.frame, text="USER",).grid(row=2, column=0)
        self.name = Entry(master=self.frame, border=0, width=40, fg="grey35", highlightbackground="grey50", highlightcolor="grey50", highlightthickness=1)
        self.name.insert(0, "Username")
        self.name.bind("<Button-1>", lambda push: self.name.delete(0, END))
        self.name.grid(row=2, column=2, pady=2)

        #PASSWORD
        Label(self.frame, text="PASSWORD",).grid(row=3, column=0)
        self.password = Entry(master=self.frame, show="*", border=1, width=40, fg="grey35", highlightbackground="grey50", highlightcolor="grey50", highlightthickness=1)
        self.password.insert(0, "*******")
        self.password.bind("<Button-1>", lambda push: self.password.delete(0, END))
        self.password.grid(row=3, column=2, pady=2)

        #PRINCIPAL BUTTON
        self.signin = Button(self.frame, text="SIGN IN", bd=0, background="grey20", highlightthickness=1, fg="grey100", activebackground="grey70", activeforeground="white", height=4, command=self.entryget).grid(row=1, column=3, rowspan=3)

        self.main = self.interface.mainloop()

    def entryget(self):
        hosget = self.host.get()
        nameget = self.name.get()
        passwordget = self.password.get()
        try:
            m1.c1 = {'host' : f'{hosget}', 'user' : f'{nameget}', 'password' : f'{passwordget}'}
            m1.one(**m1.c1)
            if hasattr(self, "interface"):
                self.interface.destroy()
            cycle()
        except Exception as e:
            if hasattr(self, "info_login"): 
                self.info_login.destroy()
            self.info_login = Label(self.frame, text="Please insert the dates correct!", fg="darkred")
            self.info_login.grid(row=4, column=2, pady=4)
            m1.logging.exception(e)
            raise e
        
class cycle:
    def __init__(self):
        self.interface = Tk()
        self.interface.title("GUI Options MYSQL")
        self.interface.geometry("400x535+754+170")
        self.interface.resizable(False, False)
        self.frame = LabelFrame(self.interface, border=0,)
        self.frame.grid(row=0, column=0, padx=10, pady=10)
        self.frame2 = LabelFrame(self.interface, border=0, relief="groove")
        self.frame2.grid(row=1, column=0, padx=10, pady=2)
        self.interface.iconbitmap(os.path.join(ima, "icon.ico"))
       

        self.image1 = ImageTk.PhotoImage(Image.open(os.path.join(ima, "1.png")).resize((300,300)))
        Label(master=self.frame, text="", image=self.image1).grid(row=0, column=1 , pady=50, padx=0)

        Label(master=self.frame, text=f"{'_'*40}",).grid(row=1, column=1 , pady=10, padx=0)

        self.options = {"CONSOLE" : winOPEN.console, 
                        "       " : winOPEN.space, 
                        "LOGS" : winOPEN.logs, 
                        "DATABASES - TABLES QUERY" : winOPEN.databases}
        ro = 0
        for values in self.options:
            obj = Button(
                self.frame2,
                text=values, 
                bd=0, 
                background="grey20", 
                highlightthickness=1,
                command= self.options[values],
                fg="grey100", 
                activebackground="grey70",
                activeforeground="white", width=25, 
            )
            ro += 1
            obj.grid(row=ro//3, column=ro%2, padx=2, pady=2,)
        self.interface.mainloop()

class windowsconsult:
    def console(self):
        windowsONE = Toplevel()
        windowsONE.title("CONSOLE")
        windowsONE.grab_set()
        windowsONE.resizable(0, 0)
        self.frame3 = LabelFrame(windowsONE, border=0)
        self.frame3.grid(row=0, column=0, padx=4, pady=4)

        def buttom1():
            try:
                self.labeltext.delete("1.0", END)
                obj = self.entrynew.get()
                ret_connect = m1.one(**m1.c1)
                ret = ret_connect.exx(obj)
                for i in ret:
                    self.labeltext.insert(END,  i)
                    self.labeltext.insert(END, "\n")
                try:
                    obj.lower()
                    ret2 = obj.split()
                    ret_connect = m1.one(**m1.c1)
                    obj2 = ret_connect.show()
                    for i in obj2:
                        if ret2[2] in i[0]:
                            self.labeltext.insert(END, f"The consult '{obj}' has realized\n")
                        else:
                            self.labeltext.insert(END, f"The consult '{obj}' has realized\n")
                            break
                except:
                    pass
                self.labeltext2.configure(text=f"ROWS OR REGISTER FOR CONSULT: - {len(ret)} -")
            except:
                pass

        self.entrynew = Entry(self.frame3,  border=0, font=("default", 12), width=80, fg="white", background="grey24", highlightbackground="grey50", highlightcolor="grey50", highlightthickness=1,)
        self.entrynew.insert(0, "Insert a consult sql here")
        self.entrynew.bind("<Button-1>", lambda push: self.entrynew.delete(0, END))
        self.entrynew.grid(row=0, column=0, pady=2, padx=4)
                
        self.buttom1 = Button(self.frame3, text="CONSULT SQL", bd=0, background="grey20", highlightthickness=1, fg="grey100", activebackground="grey70", activeforeground="white", height=1, width=18, command=buttom1).grid(row=0, column=1, padx=4)
        self.labeltext = Text(self.frame3, width=112, height=30, font=("default", 12), background="grey24", fg="white")
        self.labeltext.grid(row=1, column=0, columnspan=4, padx=5, pady=5)
        self.labeltext2 = Label(self.frame3, text="ROWS OR REGISTER FOR CONSULT: - # -")
        self.labeltext2.grid(row=2, column=0, columnspan=4)

        def deletedtext():
            self.labeltext.delete("1.0", END)        
            self.labeltext2.configure(text=f"ROWS OR REGISTER FOR CONSULT: - # -")

        self.buttom2 = Button(self.frame3, text="DELETE CONSULT", bd=0, background="grey20", highlightthickness=1, fg="grey100", activebackground="grey70", activeforeground="white", height=1, width=18, command=deletedtext).grid(row=0, column=2, padx=2)

    def space(self):
        pass
        """windowsTWO = Toplevel()
        windowsTWO.title("SPACE")"""
    
    def logs(self):
        windowsTHREE = Toplevel()
        windowsTHREE.title("LOGS")
        
        self.viewlog = Text(windowsTHREE, width=70, height=30, font=("default", 12), background="grey24", fg="white")
        self.viewlog.grid(row=0, column=0)
        viewlog_scroll_y = Scrollbar(windowsTHREE, command=self.viewlog.yview, width=20)
        viewlog_scroll_y.grid(row=0, column=1, sticky="NS")
        self.viewlog.config(yscrollcommand=viewlog_scroll_y.set)
        
        def return_err():
            try:
                with open(f"{m1.dirlog}/viewlog.txt") as opened:
                    self.viewlog.insert(END, f"{opened.read()}")
            except Exception as e:
                m1.logging.exception(e)
                raise e

        catch = Button(windowsTHREE, command=return_err, text="VIEW ALL LOGS", bd=0, background="grey20", highlightthickness=1, fg="grey100", activebackground="grey70", activeforeground="white", height=1, width=50,)
        catch.grid(row=1, column=0)

    def databases(self):
        windowsFOUR = Toplevel()
        windowsFOUR.title("DATABASES AND TABLES")
        windowsFOUR.resizable(0, 0)
        windowsFOUR.geometry("+9+316")

        def glo(): 
            try:
                if hasattr(self, "menuframe3"):
                        self.menuframe3.place_forget()
                        self.menuframe4.place_forget()
                        self.menuframe5.place_forget()
                        self.menuframe8.place_forget()
                        self.menuframe9.place_forget()
                if hasattr(self, "menuframe4"):
                        self.menuframe3.place_forget()
                        self.menuframe4.place_forget()
                        self.menuframe5.place_forget()
                        self.menuframe8.place_forget()
                        self.menuframe9.place_forget()
                if hasattr(self, "menuframe5"):
                        self.menuframe3.place_forget()
                        self.menuframe4.place_forget()
                        self.menuframe5.place_forget()
                        self.menuframe8.place_forget()
                        self.menuframe9.place_forget()
                if hasattr(self, "menuframe8"):
                        self.menuframe3.place_forget()
                        self.menuframe4.place_forget()
                        self.menuframe5.place_forget()
                        self.menuframe8.place_forget()
                        self.menuframe9.place_forget()
                if hasattr(self, "menuframe9"):
                        self.menuframe3.place_forget()
                        self.menuframe4.place_forget()
                        self.menuframe5.place_forget()
                        self.menuframe8.place_forget()
                        self.menuframe9.place_forget()
            except:
                pass
            finally:
                status()
        
        #--------------------------------------------------------------------
        #------------------- SHOW DATABASES TOP WINDOWS ---------------------
        #------------------- TOP LEVEL 1-------------------------------------
        windowsFOUR_1 = Toplevel()
        windowsFOUR_1.title("DATABASES")
        windowsFOUR_1.resizable(0,0)
        windowsFOUR_1.geometry("+1167+314")
        self.tv2 = ttk.Treeview(windowsFOUR_1, height=7,)
        self.tv2.heading("#0", text="LIST DATABASES")
        self.tv2.grid(row=0, column=0, padx=0, pady=0)
        self.scroll_ydb = Scrollbar(windowsFOUR_1, command=self.tv2.yview, width=20)
        self.scroll_ydb.grid(row=0, column=1, padx=0, pady=0, sticky="NS",)
        self.tv2.config(yscrollcommand=self.scroll_ydb.set)
        
            #GET OR SHOW DATABASES IN MINI TOP WINDOWS
        def win():
                glo()
                for i in self.tv2.get_children():
                    self.tv2.delete(i)
                self.c =  m1.one(**m1.c1)
                v = self.c.show()
                count = 0
                for x in v:
                    v2 = self.tv2.insert("", END, text=f"{count}-{x[0]}")
                    count +=1
        self.butomF = Button(windowsFOUR_1, text="RESET/CONSULT DATABASES", bd=0, background="grey20", highlightthickness=1, fg="grey100", activebackground="grey70", activeforeground="white", height=1, width=31, command=win)
        self.butomF.grid(row=1, column=0, padx=0, pady=0, columnspan=4)
        #-----------------------------------------------------------------------
        #-----------------------------------------------------------------------
        #-----------------------------------------------------------------------
        
        #-----------------------------------------------------------------------
        #------------------- SHOW TABLES OF TABLES SELECTED --------------------
        #------------------- TOP LEVEL 2----------------------------------------
        self.usewindows = Toplevel()
        self.usewindows.title("INFO COLUMNS OF TABLE")
        self.usewindows.resizable(0,0)
        self.usewindows.geometry("+632+316")

        self.menuframe10 = Menubutton(self.usewindows, text="EDIT", activeforeground='white', activebackground='grey24')
        self.menuframe10.grid(row=0, column=0, sticky="W", padx=0, pady=0)

        def alter_table():
             glo()
             windows_altertable = Toplevel()
             windows_altertable.title("ALTER TABLE")
             windows_altertable.resizable(0, 0)
            
             windows_altertable1 = LabelFrame(windows_altertable, bd=1)
             windows_altertable1.grid(row=0, column=0, padx=4, pady=4, ipadx=2, ipady=2, sticky="WE")

             infofield = Label(windows_altertable1, text="NAME COLUMN")
             infotype = Label(windows_altertable1, text="TYPE")
             infoprikey = Label(windows_altertable1, text="PRIMARY KEY")
             infocontraint = Label(windows_altertable1, text="CONSTRAINT")
             infoforeign = Label(windows_altertable1, text="FOREIGN KEY")
             inforeferences = Label(windows_altertable1, text="REFERENCES")
            
             infofield.grid(row=0, column=0, sticky="E")
             infotype.grid(row=0, column=1, sticky="E")
             infoprikey.grid(row=0, column=2, sticky="E")
             infocontraint.grid(row=2, column=0, sticky="E")
             infoforeign.grid(row=2, column=1, sticky="E")
             inforeferences.grid(row=2, column=2, sticky="E")
            
             field = Entry(windows_altertable1, border=0, font=("default", 12), width=18, fg="grey80", background="grey24", highlightbackground="grey50", highlightcolor="grey50", highlightthickness=1,)
             typefield = Entry(windows_altertable1, border=0, font=("default", 12), width=18, fg="grey80", background="grey24", highlightbackground="grey50", highlightcolor="grey50", highlightthickness=1,)
             prikey = Entry(windows_altertable1, border=0, font=("default", 12), width=18, fg="grey80", background="grey24", highlightbackground="grey50", highlightcolor="grey50", highlightthickness=1,)
             constraint = Entry(windows_altertable1, border=0, font=("default", 12), width=18, fg="grey80", background="grey24", highlightbackground="grey50", highlightcolor="grey50", highlightthickness=1,)
             foreign = Entry(windows_altertable1, border=0, font=("default", 12), width=18, fg="grey80", background="grey24", highlightbackground="grey50", highlightcolor="grey50", highlightthickness=1,)
             references = Entry(windows_altertable1, border=0, font=("default", 12), width=18, fg="grey80", background="grey24", highlightbackground="grey50", highlightcolor="grey50", highlightthickness=1,)
            
             field.grid(row=1, column=0)
             typefield.grid(row=1, column=1)
             prikey.grid(row=1, column=2)
             constraint.grid(row=3, column=0,)
             foreign.grid(row=3, column=1,)
             references.grid(row=3, column=2,)
            
             def entryadd_data2():
                fi = f" {field.get()}"
                ty = f" {typefield.get()}"
                pk = f" PRIMARY KEY {prikey.get()}"
                co1 = f" CONTRAINT {constraint.get()}"
                fo1 = f" FOREIGN KEY {foreign.get()}"
                ref1 = f" REFERENCES {references.get()}"
                create = ""

                try:
                    while True:
                            create = label_view_added_tex1.get()
                            if len(fi) >= 2 or len(ty) >= 2:
                                create += f"{fi}{ty}\n" 
                            if len(co1) >= 12:
                                create += f"{co1}"
                            if len(fo1) >= 14:
                                create += f"{fo1}"
                            if len(ref1) >= 13:
                                create += f"{ref1}"
                            if len(pk) >= 14:
                                create += f"{pk}"
                            label_view_added_tex1.set(f"{create}") 
                            break            
                except: 
                    pass
        
             def reset_entryadd_data2():
                label_view_added_tex1.set("")
            
             buttonreset = Button(windows_altertable1, text="RESET VISUALIZATION", bd=0, background="grey20", highlightthickness=1, fg="grey100", activebackground="grey70", activeforeground="white", height=1, width=20, command=reset_entryadd_data2)
             buttonadd = Button(windows_altertable1, text="ADD VISUALIZATION",  bd=0, background="grey20", highlightthickness=1, fg="grey100", activebackground="grey70", activeforeground="white", height=1, width=20, command=entryadd_data2)
             buttonadd.grid(row=5, column=1, sticky="W", pady=5)
             buttonreset.grid(row=5, column=0, sticky="W", padx=5, pady=5)

             windows_altertable2 = LabelFrame(windows_altertable, bd=1, text=f"SYNTAX  -  ALTER TABLE: {m1.used2['values'][0]}")
             windows_altertable2.grid(row=2, column=0, padx=4, pady=4, ipadx=4, ipady=4, sticky="WE")

             label_view_added_tex1 = StringVar()
             label_view_added = Label(windows_altertable2, fg="darkred", font=("default", 11),textvariable=label_view_added_tex1, anchor="w")
             label_view_added.grid(row=1, column=1, sticky="W")

             windows_altertable3 = LabelFrame(windows_altertable, bd=0)
             windows_altertable3.grid(row=3, column=0, padx=4, pady=4, ipadx=4, ipady=4, sticky="W")

             def add():
                sql = f"ADD {label_view_added_tex1.get()}".lower()
                print(sql)
                self.c = m1.one(**m1.c1)
                self.c.alter_table(sql)
             def drop():
                sql = f"DROP COLUMN {label_view_added_tex1.get()}".lower()
                self.c = m1.one(**m1.c1)
                self.c.alter_table(sql)
             def modify():
                sql = f"MODIFY COLUMN {label_view_added_tex1.get()}".lower()
                self.c = m1.one(**m1.c1)
                self.c.alter_table(sql)
             
             entryadd = Button(windows_altertable3, command=add, text="ADD",  bd=0, background="grey20", highlightthickness=1, fg="grey100", activebackground="grey70", activeforeground="white", height=1, width=15,)
             entrydrop = Button(windows_altertable3, command=drop, text="DROP",  bd=0, background="grey20", highlightthickness=1, fg="grey100", activebackground="grey70", activeforeground="white", height=1, width=15,)
             entrymodify = Button(windows_altertable3, command=modify, text="MODIFY",  bd=0, background="grey20", highlightthickness=1, fg="grey100", activebackground="grey70", activeforeground="white", height=1, width=15,)
             
             entryadd.grid(row=0, column=0, padx=5)
             entrydrop.grid(row=0, column=1, padx=5)
             entrymodify.grid(row=0, column=2,padx=5)

        self.menu10 = Menu(self.menuframe10, tearoff=0, bd=0,)
        self.menu10.add_command(label="ALTER TABLE", command=alter_table, hidemargin=False, activeforeground='white', activebackground='grey24')
        self.menuframe10.config(menu=self.menu10)

            #TREEVIEW FOR LIST TABLES FROM DATABASES
        self.tv3 = ttk.Treeview(self.usewindows, columns=("TYPE","NULL","KEY","DEFAULT","EXTRA"), height=12)
            #ROWS
        self.one1 = self.tv3.heading("#0", text="FIELD")
            #VALUES IN ROWS
        self.two1 = self.tv3.heading("TYPE", text="TYPE")
        self.tree1 = self.tv3.heading("NULL", text="NULL")
        self.four1 = self.tv3.heading("KEY",  text="KEY")
        self.five1 = self.tv3.heading("DEFAULT", text="DEFAULT")
        self.six1 = self.tv3.heading("EXTRA", text="EXTRA")
            #CONFIGURE WIDTH
        self.one1 = self.tv3.column("#0", width=120)
        self.two1 = self.tv3.column("TYPE", width=90)
        self.tree1 = self.tv3.column("NULL", width=60)
        self.four1 = self.tv3.column("KEY",  width=60)
        self.five1 = self.tv3.column("DEFAULT", width=60)
        self.six1 = self.tv3.column("EXTRA", width=120)
            #OPTION TREEVIEW TABLES
        self.tv3.grid(row=1, column=0, padx=0, pady=0)
        self.scroll_a = Scrollbar(self.usewindows, command=self.tv3.yview, width=20)
        self.scroll_a.grid(row=1, column=1, padx=0, pady=0, sticky="NS",)
        self.tv3.config(yscrollcommand=self.scroll_a.set)
            #LABEL
        self.usedtext2 = Label(self.usewindows, text=f"{':'*42}", fg="darkred")
        self.usedtext2.grid(row=2, column=0, padx=2, pady=2)
            #MENU EVENT
        self.menuframe4 = Menubutton(self.tv3, text="USE TABLE", activeforeground='white', activebackground='grey24',)
            #EVENTS TV3
        def tv3_selection_b3(e):
            glo()
            self.menuframe4.place(x=e.x, y=e.y)
        def tv3_selection_b1():
            glo()
        def tv3_copy():
            glo()
            windowsFOUR.clipboard_clear()
            values = self.tv3.item(self.tv3.focus(), "values")
            field = self.tv3.item(self.tv3.focus(), "text")
            windowsFOUR.clipboard_append(f"FIELD: {field}, TYPE: {values[0]}, NULL: {values[1]}, KEY: {values[2]}, DEFAULT: {values[3]}, EXTRA: {values[4]}")
        
        self.menupop1 = Menu(self.menuframe4, tearoff=0)
        self.menupop1.add_command(label="COPY ROW", activeforeground='white', activebackground='grey24',command=tv3_copy)
        self.menuframe4.config(menu=self.menupop1)  

        self.tv3.bind("<Button-1>", lambda e: tv3_selection_b1)
        self.tv3.bind("<Button-3>", lambda e: tv3_selection_b3(e))
        #--------------------------------------------------------------------
        #--------------------------------------------------------------------
        #--------------------------------------------------------------------

        #--------------------------------------------------------------------
        #----------------------- SELECT * FORM TABLE ------------------------
        #----------------------------TOP LEVEL 3-----------------------------
        self.usewindows1 = Toplevel()
        self.usewindows1.title("COLUMNS AND RECORDS")
        self.usewindows1.geometry("+0+0")
        self.usewindows1.resizable(0,0)
        self.usewindows1.columnconfigure(0, weight=1)
        self.usewindows1.columnconfigure(1, weight=0)
        self.usewindows1.rowconfigure(0, weight=1)
        self.usewindows1.rowconfigure(1, weight=0)
        self.usewindows1.rowconfigure(2, weight=1)
            #TOP MENU
        self.menuframe6 = Menubutton(self.usewindows1, text="EDIT", activeforeground='white', activebackground='grey24')
        self.menuframe6.grid(row=0, column=0, sticky="W", padx=0, pady=0)
        self.menuframe7 = Menubutton(self.usewindows1, text="VIEW", activeforeground='white', activebackground='grey24')
        self.menuframe7.grid(row=0, column=0, sticky="W",padx=50, pady=0)

        def tv4_buttom_selected():
            glo()

            if len(m1.where) >= 1:
                try:
                    for i in self.tv4.get_children():
                        self.tv4.delete(i)

                    self.infocolumn_get = self.infocolumn.get()
                    sql3 = self.infocolumn_get[:-1]
                    #CHANGE THE COLUMNS ASSIGNED BEFORING OF tk.treeview(COLUMNS)[self.tv4]
                    #WITH THE GET IN self.infocolumn
                    self.tv4.heading("#0", text=f"{sql3.split()[0]}")
                    sql3 = sql3.split()[1:]
                    self.tv4.config(columns=(sql3))
                    for i in sql3:
                        self.tv4.heading(i, text=i)
                        
                    try:
                        sql3 = ",".join(self.infocolumn_get[:-1].split())
                        sql2 = f"{m1.used['values'][0]}"
                        self.c = m1.one(**m1.c1)
                        self.colum2 = self.c.select_columns_fetch(sql2, sql3, m1.ft["number"])
                        count = 0
                        for i in self.colum2:
                            self.tv4.insert("", text=f"{i[0]}", values=i[1:], index=count)
                            count += 1
                    except Exception as e:
                        m1.logging.exception(e)
                        raise e
                
                    #This disable menu event 
                    """for i in self.tv4.winfo_children():
                        i.configure(state="disabled")"""
                except Exception as e:
                    m1.logging.exception(e)
                    raise e
                 
        def tv4_buttom_where():
            glo()
            windowswhere = Toplevel()
            windowswhere.title("WHERE CONSULT")
            windowswhere.resizable(0, 0)

            labelwhere = Label(windowswhere, font=("default", 11), text=f"WHERE {self.infocolumn.get().lower()[:-3]}")
            labelwhere.pack(padx=2, pady=2)

            def where():
                glo()
                if len(m1.where2) >= 1:
                    for i in self.tv4.get_children():
                        self.tv4.delete(i)

                    m1.columns1.clear()
                    m1.columns.clear()

                    self.c = m1.one(**m1.c1)
                    sql = m1.used["text"]
                    sql2 = f"{m1.used['values'][0]}"
                    self.c.show_columns_add(sql, sql2)
                    self.tv4.heading("#0", text=f"{m1.columns[0]}")
                    m1.columns1.extend(m1.columns)
                    m1.columns.pop(0)
                    self.tv4.config(columns=(m1.columns))
                    count = 0
                    columns_str = ""
                    for i in m1.columns:
                        columns_str += f"{i}"
                        self.tv4.heading(columns_str, text=columns_str)
                        columns_str = ""

                    try:
                        self.c = m1.one(**m1.c1)
                        sql3 = f"{self.infocolumn.get().lower()[:-3]} {entrywhere.get().lower()}"
                        """sql = m1.used["text"]"""
                        sql2 = f"{m1.used['values'][0]}"
                        self.colum2 = self.c.where(sql2, sql3, m1.ft["number"])
                        count = 0
                        for i in self.colum2:
                                self.tv4.insert("", text=f"{i[0]}", values=i[1:], index=count)
                                count += 1
                    except Exception as e:
                        raise e
                    finally:
                        self.infocolumn.delete(0, END)
                        self.infocolumn.insert(0, "Here view columns selected")
                        windowswhere.destroy()
                
            
            entrywhere = Entry(windowswhere, border=0, font=("default", 12), width=41, fg="grey60", highlightbackground="grey50", highlightcolor="grey50", highlightthickness=1,)  
            entrywhere.insert(0, "eg. > 20      or     eg. = name_table")      
            entrywhere.pack(padx=2, pady=2)
            buttonwhere = Button(windowswhere, bd=0, background="grey20", text="CONSULT", highlightthickness=1, fg="grey100", activebackground="grey70", activeforeground="white", height=1, width=53, command=where)
            buttonwhere.pack(padx=2, pady=2)

            # SEARCH
        self.infocolumn = Entry(self.usewindows1, font=("default", 12), border=0, width=28, state="normal", fg="grey35", highlightbackground="grey50", highlightcolor="grey50", highlightthickness=1,)
        self.infocolumn.insert(0, "Here view columns selected")
        self.infocolumn.grid(row=0, column=0, sticky="E", padx=320, pady=0)
        self.buttomcolumn_selected = Button(self.usewindows1, command=tv4_buttom_selected, text="SHOW COLUMNS SELECTED", bd=0, background="grey20", highlightthickness=1, fg="grey100", activebackground="grey70", activeforeground="white", height=1, width=25)
        self.buttomcolumn_where = Button(self.usewindows1, command=tv4_buttom_where, text="WHERE", bd=0, background="grey20", highlightthickness=1, fg="grey100", activebackground="grey70", activeforeground="white", height=1, width=18)
        self.buttomcolumn_where.grid(row=0, column=0, sticky="E", padx=183, pady=0)
        self.buttomcolumn_selected.grid(row=0, column=0, sticky="E", padx=0, pady=0)

        def tv4_insertrecord():
            windowsinsert = Toplevel()
            windowsinsert.title("INSERT VALUES INTO COLUMNS")
            windowsinsert.resizable(0, 0)
            glo()


            def gettext_AND_columns():
                obj = textentry.get("1.0", END).lower().splitlines()
                for i in obj:
                    a = literal_eval(i)
                    m1.val.append(a)
                obj2 = entrycolumns.get().split(",")
                pq = ""
                for i in obj2:
                    i
                    pq += "%s,"
                sql2 = pq[:-1]
                sql = entrycolumns.get().lower() 
                try:
                    self.c = m1.one(**m1.c1)
                    self.c.insert_record(sql, sql2)
                except:
                    pass
     
            labelcolumns = Label(windowsinsert, text="NAME COLUMNS TO USE", font=("default", 10))
            entrycolumns = Entry(windowsinsert, border=0,  font=("default", 12), width=80, fg="grey50", highlightbackground="grey50", highlightcolor="grey50", highlightthickness=1)
            entrycolumns.insert(0, ", ".join(m1.columns1[0:]))
            labelcolumns.grid(row=0, column=0, padx=0, sticky="W")
            entrycolumns.grid(row=1, column=0, padx=0, pady=0, sticky="W")

            labelvalues = Label(windowsinsert, text="VALUES TO INSERT", font=("default", 10))
            textentry = Text(windowsinsert, bd=0, font=("default", 12), width=80, fg="grey50", highlightbackground="grey50", highlightcolor="grey50", highlightthickness=1,)
            textentry.insert("1.0", "EACH STATEMENT OR RECORD WITH PARENTIS AND EACH ROW OF COLUMN SEPARATE WITH ' ' AND COMMA - EXAMPLE: ('1', 'PENELOPE', 'GUINESS', '2006-02-15 04:34:33')")
            textentry.grid(row=3, column=0, padx=0, pady=0, sticky="W")
            labelvalues.grid(row=2, column=0, sticky="W", pady=0)

            scrollbartext = Scrollbar(windowsinsert, command=textentry.yview, width=18)
            scrollbartext.grid(padx=0, pady=0, row=3, column=1, sticky="NSE")
            textentry.configure(yscrollcommand=scrollbartext.set)
            buttoninto = Button(windowsinsert, text="INSERT VALUES", font=("default", 10), command=gettext_AND_columns, bd=0, background="grey20", highlightthickness=1, fg="grey100", activebackground="grey70", activeforeground="white", height=1, width=92)
            buttoninto.grid(row=4, column=0, columnspan=4,padx=0, pady=0)
    
        def tv4_truncate():
            glo()
            change = messagebox.askyesno("CONTINUE TO TRUNCATE", "Do you want continue to Truncate this ?")
            if change == True:
                sql = m1.used["text"]
                sql2 = f"{m1.used['values'][0]}"
                self.c = m1.one(**m1.c1)
                self.c.truncate(sql, sql2)
                tv4_resettable()
            else:
                pass

        def tv4_resettable():
            glo()

            for i in self.tv4.get_children():
                self.tv4.delete(i)

            m1.columns1.clear()
            m1.columns.clear()

            """for i in m1.columns:
                self.tv4.heading(i , text=i)"""
            
            self.c = m1.one(**m1.c1)
            sql = m1.used["text"]
            sql2 = f"{m1.used['values'][0]}"
            self.c.show_columns_add(sql, sql2)
            self.tv4.heading("#0", text=f"{m1.columns[0]}")
            m1.columns1.extend(m1.columns)
            m1.columns.pop(0)
            self.tv4.config(columns=(m1.columns))
            count = 0
            columns_str = ""
            for i in m1.columns:
                columns_str += f"{i}"
                self.tv4.heading(columns_str, text=columns_str)
                columns_str = ""

            try:
                self.c = m1.one(**m1.c1)
                sql = m1.used["text"]
                sql2 = f"{m1.used['values'][0]}"
                self.colum2 = self.c.show_all_from(sql, sql2, m1.ft["number"])
                count = 0
                for i in self.colum2:
                        self.tv4.insert("", text=f"{i[0]}", values=i[1:], index=count)
                        count += 1
            except:
                pass
            
        self.menu3 = Menu(self.menuframe6, tearoff=0, bd=0,)
        self.menu4 = Menu(self.menuframe7, tearoff=0, bd=0,)
        self.menu3.add_command(label="INSERT STATEMENT", command=tv4_insertrecord, hidemargin=False, activeforeground='white', activebackground='grey24')
        self.menu3.add_separator()
        self.menu3.add_command(label="TRUNCATE", hidemargin=False, command=tv4_truncate, activeforeground='white', activebackground='grey24')
        self.menu4.add_command(label="SEARCH", hidemargin=False,  activeforeground='white', activebackground='grey24')
        self.menu4.add_separator()
        self.menu4.add_command(label="RESET TABLE", hidemargin=False, command=tv4_resettable, activeforeground='white', activebackground='grey24')
        self.menuframe6.config(menu=self.menu3,)
        self.menuframe7.config(menu=self.menu4,)

            #TREEVIEW FOR LIST TABLES FROM DATABASES
        self.tv4 = ttk.Treeview(self.usewindows1)
        self.tv4.grid(row=1, column=0, padx=0, pady=0, sticky="W")
        self.scroll_b = Scrollbar(self.usewindows1, command=self.tv4.yview, width=20)
        self.scroll_b.grid(row=1, column=1, padx=0, pady=0, sticky="NS",)
        self.scroll_b_x = Scrollbar(self.usewindows1, command=self.tv4.xview, width=20, orient="horizontal")
        self.scroll_b_x.grid(row=2, column=0, padx=0, pady=0, sticky="WE")
        self.tv4.config(yscrollcommand=self.scroll_b.set)
        self.tv4.config(xscrollcommand=self.scroll_b_x.set)

            #MENU EVENT
        self.menuframe5 = Menubutton(self.tv4, text="USE RECORD", activeforeground='white', activebackground='grey24',)
        self.menuframe8 = Menubutton(self.tv4, text="SELECT COLUMN", activeforeground='white', activebackground='grey24',)

            #EVENTS TV4
        def tv4_selection_b3(e):
            glo()
            self.region = self.tv4.identify_region(e.x, e.y)
            if self.region == "heading":
                self.menuframe8.place(x=e.x, y=e.y)

                def tv4_selection_b3_1():
                    glo()
                    self.string = self.tv4.identify_column(e.x)
                    self.string = int(self.string[1:])
                    m1.where.append(m1.columns1[self.string])
                    self.infocolumn.delete(0, END)
                    for i in m1.where:
                        self.infocolumn.insert(END,  f"{i[0:]} ")

                def tv4_selection_b3_2():
                    glo()
                    self.string = self.tv4.identify_column(e.x)
                    self.string = int(self.string[1:])
                    m1.where2.append(m1.columns1[self.string])
                    self.infocolumn.delete(0, END)
                    if len(m1.where2) >= 2 and len(self.infocolumn.get()) != 26:
                        for i in m1.where2:
                            self.infocolumn.insert(END,  f" {i[0:]} AND")
                    else:
                        for i in m1.where2:
                            self.infocolumn.insert(0,  f"{i[0:]} AND")
            else:
                m1.where2 = []
                m1.where = []
                self.menuframe5.place(x=e.x, y=e.y)
                self.infocolumn.delete(0, END)
                self.infocolumn.insert(0, "Here view columns selected")
                

            self.menupop3 = Menu(self.menuframe8, tearoff=0)
            self.menupop3.add_command(label="USE COLUMN", activeforeground='white', activebackground='grey24', command=lambda: tv4_selection_b3_1())
            self.menupop3.add_command(label="WHERE", activeforeground='white', activebackground='grey24', command=lambda: tv4_selection_b3_2())
            self.menuframe8.config(menu=self.menupop3)

        def tv4_selection_row(e):
            glo()
            self.region = self.tv4.identify_region(e.x, e.y)
            if not self.region == "heading":
                m1.where = []
                m1.where2 = []
                self.infocolumn.delete(0, END)
                self.infocolumn.insert(0, "Here view columns selected")
            else:
                pass
            
        def tv4_copy():
            glo()
            windowsFOUR.clipboard_clear()
            values = self.tv4.item(self.tv4.focus(), "values")
            id_name = self.tv4.item(self.tv4.focus(), "text")
            windowsFOUR.clipboard_append(f" COLUMNS: {m1.columns1[0:]} \n ROWS: {id_name},{values[0:]}")
        
        def tv4_deletefrom():
            glo()
            change1 = messagebox.askyesno("CONTINUE TO DROP RECORD", "Do you want continue to DROP this Record?")
            if change1 == True:
                id_name = self.tv4.item(self.tv4.focus(), "text")
                self.c = m1.one(**m1.c1)
                self.c.delete_from(sql=f"{m1.columns1[0]}", sql2=f"{id_name}")
                self.tv4.delete(self.tv4.focus())
                
        self.menupop2 = Menu(self.menuframe5, tearoff=0)
        self.menupop2.add_command(label="COPY RECORD", activeforeground='white', activebackground='grey24',command=tv4_copy)
        self.menupop2.add_command(label="DELETE RECORD", activeforeground='white', activebackground='grey24',command=tv4_deletefrom)
        self.menuframe5.config(menu=self.menupop2)
        
        self.tv4.bind("<Button-3>", lambda e: tv4_selection_b3(e))
        self.tv4.bind("<Button-1>", lambda e: tv4_selection_row(e))
        #---------------------------------------------------------------------
        #---------------------------------------------------------------------
        #---------------------------------------------------------------------


        #----------------------------------------------------------------------
        #------------------ SHOW DATABASEES AND TABLES ------------------------
        #----------------------------TOP LEVEL 0-------------------------------
            #IMAGES
        self.iconsearch = Image.open(os.path.join(ima, "search.png")).resize((30,30))
        self.iconsearch = ImageTk.PhotoImage(self.iconsearch)
        self.iconcon = Image.open(os.path.join(ima, "conne.png")).resize((10,10))
        self.iconcon = ImageTk.PhotoImage(self.iconcon)
        self.icondis = Image.open(os.path.join(ima, "disco.png")).resize((10,10))
        self.icondis = ImageTk.PhotoImage(self.icondis)
            #SEARCH
        def forsearch():
                glo()
                getrecord = self.searchdb.get().lower()
                for i in self.tv.get_children():
                    self.tv.delete(i)
        
                self.c = m1.one(**m1.c1)
                v1 = self.c.db_inside(getrecord)
                for (a , b) in v1:
                    self.tv.insert("", END, text=f"{a}", values=f"{b}")
              
        self.searchdb = Entry(windowsFOUR, font=("default", 12), border=0, width=28, state="normal", fg="grey35", highlightbackground="grey50", highlightcolor="grey50", highlightthickness=1,)
        self.searchdb.insert(0, "Write a database to search")
        self.searchdb.grid(row=0, column=0, sticky="E", padx=40, pady=0)
        self.buttom_search = Button(windowsFOUR, text="SEARCH", image=self.iconsearch, border=0, command=forsearch)
        self.buttom_search.grid(row=0, column=0, sticky="E", padx=2, pady=0)
            #FRAME FOR MENU OPTIONS
        self.menuframe1 = Menubutton(windowsFOUR, text="EDIT", activeforeground='white', activebackground='grey24')
        self.menuframe1.grid(row=0, column=0, sticky="W", padx=0, pady=0)
        self.menuframe2 = Menubutton(windowsFOUR, text="VIEW", activeforeground='white', activebackground='grey24')
        self.menuframe2.grid(row=0, column=0, sticky="W",padx=40, pady=0)
            #CREATE TOPLEVEL OF MENU AND FUNTION
        def top_searchtreeview():
            glo()
            windows_search = Toplevel()
            windows_search.title("Search")
            infowin = Label(windows_search, text="SEARCH DATABASE")
            infowin.pack()
            getsearch = Entry(windows_search, border=0, font=("default", 12), width=25, fg="grey35", highlightbackground="grey50", highlightcolor="grey50", highlightthickness=1,)
            getsearch.insert(0, "write here a database or table")
            getsearch.pack(padx=5, pady=5)

            def forsearch():
                getrecord = getsearch.get().lower()
                for i in self.tv.get_children():
                    self.tv.delete(i)
                try:
                    self.c = m1.one(**m1.c1)
                    v1 = self.c.db_inside(getrecord)
                    for (a , b) in v1:
                        self.tv.insert("", END, text=f"{a}", values=f"{b}")
                except Exception as e:
                    raise e
            
            sendsearch = Button(windows_search, text="SEARCH", bd=0, background="grey20", highlightthickness=1, fg="grey100", activebackground="grey70", activeforeground="white", height=1, width=32, command=forsearch)
            sendsearch.pack(padx=2, pady=2)
        def top_reset():
            glo()
            for i in self.tv.get_children():
                    self.tv.delete(i)
            try:
                    self.c = m1.one(**m1.c1)
                    v1 = self.c.databases()
                    for (a , b) in v1:
                        self.tv.insert("", END, text=f"{a}", values=f"{b}")
            except Exception as e:
                raise e
        def top_drop():
            glo()
            windowsdrop = Toplevel()
            windowsdrop.title("Drop database")
            infowin = Label(windowsdrop, text="DROP DATABASE ")
            infowin.pack()
            getdatabase = Entry(windowsdrop, border=0, font=("default", 12), width=30, fg="grey35", highlightbackground="grey50", highlightcolor="grey50", highlightthickness=1,)
            getdatabase.insert(0, "write here a database existing")
            getdatabase.pack(padx=5, pady=5)

            def forconfirm():
                getrecord = getdatabase.get().lower()
                self.c = m1.one(**m1.c1)
                self.c.drop(getrecord)
                for i in self.tv.get_children():
                    self.tv.delete(i)
                top_reset()
                win()
            
            sendsearchb = Button(windowsdrop, text="DROP", bd=0, background="grey20", highlightthickness=1, fg="grey100", activebackground="grey70", activeforeground="white", height=1, width=38, command=forconfirm)
            sendsearchb.pack(padx=2, pady=2)
        def top_create():
            glo()
            windowscreate = Toplevel()
            windowscreate.title("Drop database")
            infowin = Label(windowscreate, text="CREATE DATABASE")
            infowin.pack()
            getdat = Entry(windowscreate, border=0, font=("default", 12), width=30, fg="grey35", highlightbackground="grey50", highlightcolor="grey50", highlightthickness=1,)
            getdat.insert(0, "write here a database existing")
            getdat.pack(padx=5, pady=5)

            def forcreate():
                getrecord = getdat.get().lower()
                for i in self.tv.get_children():
                    self.tv.delete(i)
                self.c = m1.one(**m1.c1)
                inputpara = self.c.newdatabase(getrecord)
                top_reset()
                win()
            
            sendsearchb = Button(windowscreate, text="CREATE", bd=0, background="grey20", highlightthickness=1, fg="grey100", activebackground="grey70", activeforeground="white", height=1, width=38, command=forcreate)
            sendsearchb.pack(padx=2, pady=2)

            #MENU PRINCIPAL FOR SEACH AND RESET TREEVIEW PRINCIPAL OF SHOW DATABASES AND TABLES
        def top_tabledb():
            glo()
            windowsdrop_table = Toplevel()
            windowsdrop_table.title("Drop table of a database")
            infowin1 = Label(windowsdrop_table, text=" 1 - USE DATABASE")
            infowin1.grid(row=0, column=0)
            infowin2 = Label(windowsdrop_table, text="2 - NAME TABLE")
            infowin2.grid(row=0, column=1)

            entrywin1 = Entry(windowsdrop_table, border=0, font=("default", 12), width=25, fg="grey35", highlightbackground="grey50", highlightcolor="grey50", highlightthickness=1,)
            entrywin1.insert(0, "write here database")
            entrywin1.grid(row=1, column=0, padx=2)
            entrywin2 = Entry(windowsdrop_table,  border=0, font=("default", 12), width=25, fg="grey35", highlightbackground="grey50", highlightcolor="grey50", highlightthickness=1,)
            entrywin2.insert(0, "write here the name table")
            entrywin2.grid(row=1, column=1, padx=2)

            def entrywin():
                win1 = entrywin1.get().lower()
                win2 = entrywin2.get().lower()

                self.c = m1.one(**m1.c1)
                self.v4 = self.c.usedb_deletetable(win1,win2)
                top_reset()

            sendsearch = Button(windowsdrop_table, text="DROP TABLE ON DATABASE SELECTED", bd=0, background="grey20", highlightthickness=1, fg="grey100", activebackground="grey70", activeforeground="white", height=1, width=65, command=entrywin)
            sendsearch.grid(row=2, column=0, padx=2, pady=2, columnspan=2)
        def top_create_table():
            glo()
            windows_create_table = Toplevel()
            windows_create_table.title("CREATE TABLE")
            windows_create_table.resizable(0, 0)
            
            windows_create_tableframe1 = LabelFrame(windows_create_table, bd=1)
            windows_create_tableframe1.grid(row=0, column=0, padx=4, pady=4, ipadx=2, ipady=2, sticky="WE")

            infofield = Label(windows_create_tableframe1, text="NAME")
            infotype = Label(windows_create_tableframe1, text="TYPE")
            infonull = Label(windows_create_tableframe1, text="NULL")
            infokey = Label(windows_create_tableframe1, text="KEY")
            infodefault = Label(windows_create_tableframe1, text="DEFAULT")
            infoextra= Label(windows_create_tableframe1, text="EXTRA")
            infocontraint = Label(windows_create_tableframe1, text="CONSTRAINT")
            infoforeign = Label(windows_create_tableframe1, text="FOREIGN KEY")
            inforeferences = Label(windows_create_tableframe1, text="REFERENCES")
            
            infofield.grid(row=0, column=0, sticky="E")
            infotype.grid(row=0, column=1, sticky="E")
            infonull.grid(row=0, column=2, sticky="E")
            infokey.grid(row=0, column=3, sticky="E")
            infodefault.grid(row=0, column=4, sticky="E")
            infoextra.grid(row=0, column=5, sticky="E")
            infocontraint.grid(row=2, column=0, sticky="E")
            infoforeign.grid(row=2, column=1, sticky="E")
            inforeferences.grid(row=2, column=2, sticky="E")
            
            field = Entry(windows_create_tableframe1, border=0, font=("default", 12), width=18, fg="grey80", background="grey24", highlightbackground="grey50", highlightcolor="grey50", highlightthickness=1,)
            typefield = Entry(windows_create_tableframe1, border=0, font=("default", 12), width=18, fg="grey80", background="grey24", highlightbackground="grey50", highlightcolor="grey50", highlightthickness=1,)
            null = Entry(windows_create_tableframe1, border=0, font=("default", 12), width=18, fg="grey80", background="grey24", highlightbackground="grey50", highlightcolor="grey50", highlightthickness=1,)
            key = Entry(windows_create_tableframe1, border=0, font=("default", 12), width=18, fg="grey80", background="grey24", highlightbackground="grey50", highlightcolor="grey50", highlightthickness=1,)
            default = Entry(windows_create_tableframe1, border=0, font=("default", 12), width=18, fg="grey80", background="grey24", highlightbackground="grey50", highlightcolor="grey50", highlightthickness=1,)
            extra = Entry(windows_create_tableframe1, border=0, font=("default", 12), width=18, fg="grey80", background="grey24", highlightbackground="grey50", highlightcolor="grey50", highlightthickness=1,)
            constraint = Entry(windows_create_tableframe1, border=0, font=("default", 12), width=18, fg="grey80", background="grey24", highlightbackground="grey50", highlightcolor="grey50", highlightthickness=1,)
            foreign = Entry(windows_create_tableframe1, border=0, font=("default", 12), width=18, fg="grey80", background="grey24", highlightbackground="grey50", highlightcolor="grey50", highlightthickness=1,)
            references = Entry(windows_create_tableframe1, border=0, font=("default", 12), width=18, fg="grey80", background="grey24", highlightbackground="grey50", highlightcolor="grey50", highlightthickness=1,)
            
            field.grid(row=1, column=0)
            typefield.grid(row=1, column=1)
            null.grid(row=1, column=2)
            key.grid(row=1, column=3)
            default.grid(row=1, column=4)
            extra.grid(row=1, column=5)
            constraint.grid(row=3, column=0,)
            foreign.grid(row=3, column=1,)
            references.grid(row=3, column=2,)
            
            def entryadd_data():
                fi = f" {field.get()}"
                ty = f" {typefield.get()}"
                nu = f" {null.get()}"
                k = f" {key.get()}"
                de = f" {default.get()}"
                ex = f" {extra.get()}"
                co = f" CONTRAINT {constraint.get()}"
                fo = f" FOREIGN KEY {foreign.get()}"
                ref = f" REFERENCES {references.get()}"
                create = ""
                try:
                    while True:
                        if len(fi) >= 2 or len(ty) >= 2 or len(nu) >= 2 or len(k) >= 2 or len(de) >= 2 or len(ex) >= 2:
                            create = label_view_added_text.get()
                            create += f"{fi}{ty}{nu}{k}{de}{ex},\n"
                            label_view_added_text.set(f"{create}")
                            if len(co) >= 12 or len(fo) >= 14 or len(ref) >= 13:
                                create += f"{co}{fo}{ref},\n"
                                label_view_added_text.set(f"{create}")
                            else:
                                pass
                            break
                        else:
                            pass
                        break
                except:
                    pass
        
            def reset_entryadd_data():
                label_view_added_text.set("")
            
            buttonreset = Button(windows_create_tableframe1, text="RESET", bd=0, background="grey20", highlightthickness=1, fg="grey100", activebackground="grey70", activeforeground="white", height=1, width=20, command=reset_entryadd_data)
            buttonadd = Button(windows_create_tableframe1, text="ADD",  bd=0, background="grey20", highlightthickness=1, fg="grey100", activebackground="grey70", activeforeground="white", height=1, width=20, command=entryadd_data)
            buttonadd.grid(row=4, column=5, sticky="E",)
            buttonreset.grid(row=4, column=4, sticky="E")

            windows_create_tableframe2 = LabelFrame(windows_create_table, bd=1, text="SYNTAX  -  CREATE TABLE TABLE_NAME")
            windows_create_tableframe2.grid(row=2, column=0, padx=4, pady=4, ipadx=4, ipady=4, sticky="WE")

            label_view_added_text = StringVar()
            label_view_added = Label(windows_create_tableframe2, fg="darkred", font=("default", 11),textvariable=label_view_added_text, anchor="w")
            label_view_added.grid(row=1, column=1, sticky="W")

            windows_create_tableframe3 = LabelFrame(windows_create_table, bd=0)
            windows_create_tableframe3.grid(row=3, column=0, padx=4, pady=4, ipadx=4, ipady=4, sticky="E")

            def send_alldates():
                glo()
                sql = entrydb.get().lower()
                sql2 = entrytable.get().lower()
                sql3 = label_view_added_text.get().lower().splitlines()
                sql3 = "".join(sql3)[:-1]
                self.c = m1.one(**m1.c1)
                self.c.create_table(sql, sql2, sql3)
                top_reset()

            entrydb = Entry(windows_create_tableframe3, border=0, font=("default", 12), width=18, fg="grey35", highlightbackground="grey50", highlightcolor="grey50", highlightthickness=1,)
            entrytable = Entry(windows_create_tableframe3, border=0, font=("default", 12), width=18, fg="grey35", highlightbackground="grey50", highlightcolor="grey50", highlightthickness=1,)
            labeldb = Label(windows_create_tableframe3, font=("default", 10), text="DATABASE")
            labeltable = Label(windows_create_tableframe3, font=("default", 10), text="TABLE TO CREATE")
            buttonadd_alldates = Button(windows_create_tableframe3, command=send_alldates, text="CREATE TABLE",  bd=0, background="grey20", highlightthickness=1, fg="grey100", activebackground="grey70", activeforeground="white", height=1, width=20,)

            labeldb.grid(row=0, column=0)
            labeltable.grid(row=0, column=3)
            buttonadd_alldates.grid(row=0, column=5, padx=2,)
            entrydb.grid(row=0, column=2, padx=2)
            entrytable.grid(row=0, column=4, padx=2)

        self.menu1 = Menu(self.menuframe1, tearoff=0, bd=0,)
        self.menu2 = Menu(self.menuframe2, tearoff=0, bd=0,)
        self.menu1.add_command(label="DROP DATABASE", hidemargin=False, command=top_drop, activeforeground='white', activebackground='grey24')
        self.menu1.add_command(label="CREATE DATABASE", hidemargin=False, command=top_create, activeforeground='white', activebackground='grey24')
        self.menu1.add_separator()
        self.menu1.add_command(label="CREATE TABLE", hidemargin=False, command=top_create_table, activeforeground='white', activebackground='grey24')
        self.menu1.add_command(label="DROP TABLE", hidemargin=False, command=top_tabledb,  activeforeground='white', activebackground='grey24')
        self.menu2.add_command(label="SEARCH DATABASE", hidemargin=False, command=top_searchtreeview,  activeforeground='white', activebackground='grey24')
        self.menu2.add_command(label="RESET TABLE", hidemargin=False, command=top_reset, activeforeground='white', activebackground='grey24')
        self.menuframe1.config(menu=self.menu1,)
        self.menuframe2.config(menu=self.menu2,)

            #FRAME PRINCIPAL WIDGET PAGE TABLES AND DATABASES
        self.frame7 = LabelFrame(windowsFOUR, bd=0)
        self.frame7.grid(row=2, column=0, padx=2, pady=2)
            #ADD A WIDGET FOR SCROLL TREEWIEW 
        self.scroll_y = Scrollbar(self.frame7, bd=0,)
        self.scroll_y.grid(row=0, column=1, sticky="NWSE")
            #CREATE A TREEVIEW FOR SHOW DATABASES AND TABLES
        self.tv = ttk.Treeview(self.frame7, columns=("TWO"), yscrollcommand=self.scroll_y.set,)
            #COLUMNS
        self.tv.column("#0", width=290)
        self.tv.column("TWO", width=290)
        self.oneco = self.tv.heading("#0", text="DATABASES", )
        self.twoco = self.tv.heading("TWO", text="TABLES", anchor="center",)
            #ROWS
        def rowl():
            glo()
            for i in self.tv.get_children():
                self.tv.delete(i)

            self.c = m1.one(**m1.c1)
            v1 = self.c.databases()
            for (a , b) in v1:
                self.tv.insert("", END, text=f"{a}", values=f"{b}")
  

            # CHANGE LIMIT ROWS FOR TV4 TREEVIEW
        def changelimit():
            glo()
            self.number = int(self.entrynumber.get())
            m1.ft["number"] = self.number

        self.scroll_y.config(command=self.tv.yview, width=20)
        self.tv.grid(row=0, column=0,)
            #THIS FRAME GOES TO SEPARATE THE FRAME 7 
        self.frame6 = LabelFrame(windowsFOUR, bd=0)
        self.frame6.grid(row=1, column=0, padx=2, pady=2)
        self.frame8 = LabelFrame(windowsFOUR, bd=0)
        self.frame8.grid(row=3, column=0, padx=2, pady=2)
        self.buttom3 = Button(self.frame6, text="PRESS HERE FOR SHOW DATABASES AND TABLES", bd=0, background="grey20", highlightthickness=1, fg="grey100", activebackground="grey70", activeforeground="white", height=1, width=75, command=rowl)
        self.buttom3.grid(row=0, column=0, padx=0, pady=2)

        def status():
            pass
            try:
                self.c = m1.one(**m1.c1)
                if self.c.torf() == True:
                    self.buttom_conne.config(image=self.iconcon)
                else:
                    pass
            except Exception as e:
                m1.logging.exception(e)
                self.buttom_conne.config(image=self.icondis)
                raise e

        self.buttom_conne = Button(self.frame6, command=status, text="STATUS ", image=self.iconcon, compound="right",fg="grey35", highlightbackground="grey50", highlightcolor="grey50", highlightthickness=1, width=60, bd=1, borderwidth=0)
        self.buttom_conne.grid(row=0, column=1, padx=0, pady=2)
        self.copyselected = Entry(self.frame7, border=0, font=("default", 12), width=67,fg="grey35", highlightbackground="grey50", highlightcolor="grey50", highlightthickness=1,)
        self.copyselected.insert(0, "Here does get any select from table")
        self.copyselected.grid(row=1, column=0, columnspan=2,padx=2, pady=2)
        self.entrynumber = Entry(self.frame8, border=0, font=("default", 12), width=25, fg="grey60", background="grey24", highlightbackground="grey50", highlightcolor="grey50", highlightthickness=1,)
        self.entrynumber.insert(0, f"{m1.ft['number']}")
        self.buttomnumber = self.buttom3 = Button(self.frame8, text="CHANGE LIMIT RECORD IN COLUMNS CONSULT", bd=0, background="grey20", highlightthickness=1, fg="grey100", activebackground="grey70", activeforeground="white", height=1, width=53, command=changelimit)
        self.entrynumber.grid(row=0, column=0, padx=2, pady=2)
        self.buttomnumber.grid(row=0, column=1, padx=2, pady=2)
            #CREATE A CALLBACK CLICKER AND ADD A EVENT MENU ON TREEVIEW SELF.TV
        self.menuframe3 = Menubutton(self.tv, text="USE TABLE", activeforeground='white', activebackground='grey24',)
            #EVENTS TV AND CALL FOR ITER TABLES IN TOPLEVELS TREEVIEWS
        def tv_selection_b3(e):
            glo()
            m1.used = {}
            m1.used = self.tv.item(self.tv.focus())
            m1.used2 = self.tv.item(self.tv.focus())
            self.menuframe3.place(x=e.x, y=e.y)
        
        def tv_selection_b1():
                used3 = self.tv.item(self.tv.focus())
                #"try and except " : bug when to try for first a event <button-1> return error in console
                try:
                    glo()
                    self.copyselected.delete(0, END)
                    self.copyselected.insert(0, f"DATABASE: {used3['text']} TABLE: {used3['values'][0]}")
                    used3 = {}
                except:
                    pass

        def tv3_itercolumns():
            glo()
            for i in self.tv3.get_children():
                self.tv3.delete(i)
    
            self.c = m1.one(**m1.c1)
            sql = m1.used2["text"]
            sql2 = f"{m1.used2['values'][0]}"
            self.colum = self.c.show_columns(sql, sql2)
            count = 0
            for i in self.colum:
                self.tv3.insert("", text=i[0], values=(i[1],i[2],i[3],i[4],i[5]), index=count)
                count += 1  

        def tv4_itercolumns():
            glo()

            for i in self.tv4.get_children():
                self.tv4.delete(i)
            m1.columns1.clear()
            m1.columns.clear()   
            #ADD COLUMNS TO tk.treeview(tv4) WITH m1.columns and m1.columns1
            self.c = m1.one(**m1.c1)
            sql = m1.used["text"]
            sql2 = f"{m1.used['values'][0]}"
            #HERE m1.columns CALL TO APPEND FOR LOAD COLUMNS FROM show_columns_add()
            self.c.show_columns_add(sql, sql2)
            #HERE THIS CONFIGURE OR ADD THE TEXT TO ONE COLUMN NUMBER ROOT "#0" 
            self.tv4.heading("#0", text=f"{m1.columns[0]}")
            #SAVE THE COLUMNS m1.columns IN m1.columns1 FOR DELETE THE ONE TEXT COLUMN ASSIGNATED IN "#0" BEFORE
            m1.columns1.extend(m1.columns)
            #m1.columns TO CEDED ITS COLUMNS SO DELETE THE ONE COLUMN OR NAME TEXT "#0" ROOT
            #WHEN ITERATE THE OTHERS NOT APPEND OR DUPLICATE THE NAME COLUMN #0 ASSIGNATED
            m1.columns.pop(0)
            #WE CONFIGURE HERE THE NEXT VIEWS ASSIGN OR SPACES RESERVED FOR LATER CONFIGURE THEM FOR ONE "HEAD (tk.treeview.heading)" OR ITERATING
            #WITH m1.columns.pop(0) FOR NOT GENERATE A SPACE INSIDE TABLE self.tv4
            self.tv4.config(columns=(m1.columns))
            #HERE CALL tk.treeview.heading AND A LIST m1.columns FOR ADD FOLLOW COLUMNS MISSING. AFTER #0
            #USE columns_str FOR GET m1.columns POSITION WITH FORMATE "string witout []"
            columns_str = ""
            for i in m1.columns:
                columns_str += f"{i}"
                # tk.treeview.heading (# - NAME OR ITEM COLUMN ASSIGNED (in tk.treeview(COLUMNS) or tk.treeview.config(COLUMNS))   ,  # - text = TEXT TO SHOW)
                self.tv4.heading(columns_str, text=columns_str)
                columns_str = ""

            #LATER GET A fetchmany() WITH show_all_from
            try:
                self.c = m1.one(**m1.c1)
                sql = m1.used["text"]
                sql2 = f"{m1.used['values'][0]}"
                self.colum2 = self.c.show_all_from(sql, sql2, m1.ft["number"])
                count = 0
                for i in self.colum2:
                        self.tv4.insert("", text=f"{i[0]}", values=i[1:], index=count)
                        count += 1
            except Exception as e:
                m1.logging.exception(e)
                raise e

        def tv_copyrow():
            glo()
            windowsFOUR.clipboard_clear()
            windowsFOUR.clipboard_append(f"DATABASE: {m1.used['text']} TABLE: {m1.used['values'][0]}")
                
        def backup_database():
            glo()
            namedb = self.tv.item(self.tv.focus(), "text")
            self.c = m1.one(**m1.c1)
            self.c.copydb(namedb)

        def upload():
            glo()
            windows_upload= Toplevel()
            windows_upload.title("UPLOAD DATABASE")
            getdatabase = Entry(windows_upload, border=0, font=("default", 12), width=25, fg="grey35", highlightbackground="grey50", highlightcolor="grey50", highlightthickness=1,)
            getdatabase.insert(0, "write here a database viewed")
            getdatabase.grid(row=0, column=0, padx=2, pady=2)

            def update():
                self.c = m1.one(**m1.c1)
                self.c.uploaddb(getdatabase.get().lower())
            
            sendupload = Button(windows_upload, text="UPLOAD", bd=0, background="grey20", highlightthickness=1, fg="grey100", activebackground="grey70", activeforeground="white", height=1, width=32, command=update)
            sendupload.grid(row=1, column=0, padx=2, pady=2)
            containerba = LabelFrame(windows_upload, text="VIEW ALL BACKUP")
            containerba.grid(row=2, column=0, padx=2, pady=2, sticky="WE")

            down = 0
            for i in os.listdir(m1.dirtwo):
                infowin = Label(containerba, text=f"{i}")
                infowin.grid(row=down, column=0, padx=2, pady=2, sticky="W")
                down += 1

        self.menupop = Menu(self.menuframe3, tearoff=0)   
        self.menupop.add_command(label="CONSULT COLUMNS", activeforeground='white', activebackground='grey24', command=tv3_itercolumns)
        self.menupop.add_command(label="CONSULT SELECT ALL ROW", activeforeground='white', activebackground='grey24', command=tv4_itercolumns)
        self.menupop.add_separator()
        self.menupop.add_command(label="UPLOAD DATABASE", activeforeground='white', activebackground='grey24', command=upload)
        self.menupop.add_command(label="BACKUP DATABASE", activeforeground='white', activebackground='grey24', command=backup_database)
        self.menupop.add_separator()
        self.menupop.add_command(label="COPY ROW", activeforeground='white', activebackground='grey24', command=tv_copyrow)
        self.menuframe3.config(menu=self.menupop)    

            #CALL EVENT MENU SELF.TV
        self.tv.bind("<Button-3>", lambda e: tv_selection_b3(e))
        self.tv.bind("<Button-1>", lambda e: tv_selection_b1())
        #-----------------------------------------------------------------------
        #-----------------------------------------------------------------------
        #-----------------------------------------------------------------------
        status()
#CALL THIS FOR ITERARION OPTIONS TOPLEVES IN "CYCLE()"
winOPEN = windowsconsult()

login()
import sqlite3
from tkinter import *
from tkinter import messagebox , simpledialog
from scores_A import *
import tkinter as tk 
import webbrowser
import smtplib
from email.mime.text import MIMEText
from tkinter import filedialog
import random
edit_window = None 
otp_int=None
image_path = None

root = Tk()
root.title("main window")
root.geometry("1600x900")
bg = Image.open(r"D:\Com\second\pyrhon\bas _score\new\first.png") 
photo = ImageTk.PhotoImage(bg)
Label(root,image=photo).place(x=0,y=0)
def open_information():
    info_window = tk.Toplevel()
    bg_image = tk.PhotoImage(file=r"D:\Com\second\pyrhon\bas _score\new\Infor\Bg_info.png")
    info_window.geometry("1600x900")
    bg_label = tk.Label(info_window, image=bg_image)
    bg_label.image = bg_image  # Keep a reference to the image
    bg_label.place(x=0, y=0)
    

    back_button_image = tk.PhotoImage(file=r"D:\Com\second\pyrhon\bas _score\new\Infor\Back.png")  # แทน path_to_your_image.png ด้วยที่อยู่ของไฟล์รูปของคุณ
    back_button = tk.Button(info_window, text="Back", command=info_window.destroy, image=back_button_image,highlightthickness=0, bd=0,bg="white")
    back_button.image = back_button_image
    back_button.place(x=100,y=50)
    
    
    info_button_image= tk.PhotoImage(file=r"D:\Com\second\pyrhon\bas _score\new\Infor\readmore.png")
    info_button = tk.Button(info_window, text="more info",command=more_info,image=info_button_image,highlightthickness=0, bd=0,bg="white")
    info_button.image = info_button_image
    info_button.place(x=320,y=600)


def more_info():
    file_path =r"D:\Com\second\pyrhon\bas _score\new\Web\inance-html\index.html"
    webbrowser.open(file_path, new=2)
# login menu
def open_login():
    login_window = Toplevel()
    login_window.title("LOGIN")
    login_window.geometry("1600x900")
    login_window_bg = Image.open(r'D:\Com\second\pyrhon\bas _score\logIN.png')
    photo = ImageTk.PhotoImage(login_window_bg)
    Label(login_window,image=photo).place(x=0,y=0)
    def validate_login():
        
        
        username = username_entry.get()
        password = password_entry.get()
        
        conn = sqlite3.connect('login.db')
        c = conn.cursor()
        
        c.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
        user = c.fetchone()
        
        
        if username == "admin" and password == "admin":
            print("admin")
            open_main()
            
            
            conn.close()
            
            
            
        elif user:
            print("Login successful")
            conn.close()
        
            
            
        else:
            messagebox.showinfo("Invalid Input", "Invalid username or password")
            conn.close()
            
        
        
  
    username_entry = tk.Entry(login_window,font='DBHelvethaicaX 40',width=29,bg="#313549",highlightthickness=0,fg="#e2e1e1",bd=0)
    username_entry.place(x=600,y=340,height=95)
    
    password_entry = tk.Entry(login_window, show="*",font='DBHelvethaicaX 40',width=29,bg="#313549",highlightthickness=0,fg="#e2e1e1",bd=0)
    password_entry.place(x=600,y=460,height=95)
    
    login_button_image =tk.PhotoImage(file=r"D:\Com\second\pyrhon\bas _score\new\login\Login1.png")
    login_button = tk.Button(login_window, text="Login", command=validate_login,image=login_button_image,bd=0,highlightthickness=0,bg="#b7a299")
    login_button.image =login_button_image
    login_button.place(x=896,y=602)



    back_button_image =tk.PhotoImage(file=r"D:\Com\second\pyrhon\bas _score\new\login\back.png")
    back_button = tk.Button(login_window, text="Back", command=login_window.destroy,image=back_button_image,bd=0,highlightthickness=0,bg="#383737")
    back_button.image = back_button_image
    back_button.place(x=50,y=47)


    # reset_button_image =tk.PhotoImage(file=r"D:\Com\second\pyrhon\bas _score\new\login\Forget.png")
    # reset_button = tk.Button(login_window, text="reset", command=resetwindow,bg="#8f8d8d",image=reset_button_image,bd=0,highlightthickness=0)
    # reset_button.image=reset_button_image
    # reset_button.place(x=503,y=602)
    login_window.mainloop()

conn = sqlite3.connect('login.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT, email TEXT)')
conn.commit()
conn.close()

def check_email_in_database(email):
    conn = sqlite3.connect('login.db')
    cursor = conn.cursor()

    # Execute a query to check if the email exists
    cursor.execute("SELECT * FROM users WHERE email=?", (email,))
    user = cursor.fetchone()

    conn.close()

    return user is not None

def resetwindow():
        
        
    reset_window = Toplevel()
    reset_window.title("Forgot username/password")
    bg_image = tk.PhotoImage(file=r"D:\Com\second\pyrhon\bas _score\new\REset_password\Reset_password.png")
    reset_window.geometry("1200x670")
    bg_label = tk.Label(reset_window, image=bg_image)
    bg_label.image = bg_image  # Keep a reference to the image
    bg_label.place(x=0, y=0)
    def check_email():
            global otp_int
            email = email_entry.get()
            if check_email_in_database(email):
                # Email exists in the database, continue with your reset logic
                otp = random.randint(1000, 9999)
                otp_int =int(otp)
                # สร้างข้อความอีเมล
                subject = "Your OTP Code"
                body = f"Your OTP is: {otp}"
                sender_email = "theerasak.22em@gmail.com"
                receiver_email = f"{email}"

                message = MIMEText(body)
                message['Subject'] = subject
                message['From'] = sender_email
                message['To'] = receiver_email

                # เชื่อมต่อกับเซิร์ฟเวอร์ SMTP ของ Gmail
                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
                    server.login("theerasak.22em@gmail.com", "ockr qxir muzp qicc")
                    server.sendmail(sender_email, [receiver_email], message.as_string())

                print("OTP sent successfully.",otp_int)
                pass
            else:
                # Email does not exist, show a messagebox
                messagebox.showerror("Error", "Email not found in the database.")
    def check_otp ():
        global otp_int
        email = email_entry.get()
        entry_otp = otp_entry.get()
        if entry_otp == otp_int:
            conn = sqlite3.connect('login.db')
            c = conn.cursor()   
            c.execute("SELECT * FROM users WHERE email=?", (email,))
            user = c.fetchone()




        else :
            messagebox.showerror("Error", "worng OTP")

    check_button = tk.Button(reset_window, text="Check Email", command=check_email)
    check_button.place(x=500, y=150)
    
    
    check_otp_button = tk.Button(reset_window, text="Check otp", command=check_otp)
    check_otp_button.place(x=600, y=150)
    
    
    
    otp_entry= tk.Entry(reset_window,)
    otp_entry.place(x=390,y=200)


    back_button_image =tk.PhotoImage(file=r"D:\Com\second\pyrhon\bas _score\new\login\back.png")
    back_button = tk.Button(reset_window, text="Back", command=reset_window.destroy,image=back_button_image,bd=0,highlightthickness=0,bg="#383737")
    back_button.image = back_button_image
    back_button.place(x=50,y=47)

    


    email_entry =tk.Entry(reset_window)
    email_entry.place(x=390,y=110)


def open_register():
    register_window = Toplevel()
    bg_image = tk.PhotoImage(file=r"D:\Com\second\pyrhon\bas _score\new\regis\register_mail.png")
    register_window.geometry("1600x900")
    bg_label = tk.Label(register_window, image=bg_image)
    bg_label.image = bg_image  # Keep a reference to the image
    bg_label.place(x=0, y=0)
    def validate_register():
        username = username_entry.get()
        password = password_entry.get()
        email = email_entry.get()
        
        conn = sqlite3.connect('login.db')
        c = conn.cursor()
        
        c.execute('SELECT * FROM users WHERE username=?', (username,))
        if c.fetchone():
            error_label.config(text="Username นี้ถูกใช้ไปแล้ว")
            conn.close()
            return
        
        c.execute('INSERT INTO users (username, password, email) VALUES (?, ?, ?)', (username, password, email))
        conn.commit()
        
        conn.close()
        register_window.destroy()
    
    username_label = tk.Label(register_window, text="Username:")
    username_label.pack()
    username_entry = tk.Entry(register_window)
    username_entry.pack()
    
    password_label = tk.Label(register_window, text="Password:")
    password_label.pack()
    password_entry = tk.Entry(register_window, show="*")
    password_entry.pack()
    
    email_label = tk.Label(register_window, text="E-mail")
    email_label.pack()
    email_entry = tk.Entry(register_window)
    email_entry.pack()
    
    register_button_bg =tk.PhotoImage(file=r"D:\Com\second\pyrhon\bas _score\new\regis\Submit.png")
    register_button = tk.Button(register_window, text="Register", command=validate_register,image=register_button_bg)
    register_button.image = register_button_bg
    register_button.pack()
    
    error_label = tk.Label(register_window, text="", fg="red")
    error_label.pack()
    back_button = tk.Button(register_window, text="Back", command=register_window.destroy)
    back_button.pack()



info_button_BG= tk.PhotoImage(file=r"D:\Com\second\pyrhon\bas _score\new\first\button_information.png")
info_button = tk.Button(root, text="Information", command=open_information,image=info_button_BG,highlightthickness=0, bd=0,bg="#363534")
info_button.image = info_button_BG
info_button.place(x=456.33,y=179.77)


login_button_BG =tk.PhotoImage(file=r"D:\Com\second\pyrhon\bas _score\new\first\F_login.png")
login_button = tk.Button(root, text="Login", command=open_login,image =login_button_BG,highlightthickness=0, bd=0,bg="#383736")
login_button.image = login_button_BG
login_button.place(x=456, y=358)


register_button_BG = tk.PhotoImage(file=r"D:\Com\second\pyrhon\bas _score\new\first\register.png")
register_button = tk.Button(root, text="Register", command=open_register,image=register_button_BG,highlightthickness=0, bd=0,bg="#363534")
register_button.image = register_button_BG
register_button.place(x=456,y=539)

def destroy_main():
    root.withdraw()
    
  
def open_main():
    
    destroy_main()
    window = Toplevel()
    window.geometry("1600x900")
    window.minsize(1440, 810)
    window.maxsize(1440, 810)
    window.option_add('*Font','DBHelvethaicaX 15')
    window.title("Score Sheet Basketball")
    bg = Image.open(r"D:\Com\second\pyrhon\bas _score\main_bg (1).png") 
    photo = ImageTk.PhotoImage(bg)
    Label(window,image=photo).place(x=0,y=0)

    db  = sqlite3.connect('teams.db')
    conn1 = db.cursor()

    

    def create_team_table():
        team_name = team_name_entry.get()
        db.execute(f'''
        CREATE TABLE IF NOT EXISTS {team_name} 
        (   id INTEGER PRIMARY KEY AUTOINCREMENT,
            player_id TEXT,
            player_name TEXT,
            player_number TEXT,
            position TEXT,
            path_images TEXT NOT NULL,
            images BLOB NOT NULL,
            UNIQUE(player_id))''')
        db.commit()
        showplayer()
    
    def create_team_table_copy():
        db3  = sqlite3.connect('log_teams.db')
        conn3 = db3.cursor()
        team_name_copy = team_name_entry.get()
        table_name = team_name_copy 
        conn3.execute(f'''
        CREATE TABLE IF NOT EXISTS {table_name}
        (   id INTEGER PRIMARY KEY AUTOINCREMENT,
            player_id TEXT,
            player_name TEXT,
            player_number TEXT,
            position TEXT,
            path_images TEXT NOT NULL,
            images BLOB NOT NULL,
            scores INTEGER,
            fouls INTEGER,
            UNIQUE(player_id))''')
        db3.commit()

    def creat_two_table():
        create_team_table()
        create_team_table_copy()


    # finish
    def finish_botton():
        tamlaew()

    def tamlay():
        finish_botton()

    button = tk.Button(window, text="Finish", command=tamlay,font="DBHelvethaicaX 20",bd=0)
    button.place(x=1249,y=66)
    button.config(width=10)



    def add_player():
        team_name = team_name_entry.get()
        player_name = name.get()
        player_number = number.get()
        position = positions.get()
        global image_path

        player_id = f"{team_name}_{player_number}"

        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.gif *.bmp *.jpeg")])
        if file_path:  
            image_path = file_path  # Assign the selected file path to image_path
            with open(image_path, 'rb') as image_file:
                image_data = image_file.read()
            db.execute(f"INSERT INTO {team_name} (player_id, player_name, player_number, position, path_images, images) VALUES (?, ?, ?, ?, ?, ?)",
                    (player_id, player_name, player_number, position, image_path, image_data))
            db.commit()
        showplayer()




    def showplayer():
        team_name = team_name_entry.get()
        sql_cmd = f"SELECT player_id, player_name, player_number, position FROM {team_name}"
        players = db.execute(sql_cmd)
        listbox.delete(0, END)
        for player in players:
            listbox.insert(END, player)
            

    def on_click_edit_button():
        window_edit()

    def exit_program():
        result = messagebox.askyesno("สิออกหรือบ่ออก", "ออกอยู่บ้อ")
        if result:
            window.destroy()


    button_exit = tk.Button(window,text="ออกบ่", command=exit_program,bd=0,font="DBHelvethaicaX 20")
    button_exit.place(x=110, y=66)
    button_exit.config(width=10)

    # "ชื่อทีม:"
    team_name_entry = tk.Entry(window,width=30,font="DBHelvethaicaX 40")
    team_name_entry.place(x=300, y=200)
    team_name_entry.config(width=15)

    create_team_button = tk.Button(window, text="สร้าง/เลือกทีม", command=creat_two_table,bd=0,font="DBHelvethaicaX 20")
    create_team_button.place(x=600, y=200)

    name = tk.Entry(window,font="DBHelvethaicaX 40")
    name.place(x=300, y=300)
    name.config(width=15)
    # name_label =Label(root, text="ชื่อผู้เล่น:").place(x=300,y=310)
    number = tk.Entry(window,font="DBHelvethaicaX 40")
    number.place(x=300, y=400)
    number.config(width=15)
    # number_label=Label(root, text="หมายเลขผู้เล่น:").place(x=280,y=410)
    positions = tk.Entry(window,font="DBHelvethaicaX 40")
    positions.place(x=300, y=500)
    positions.config(width=15)

    add_player_button = tk.Button(window, text="เพิ่มนักกีฬา", command=add_player,font="DBHelvethaicaX 20",bd=0)
    add_player_button.place(x=300, y=600)
    add_player_button.config(width=10)


    listbox = tk.Listbox(window,width=30,height=17,font="DBHelvethaicaX 20",bd=0)
    listbox.place(x=900,y=200)

    show_player_button = tk.Button(window,text ="Refresh", command=showplayer,font="DBHelvethaicaX 20",bd=0)
    show_player_button.place(x=450, y=600)
    show_player_button.config(width=10)


    edit_button = tk.Button(window,text="edit", command=on_click_edit_button,font="DBHelvethaicaX 20",bd=0)
    edit_button.place(x=600, y=600)
    edit_button.config(width=10)

    
    #edit window 
    def window_edit():
            global edit_window

            if edit_window is not None and edit_window.winfo_exists():
                edit_window.destroy()

            edit_window = Toplevel()
            edit_window.title("Score Sheet Basketball")
            edit_window.geometry("1280x720")

            id_var = StringVar()
            player_id_var = StringVar()
            name_var = StringVar()
            number_var = StringVar()
            position_var = StringVar()

            def showdata():
                team_name = team_name_entry.get()
                sql_cmd = f"SELECT id,player_id,player_name, player_number, position FROM {team_name}"
                players = db.execute(sql_cmd)
                for item in players:
                    Label(edit_window, text=item).pack(anchor="nw")
                    e = Button(edit_window, text="Edit", command=lambda k=item[0]: edit_data(k))
                    e.pack()
            def edit_data(selected_id):
                team_name = team_name_entry.get()
                sql_cmd = f"SELECT id,player_id,player_name, player_number,position FROM {team_name} WHERE id = ?"
                cursor = db.execute(sql_cmd, (selected_id,))
                row = cursor.fetchone()

                id_var.set(row[0])
                player_id_var.set(row[1])
                name_var.set(row[2])
                number_var.set(row[3])
                position_var.set(row[4])

                e0 = Entry(edit_window, textvariable=id_var,state="readonly")
                e0.pack(side=LEFT)
                e1 = Entry(edit_window,textvariable=player_id_var)
                e1.pack(side = LEFT)
                e2 = Entry(edit_window, textvariable=name_var)
                e2.pack(side=LEFT)
                e3 = Entry(edit_window, textvariable=number_var)
                e3.pack(side=LEFT)
                e4 = Entry(edit_window, textvariable=position_var)
                e4.pack(side=LEFT)

                b2 = Button(edit_window, text="UPDATE", command=update_data)
                b2.pack(side=LEFT)
                b3 = Button(edit_window, text="Delete", command=delete_player)
                b3.pack(side=LEFT)

            def update_data():
                team_name = team_name_entry.get()
                data = (player_id_var.get(),name_var.get(), number_var.get(), position_var.get(), id_var.get())
                sql_cmd = f"UPDATE {team_name} SET player_id = ? ,player_name = ?, player_number = ?, position = ? WHERE id = ?"
                db.execute(sql_cmd, data)
                db.commit()
                for widget in edit_window.winfo_children():
                        widget.destroy()
                showdata()

            def delete_player():
                player_id = id_var.get()
                team_name = team_name_entry.get()
                sql_cmd = f"DELETE FROM {team_name} WHERE id = ?"
                decrement_cmd = f"UPDATE {team_name} SET id = id - 1 WHERE id > ?"

                try:
                        
                        db.execute(sql_cmd, (player_id,))
                        db.execute(decrement_cmd, (player_id,))
                        db.commit()
                        for widget in edit_window.winfo_children():
                            widget.destroy()
                        showdata()
                except sqlite3.Error as e:
                    print("Error deleting player:", e)

            showdata()
    window.mainloop()        
root.mainloop()




                

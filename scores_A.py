from tkinter import *
from PIL import Image, ImageTk
from tkinter.ttk import *
import sqlite3 
from tkinter import simpledialog
from tkinter import font 
import tkinter as tk
from tkinter import ttk 
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
import sqlite3


# team_1, team_2 = finish_botton()

db1 = sqlite3.connect('teams.db')
conn1 = db1.cursor()

db2 = sqlite3.connect('matchs.db')
conn2 = db2.cursor()

fouls_der_a = 0
fouls_der_b = 0 
kho_timeouts_a = 0
kho_timeouts_b = 0
quarter = 1

team1 = None
team2 = None


#team A
foul_team_A = 5 
timeout_value_A = 0
total_fouls_A = 0
player_1_fouls = 0
player_2_fouls = 0
player_3_fouls = 0
player_4_fouls = 0
player_5_fouls = 0
player_6_fouls = 0
player_7_fouls = 0
player_8_fouls = 0
player_9_fouls = 0
player_10_fouls = 0
player_11_fouls = 0
player_12_fouls = 0

max_fouls= 5

player_1_scores = 0
player_2_scores = 0
player_3_scores = 0
player_4_scores = 0
player_5_scores = 0
player_6_scores = 0
player_7_scores = 0
player_8_scores = 0
player_9_scores = 0
player_10_scores = 0
player_11_scores = 0
player_12_scores = 0

total_point_A= 0

#team B
foul_team_B = 5 
timeout_value_B = 0
total_fouls_B = 0
player_13_fouls = 0
player_14_fouls = 0
player_15_fouls = 0
player_16_fouls = 0
player_17_fouls = 0
player_18_fouls = 0
player_19_fouls = 0
player_20_fouls = 0
player_21_fouls = 0
player_22_fouls = 0
player_23_fouls = 0
player_24_fouls = 0
toltal_fouls_B = 0


player_13_scores = 0
player_14_scores = 0
player_15_scores = 0
player_16_scores = 0
player_17_scores = 0
player_18_scores = 0
player_19_scores = 0
player_20_scores = 0
player_21_scores = 0
player_22_scores = 0
player_23_scores = 0
player_24_scores = 0
total_point_B= 0


def tamlaew():
    
    master = Toplevel()
    master.geometry("1440x810")
    label_font = font.Font(size = 14)
    master.minsize(1440, 810)
    master.maxsize(1440, 810)

    bg = Image.open(r"D:\Com\second\pyrhon\bas _score\MABG.png")
    bg = bg.resize((1440, 810), Image.ANTIALIAS)  # ปรับขนาดรูปให้ตรงกับหน้าต่างหลัก
    photo = ImageTk.PhotoImage(bg)
    canvas = Canvas(master, width=1600, height=900)
    canvas.pack()
    canvas.create_image(0, 0, anchor=NW, image=photo)

   
    
    destroy_window = tk.Button(master,text="Back", command = master.destroy,font="DBHelvethaicaX 20",bd=0)
    destroy_window.place(x=38, y=10)
    destroy_window.config(width=10)


    # button = Button(master, text="กรอกทีม", command=input_team)
    # button.place(x=38, y=120) 

    #team A
    b_player_1 = IntVar()
    b_player_2 = IntVar()
    b_player_3 = IntVar()
    b_player_4 = IntVar()
    b_player_5 = IntVar()
    b_player_6 = IntVar()
    b_player_7 = IntVar()
    b_player_8 = IntVar()
    b_player_9 = IntVar()
    b_player_10 = IntVar()
    b_player_11 = IntVar()
    b_player_12 = IntVar()

    fouls_point_A  = IntVar()
    max_fouls_A_team_A = IntVar()


    s_player_1 = IntVar()
    s_player_2 = IntVar()
    s_player_3 = IntVar()
    s_player_4 = IntVar()
    s_player_5 = IntVar()
    s_player_6 = IntVar()
    s_player_7 = IntVar()
    s_player_8 = IntVar()
    s_player_9 = IntVar()
    s_player_10 = IntVar()
    s_player_11 = IntVar()



    s_player_12 = IntVar()
    s_player_13 = IntVar()
    s_player_14 = IntVar()
    s_player_15 = IntVar()
    s_player_16 = IntVar()
    s_player_17 = IntVar()
    s_player_18 = IntVar()
    s_player_19 = IntVar()
    s_player_20 = IntVar()
    s_player_21 = IntVar()
    s_player_22 = IntVar()
    s_player_23 = IntVar()
    s_player_24 = IntVar()
    total_score_A = IntVar()


    #team B
    b_player_13 = IntVar()
    b_player_14 = IntVar()
    b_player_15 = IntVar()
    b_player_16 = IntVar()
    b_player_17 = IntVar()
    b_player_18 = IntVar()
    b_player_19 = IntVar()
    b_player_20 = IntVar()
    b_player_21 = IntVar()
    b_player_22 = IntVar()
    b_player_23 = IntVar()
    b_player_24 = IntVar()
    fouls_point_B  = IntVar()
    max_fouls_B_team_ = IntVar()

    
    s_player_13 = IntVar()
    s_player_14 = IntVar()
    s_player_15 = IntVar()
    s_player_16 = IntVar()
    s_player_17 = IntVar()
    s_player_18 = IntVar()
    s_player_19 = IntVar()
    s_player_20 = IntVar()
    s_player_21 = IntVar()
    s_player_22 = IntVar()
    s_player_23 = IntVar()
    s_player_24 = IntVar()
    total_score_B = IntVar()

    team1_selected = tk.StringVar()
    team2_selected = tk.StringVar()
    
    name_match = tk.StringVar()

# Ask for input
    name_match.set(simpledialog.askstring("Input", "ชื่อการแข่งขัน"))

# Check if input is provided
    def create_table_match():
            name_of_match = name_match.get()
            db2.execute(f'''
            CREATE TABLE IF NOT EXISTS {name_of_match}
            (   quarter INTEGER PRIMARY KEY AUTOINCREMENT,
                total_scores_A INTEGER,
                total_scores_B INTEGER,
                time_outs_A INTEGER,
                time_outs_B INTEGER,
                fouls_A INTEGER,
                fouls_B INTEGER,
                date_time TIMESTAMP
            )
            ''')
            db2.commit()
    
    create_table_match()
    





            

            


        

    

    

    def populate_teams():
        conn1.execute("SELECT name FROM sqlite_master WHERE type='table'")
        table_names = [row[0] for row in conn1.fetchall()] 
        team1_combobox['values'] = table_names
        team2_combobox['values'] = table_names
    
    def input_team():
        team1 = team1_selected.get()
        team2 = team2_selected.get()
        create_table_team_A()
        create_table_team_B()      

        if team1 and team2:
            show_name_A(team1)
            show_name_B(team2)
            show_number_A(team1)
            show_number_B(team2)
            show_all_star_A(team1)
            show_all_star_B(team2)

    def show_name_A(team_1):
        if team_1:
            sql_cmd = f"SELECT player_name FROM {team_1}"
            for index, item in enumerate(db1.execute(sql_cmd)):
                player_name = item[0]
                Label(master, text=player_name, font=label_font,background='#f3f1fc').place(x=80, y=(index * 30) + 400)
                    
    def show_all_star_A(team1):
        label=Label(master, text = team1,font=label_font)
        label.place(x=350, y=110)
        label.config(background='#df5162')
        
    def show_all_star_B(team2):
        label2=Label(master, text = team2,font=label_font)
        label2.place(x=980, y=110)
        label2.config(background='#3db2b8')
   
    def show_name_B(team_2):
            if team_2:
                sql_cmd = f"SELECT player_name FROM {team_2}"
                for index, item in enumerate(db1.execute(sql_cmd)):
                    player_name = item[0]
                    Label(master, text=player_name, font=label_font,background="#f3f1fc").place(x=785,y=(index * 30) + 400)
    
    def show_number_A(team1):
        sql_cmd = f'select player_number from {team1}'
        for index, item in enumerate(db1.execute(sql_cmd)):
                    Label(master, text=item,font=label_font,background="#f3f1fc").place(x=300,y=(index * 30) + 400)
    
    def show_number_B(team2):
        sql_cmd = f'select player_number from {team2}'
        for index, item in enumerate(db1.execute(sql_cmd)):
                    Label(master, text=item,font=label_font,background="#f3f1fc").place(x=1000,y=(index * 30) + 400)
                   

    team1_combobox = ttk.Combobox(master, textvariable=team1_selected)
    team2_combobox = ttk.Combobox(master, textvariable=team2_selected)
    team1_combobox.place(x=40, y=100)
    team2_combobox.place(x=1220, y=100)

    
    populate_teams()
    select_button = tk.Button(master, text="เลือกทีม", command=input_team,font="DBHelvethaicaX 20",bd=0)
    select_button.place(x=180, y=10)
    select_button.config(width=10)

    def create_table_team_A():
        team1 = team1_selected.get()
        
        # Check if the 'scores' column exists in the table
        cursor = db1.execute(f"PRAGMA table_info({team1})")
        columns = [column[1] for column in cursor.fetchall()]
        
        if 'scores' not in columns:
            # Add the 'scores' column if it does not exist
            db1.execute(f"ALTER TABLE {team1} ADD COLUMN scores INTEGER")
        
        # Check if the 'fouls' column exists in the table
        if 'fouls' not in columns:
            # Add the 'fouls' column if it does not exist
            db1.execute(f"ALTER TABLE {team1} ADD COLUMN fouls INTEGER")

        db1.commit()


    def create_table_team_B():
        team2 = team2_selected.get()
        
        # Check if the 'scores' column exists in the table
        cursor = db1.execute(f"PRAGMA table_info({team2})")
        columns = [column[1] for column in cursor.fetchall()]
        
        if 'scores' not in columns:
            # Add the 'scores' column if it does not exist
            db1.execute(f"ALTER TABLE {team2} ADD COLUMN scores INTEGER")
        
        # Check if the 'fouls' column exists in the table
        if 'fouls' not in columns:
            # Add the 'fouls' column if it does not exist
            db1.execute(f"ALTER TABLE {team2} ADD COLUMN fouls INTEGER")

        db1.commit()


    def make_pdf():
            try:
                
                team1 = team1_selected.get()
                conn1.execute(f'SELECT player_name, player_number, position, scores, fouls FROM {team1}')
                data = conn1.fetchall()
                print(data)
                column_names = ['Name', 'Number', 'Position', 'Scores', 'Fouls']  # Replace with your actual column names
                
                team2 = team2_selected.get()
                conn1.execute(f'SELECT player_name, player_number, position, scores, fouls FROM {team2}')
                data_team_b = conn1.fetchall()
                print(data_team_b)
                


                name_of_match = name_match.get()
                conn2.execute(f'SELECT total_scores_A, total_scores_B, time_outs_A, time_outs_B, fouls_A, fouls_B FROM {name_of_match}')
                data_matchs = conn2.fetchall()
                print(data_matchs)

                column_names_matchs = ['Scores A', 'Scores B', 'Time Outs A', 'Time Outs B', 'Fouls A', 'Fouls B']  # Replace with your actual column names

            

                pdf_filename = 'detail.pdf'

                
                doc = SimpleDocTemplate(pdf_filename, pagesize=letter)

            
                table_data_matchs = [column_names_matchs]  
                table_data_matchs.extend(data_matchs)  

            
                table_data = [column_names] 
                table_data.extend(data)  
                
                table_data_team_b = [column_names]  
                table_data_team_b.extend(data_team_b)  

            
                column_widths = [100] * len(column_names)

                
                table_matchs = Table(table_data_matchs, colWidths=column_widths)
                table = Table(table_data, colWidths=column_widths)
                table_team_b = Table(table_data_team_b, colWidths=column_widths)

                team1 = team1_selected.get()
                team2 = team2_selected.get()
                name_of_match = name_match.get()
                team_title = Paragraph("Team A:" + team1, getSampleStyleSheet()['Title'])
                team_title_team_b = Paragraph("Team B:" + team2, getSampleStyleSheet()['Title'])
                match_title_name = Paragraph("Match :" + name_of_match, getSampleStyleSheet()['Title'])
                
                style = TableStyle([])

                table_matchs.setStyle(style)
                table.setStyle(style)
                table_team_b.setStyle(style)

        
                elements = [match_title_name,table_matchs, PageBreak(), team_title, table, PageBreak(), team_title_team_b, table_team_b]
                doc.build(elements)
                
                
            except Exception as e:
                print(f"An error occurred: {e}")

            copy_table()
            
            clear_scores()
            destroyed()

            conn2.close()
            conn1.close()


    def clear_scores():
        team1 = team1_selected.get()
        team2 = team2_selected.get()
        db1.execute(f"UPDATE {team1}  SET scores = '', fouls = '' ")
        db1.execute(f"UPDATE {team2}  SET scores = '', fouls = '' ")
        db1.commit()
    
        
            
            




    





            
    
            



            
    
            




                
    
                




            

    def long_database():
        global fouls_der_b
        global fouls_der_a
        global total_point_A
        global total_point_B
        global kho_timeouts_a
        global kho_timeouts_b

        # fouls_der_a = 0 
        # fouls_der_b = 0
        # kho_timeouts_a = 0
        # kho_timeouts_b = 0 
        
        current_date_time = datetime.now()
        name_of_match = name_match.get()
        data = (total_point_A,total_point_B,kho_timeouts_a,kho_timeouts_b,fouls_der_a,fouls_der_b,current_date_time)
        db2.execute(f"INSERT INTO {name_of_match} (total_scores_A, total_scores_B, time_outs_A, time_outs_B, fouls_A, fouls_B, date_time) VALUES (?, ?, ?, ?, ?, ?, ?)", data)
        db2.commit()

    def copy_table():
        db3 = sqlite3.connect('log_teams.db')
        conn3 = db3.cursor()

        team1 = team1_selected.get()
        team2 = team2_selected.get()

        # Retrieve data from the source tables
        conn1.execute(f"SELECT * FROM {team1}")
        data1 = conn1.fetchall()  # Fetch all rows from the result
        conn1.execute(f"SELECT * FROM {team2}")
        data2 = conn1.fetchall()  # Fetch all rows from the result

        table_name1 = team1  # The table name you want to copy data into
        table_name2 = team2  # The table name you want to copy data into

        # Create tables in the destination database if they don't exist
        conn3.execute(f"CREATE TABLE IF NOT EXISTS {table_name1} AS SELECT * FROM {team1}")
        conn3.execute(f"CREATE TABLE IF NOT EXISTS {table_name2} AS SELECT * FROM {team2}")

        # Insert data into the destination tables
        for row in data1:
            conn3.execute(f"INSERT INTO {table_name1} VALUES ({', '.join(['?'] * len(row))})", row)

        for row in data2:
            conn3.execute(f"INSERT INTO {table_name2} VALUES ({', '.join(['?'] * len(row))})", row)

        # Commit the changes to the destination database
        db3.commit()  # Commit changes to the destination database

            # Close both database connectio
        
    
    def on_click_fouls(player_num):
        global max_fouls
        global total_fouls_A
        global foul_team_A
        global total_fouls_B
        global fouls_der_a
        global fouls_der_b
        global quarter
        
        

        
        if player_num == 1:
            global player_1_fouls
            player_1_fouls += 1
            team1 = team1_selected.get()
            db1.execute(f'UPDATE {team1} SET fouls = ? WHERE id = 1',(player_1_fouls,))
            db1.commit()

            b_player_1.set(player_1_fouls)
            fouls_point_A.set(total_fouls_A)
            total_fouls_A += 1
            fouls_der_a +=1
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET fouls_A = ? WHERE quarter = ?',(fouls_der_a,quarter))
            db2.commit()
            fouls_point_A.set(min(total_fouls_A, 5))  
            if total_fouls_A ==foul_team_A:
                fouls_point_A.set(5)
            
            if player_1_fouls >= max_fouls:
                button_player_1["state"] = DISABLED
                button_player_1_scores["state"] = DISABLED
                button_player_1_scores_two["state"] = DISABLED
                button_player_1_scores_three['state'] = DISABLED
                
            
            
            
        elif player_num == 2:
            global player_2_fouls
            player_2_fouls += 1
            team1 = team1_selected.get()
            db1.execute(f'UPDATE {team1} SET fouls = ? WHERE id = 2',(player_2_fouls,))
            db1.commit()
            b_player_2.set(player_2_fouls)
            fouls_point_A.set(total_fouls_A)
            total_fouls_A += 1
            fouls_der_a +=1
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET fouls_A = ? WHERE quarter = ?',(fouls_der_a,quarter))
            db2.commit()
            fouls_point_A.set(min(total_fouls_A, 5))
            if total_fouls_A ==foul_team_A:
                fouls_point_A.set(5)
                
            if player_2_fouls >= max_fouls:
                button_player_2["state"] = DISABLED
                button_player_2_scores["state"] = DISABLED
                button_player_2_scores_two["state"] = DISABLED
                button_player_2_scores_three['state'] = DISABLED

                
                
            
            
            
        elif player_num == 3:
            global player_3_fouls
            player_3_fouls += 1
            team1 = team1_selected.get()
            db1.execute(f'UPDATE {team1} SET fouls = ? WHERE id = 3',(player_3_fouls,))
            db1.commit()
            b_player_3.set(player_3_fouls)
            fouls_point_A.set(total_fouls_A)
            total_fouls_A += 1
            fouls_der_a +=1
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET fouls_A = ? WHERE quarter = ?',(fouls_der_a,quarter))
            db2.commit()
            fouls_point_A.set(min(total_fouls_A, 5))
            if total_fouls_A ==foul_team_A:
                fouls_point_A.set(5)
            if player_3_fouls >= max_fouls:
                button_player_3["state"] = DISABLED
                button_player_3_scores["state"] = DISABLED
                button_player_3_scores_two["state"] = DISABLED
                button_player_3_scores_three['state'] = DISABLED
                
        

        elif player_num == 4:
            global player_4_fouls
            
            player_4_fouls += 1
            team1 = team1_selected.get()
            db1.execute(f'UPDATE {team1} SET fouls = ? WHERE id = 4 ',(player_4_fouls,))
            db1.commit()
            b_player_4.set(player_4_fouls)
            fouls_point_A.set(total_fouls_A)
            total_fouls_A += 1
            fouls_der_a +=1
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET fouls_A = ? WHERE quarter = ?',(fouls_der_a,quarter))
            db2.commit()
            fouls_point_A.set(min(total_fouls_A, 5))
            if total_fouls_A ==foul_team_A:
                fouls_point_A.set(5)
                
            if player_4_fouls >= max_fouls:
                button_player_4["state"] = DISABLED
                button_player_4_scores["state"] = DISABLED
                button_player_4_scores_two["state"] = DISABLED
                button_player_4_scores_three['state'] = DISABLED
        

        elif player_num == 5:
            global player_5_fouls
            
            
            player_5_fouls += 1
            team1 = team1_selected.get()
            db1.execute(f'UPDATE {team1} SET fouls = ? WHERE id = 5',(player_5_fouls,))
            db1.commit()
            b_player_5.set(player_5_fouls)
            fouls_point_A.set(total_fouls_A)
            if player_5_fouls >= max_fouls:
                button_player_5["state"] = DISABLED
                button_player_5_scores["state"] = DISABLED
                button_player_5_scores_two["state"] = DISABLED
                button_player_5_scores_three['state'] = DISABLED
            total_fouls_A += 1
            fouls_der_a +=1
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET fouls_A = ? WHERE quarter = ?',(fouls_der_a,quarter))
            db2.commit()
            fouls_point_A.set(min(total_fouls_A, 5))
            if total_fouls_A ==foul_team_A:
                fouls_point_A.set(5)

        elif player_num == 6:
            global player_6_fouls
            
            
            player_6_fouls += 1
            team1 = team1_selected.get()
            db1.execute(f'UPDATE {team1} SET fouls = ? WHERE id = 6',(player_6_fouls,))
            db1.commit()
            b_player_6.set(player_6_fouls)
            fouls_point_A.set(total_fouls_A)
            if player_6_fouls >= max_fouls:
                button_player_6["state"] = DISABLED
                button_player_6_scores["state"] = DISABLED
                button_player_6_scores_two["state"] = DISABLED
                button_player_6_scores_three['state'] = DISABLED
            total_fouls_A += 1
            fouls_der_a +=1
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET fouls_A = ? WHERE quarter = ?',(fouls_der_a,quarter))
            db2.commit()
            fouls_point_A.set(min(total_fouls_A, 5))
            if total_fouls_A == foul_team_A:
                fouls_point_A.set(5)
        

        elif player_num == 7:
            global player_7_fouls
            
            
            player_7_fouls += 1
            team1 = team1_selected.get()
            db1.execute(f'UPDATE {team1} SET fouls = ? WHERE id = 7',(player_7_fouls,))
            db1.commit()
            b_player_7.set(player_7_fouls)
            fouls_point_A.set(total_fouls_A)
            if player_7_fouls >= max_fouls:
                button_player_7["state"] = DISABLED
                button_player_7_scores["state"] = DISABLED
                button_player_7_scores_two["state"] = DISABLED
                button_player_7_scores_three['state'] = DISABLED
            total_fouls_A += 1
            fouls_der_a +=1
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET fouls_A = ? WHERE quarter = ?',(fouls_der_a,quarter))
            db2.commit()
            fouls_point_A.set(min(total_fouls_A, 5))
            if total_fouls_A ==foul_team_A:
                fouls_point_A.set(5)
        

        elif player_num == 8:
            global player_8_fouls
            
            
            player_8_fouls += 1
            team1 = team1_selected.get()
            db1.execute(f'UPDATE {team1} SET fouls = ? WHERE id = 8',(player_8_fouls,))
            db1.commit()
            b_player_8.set(player_8_fouls)
            fouls_point_A.set(total_fouls_A)
            if player_8_fouls >= max_fouls:
                button_player_8["state"] = DISABLED
                button_player_8_scores["state"] = DISABLED
                button_player_8_scores_two["state"] = DISABLED
                button_player_8_scores_three['state'] = DISABLED
            total_fouls_A += 1
            fouls_der_a +=1
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET fouls_A = ? WHERE quarter = ?',(fouls_der_a,quarter))
            db2.commit()
            fouls_point_A.set(min(total_fouls_A, 5))
            if total_fouls_A ==foul_team_A:
                fouls_point_A.set(5)

        elif player_num == 9:
            global player_9_fouls
            
            
            player_9_fouls += 1
            team1 = team1_selected.get()
            db1.execute(f'UPDATE {team1} SET fouls = ? WHERE id = 9',(player_9_fouls,))
            db1.commit()
            b_player_9.set(player_9_fouls)
            fouls_point_A.set(total_fouls_A)
            if player_9_fouls >= max_fouls:
                button_player_9["state"] = DISABLED
                button_player_9_scores["state"] = DISABLED
                button_player_9_scores_two["state"] = DISABLED
                button_player_9_scores_three['state'] = DISABLED
            total_fouls_A += 1
            fouls_der_a +=1
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET fouls_A = ? WHERE quarter = ?',(fouls_der_a,quarter))
            db2.commit()
            fouls_point_A.set(min(total_fouls_A, 5))
            if total_fouls_A ==foul_team_A:
                fouls_point_A.set(5)
        

        elif player_num == 10:
            global player_10_fouls
            
            
            player_10_fouls += 1
            team1 = team1_selected.get()
            db1.execute(f'UPDATE {team1} SET fouls = ? WHERE id = 10',(player_10_fouls,))
            db1.commit()
            b_player_10.set(player_10_fouls)
            fouls_point_A.set(total_fouls_A)
            if player_10_fouls >= max_fouls:
                button_player_10["state"] = DISABLED
                button_player_10_scores["state"] = DISABLED
                button_player_10_scores_two["state"] = DISABLED
                button_player_10_scores_three['state'] = DISABLED
            total_fouls_A += 1
            fouls_der_a +=1
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET fouls_A = ? WHERE quarter = ?',(fouls_der_a,quarter))
            db2.commit()
            fouls_point_A.set(min(total_fouls_A, 5))
            if total_fouls_A ==foul_team_A:
                fouls_point_A.set(5)
        

        elif player_num == 11:
            global player_11_fouls
            
            
            player_11_fouls += 1
            team1 = team1_selected.get()
            db1.execute(f'UPDATE {team1} SET fouls = ? WHERE id = 11 ',(player_11_fouls,))
            db1.commit()
            b_player_11.set(player_11_fouls)
            fouls_point_A.set(total_fouls_A)
            if player_11_fouls >= max_fouls:
                button_player_11["state"] = DISABLED
                button_player_11_scores["state"] = DISABLED
                button_player_11_scores_two["state"] = DISABLED
                button_player_11_scores_three['state'] = DISABLED
            total_fouls_A += 1
            fouls_der_a +=1
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET fouls_A = ? WHERE quarter = ?',(fouls_der_a,quarter))
            db2.commit()
            fouls_point_A.set(min(total_fouls_A, 5))
            if total_fouls_A ==foul_team_A:
                fouls_point_A.set(5)
        

        elif player_num == 12:
            global player_12_fouls
            
            
            player_12_fouls += 1
            team1 = team1_selected.get()
            db1.execute(f'UPDATE {team1} SET fouls = ? WHERE id = 12',(player_12_fouls,))
            db1.commit()
            b_player_12.set(player_12_fouls)
            fouls_point_A.set(total_fouls_A)
            if player_12_fouls >= max_fouls:
                button_player_12["state"] = DISABLED
                button_player_12_scores["state"] = DISABLED
                button_player_12_scores_two["state"] = DISABLED
                button_player_12_scores_three['state'] = DISABLED
            total_fouls_A += 1
            fouls_der_a +=1
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET fouls_A = ? WHERE quarter = ?',(fouls_der_a,quarter))
            db2.commit()
            fouls_point_A.set(min(total_fouls_A, 5))
            if total_fouls_A ==foul_team_A:
                fouls_point_A.set(5)
            

        #team B
        elif player_num == 13:
            global player_13_fouls
            total_fouls_B += 1 
            
            fouls_der_b +=1
            name_of_match = name_match.get()
            player_13_fouls += 1
            team2 = team2_selected.get()
            db1.execute(f'UPDATE {team2} SET fouls = ? WHERE id = 1',(player_13_fouls,))
            db1.commit()
            b_player_13.set(player_13_fouls)
            fouls_point_B.set(total_fouls_B)
            if player_13_fouls >= max_fouls:
                button_player_13["state"] = DISABLED
                button_player_13_scores["state"] = DISABLED
                button_player_13_scores_two["state"] = DISABLED
                button_player_13_scores_three['state'] = DISABLED
            fouls_point_B.set(min(total_fouls_B, 5))
            if total_fouls_B ==foul_team_B:
                fouls_point_B.set(5)
            db2.execute(f'UPDATE {name_of_match} SET fouls_B = ? WHERE quarter = ?',(fouls_der_b,quarter))
            db2.commit()

        elif player_num == 14:
            global player_14_fouls
            
            fouls_der_b +=1
            total_fouls_B += 1 
            name_of_match = name_match.get()
            player_14_fouls += 1
            team2 = team2_selected.get()
            db1.execute(f'UPDATE {team2} SET fouls = ? WHERE id = 2',(player_14_fouls,))
            db1.commit()
            b_player_14.set(player_14_fouls)
            fouls_point_B.set(total_fouls_B)
            if player_14_fouls >= max_fouls:
                button_player_14["state"] = DISABLED
                button_player_14_scores["state"] = DISABLED
                button_player_14_scores_two["state"] = DISABLED
                button_player_14_scores_three['state'] = DISABLED
            fouls_point_B.set(min(total_fouls_B, 5))
            if total_fouls_B ==foul_team_B:
                fouls_point_B.set(5)
            db2.execute(f'UPDATE {name_of_match} SET fouls_B = ? WHERE quarter = ?',(fouls_der_b,quarter))
            db2.commit()

        elif player_num == 15:
            global player_15_fouls
            fouls_der_b +=1
            total_fouls_B += 1 
            name_of_match = name_match.get()
            player_15_fouls += 1
            team2 = team2_selected.get()
            db1.execute(f'UPDATE {team2} SET fouls = ? WHERE id = 3 ',(player_15_fouls,))
            db1.commit()
            b_player_15.set(player_15_fouls)
            fouls_point_B.set(total_fouls_B)
            if player_15_fouls >= max_fouls:
                button_player_15["state"] = DISABLED
                button_player_15_scores["state"] = DISABLED
                button_player_15_scores_two["state"] = DISABLED
                button_player_15_scores_three['state'] = DISABLED
            fouls_point_B.set(min(total_fouls_B, 5))
            if total_fouls_B ==foul_team_B:
                fouls_point_B.set(5)
            db2.execute(f'UPDATE {name_of_match} SET fouls_B = ? WHERE quarter = ?',(fouls_der_b,quarter))
            db2.commit()

        elif player_num == 16:
            global player_16_fouls
            fouls_der_b +=1
            total_fouls_B += 1 
            name_of_match = name_match.get()
            player_16_fouls += 1
            team2 = team2_selected.get()
            db1.execute(f'UPDATE {team2} SET fouls = ? WHERE id = 4',(player_16_fouls,))
            db1.commit()
            b_player_16.set(player_16_fouls)
            fouls_point_B.set(total_fouls_B)
            if player_16_fouls >= max_fouls:
                button_player_16["state"] = DISABLED
                button_player_16_scores["state"] = DISABLED
                button_player_16_scores_two["state"] = DISABLED
                button_player_16_scores_three['state'] = DISABLED
            fouls_point_B.set(min(total_fouls_B, 5))
            if total_fouls_B ==foul_team_B:
                fouls_point_B.set(5)
            db2.execute(f'UPDATE {name_of_match} SET fouls_B = ? WHERE quarter = ?',(fouls_der_b,quarter))
            db2.commit()

        elif player_num == 17:
            global player_17_fouls
            fouls_der_b +=1
            total_fouls_B += 1 
            name_of_match = name_match.get()
            player_17_fouls += 1
            team2 = team2_selected.get()
            db1.execute(f'UPDATE {team2} SET fouls = ? WHERE id = 5',(player_17_fouls,))
            db1.commit()
            b_player_17.set(player_17_fouls)
            fouls_point_B.set(total_fouls_B)
            if player_17_fouls >= max_fouls:
                button_player_17["state"] = DISABLED
                button_player_17_scores["state"] = DISABLED
                button_player_17_scores_two["state"] = DISABLED
                button_player_17_scores_three['state'] = DISABLED
            fouls_point_B.set(min(total_fouls_B, 5))
            if total_fouls_B ==foul_team_B:
                fouls_point_B.set(5)
            db2.execute(f'UPDATE {name_of_match} SET fouls_B = ? WHERE quarter = ?',(fouls_der_b,quarter))
            db2.commit()

        elif player_num == 18:
            global player_18_fouls
            fouls_der_b +=1
            total_fouls_B += 1 
            name_of_match = name_match.get()
            player_18_fouls += 1
            team2 = team2_selected.get()
            db1.execute(f'UPDATE {team2} SET fouls = ? WHERE id = 6',(player_18_fouls,))
            db1.commit()
            b_player_18.set(player_18_fouls)
            fouls_point_B.set(total_fouls_B)
            if player_18_fouls >= max_fouls:
                button_player_18["state"] = DISABLED
                button_player_18_scores["state"] = DISABLED
                button_player_18_scores_two["state"] = DISABLED
                button_player_18_scores_three['state'] = DISABLED
            fouls_point_B.set(min(total_fouls_B, 5))
            if total_fouls_B ==foul_team_B:
                fouls_point_B.set(5)
            db2.execute(f'UPDATE {name_of_match} SET fouls_B = ? WHERE quarter = ?',(fouls_der_b,quarter))
            db2.commit()

        elif player_num == 19:
            global player_19_fouls
            fouls_der_b +=1
            total_fouls_B += 1 
            name_of_match = name_match.get()
            player_19_fouls += 1
            team2 = team2_selected.get()
            db1.execute(f'UPDATE {team2} SET fouls = ? WHERE id =7 ',(player_19_fouls,))
            db1.commit()
            b_player_19.set(player_19_fouls)
            fouls_point_B.set(total_fouls_B)
            if player_19_fouls >= max_fouls:
                    button_player_19["state"] = DISABLED
                    button_player_19_scores["state"] = DISABLED
                    button_player_19_scores_two["state"] = DISABLED
                    button_player_19_scores_three['state'] = DISABLED
            fouls_point_B.set(min(total_fouls_B, 5))
            if total_fouls_B ==foul_team_B:
                fouls_point_B.set(5)
            db2.execute(f'UPDATE {name_of_match} SET fouls_B = ? WHERE quarter = ?',(fouls_der_b,quarter))
            db2.commit()

        elif player_num == 20:
            global player_20_fouls
            fouls_der_b +=1
            total_fouls_B += 1 
            name_of_match = name_match.get()
            player_20_fouls += 1
            team2 = team2_selected.get()
            db1.execute(f'UPDATE {team2} SET fouls = ? WHERE id = 8',(player_20_fouls,))
            db1.commit()
            b_player_20.set(player_20_fouls)
            fouls_point_B.set(total_fouls_B)
            if player_20_fouls >= max_fouls:
                button_player_20["state"] = DISABLED
                button_player_20_scores["state"] = DISABLED
                button_player_20_scores_two["state"] = DISABLED
                button_player_20_scores_three['state'] = DISABLED
            fouls_point_B.set(min(total_fouls_B, 5))
            if total_fouls_B ==foul_team_B:
                fouls_point_B.set(5)
            db2.execute(f'UPDATE {name_of_match} SET fouls_B = ? WHERE quarter = ?',(fouls_der_b,quarter))
            db2.commit()
                

        elif player_num == 21:
            global player_21_fouls
            fouls_der_b +=1
            total_fouls_B += 1 
            name_of_match = name_match.get()
            player_21_fouls += 1
            team2 = team2_selected.get()
            db1.execute(f'UPDATE {team2} SET fouls = ? WHERE id = 9',(player_21_fouls,))
            db1.commit()
            b_player_21.set(player_21_fouls)
            fouls_point_B.set(total_fouls_B)
            if player_21_fouls >= max_fouls:
                button_player_21["state"] = DISABLED
                button_player_21_scores["state"] = DISABLED
                button_player_21_scores_two["state"] = DISABLED
                button_player_21_scores_three['state'] = DISABLED
            fouls_point_B.set(min(total_fouls_B, 5))
            if total_fouls_B ==foul_team_B:
                fouls_point_B.set(5)
            db2.execute(f'UPDATE {name_of_match} SET fouls_B = ? WHERE quarter = ?',(fouls_der_b,quarter))
            db2.commit()

        elif player_num == 22:
            global player_22_fouls
            fouls_der_b +=1
            total_fouls_B += 1 
            name_of_match = name_match.get()
            player_22_fouls += 1
            team2 = team2_selected.get()
            db1.execute(f'UPDATE {team2} SET fouls = ? WHERE id = 10',(player_22_fouls,))
            db1.commit()
            b_player_22.set(player_22_fouls)
            fouls_point_B.set(total_fouls_B)
            if player_22_fouls >= max_fouls:
                button_player_22["state"] = DISABLED
                button_player_22_scores["state"] = DISABLED
                button_player_22_scores_two["state"] = DISABLED
                button_player_22_scores_three['state'] = DISABLED
            fouls_point_B.set(min(total_fouls_B, 5))
            if total_fouls_B ==foul_team_B:
                fouls_point_B.set(5)
            db2.execute(f'UPDATE {name_of_match} SET fouls_B = ? WHERE quarter = ?',(fouls_der_b,quarter))
            db2.commit()

        elif player_num == 23:
            global player_23_fouls
            fouls_der_b +=1
            total_fouls_B += 1
            name_of_match = name_match.get()
            player_23_fouls += 1
            team2 = team2_selected.get()
            db1.execute(f'UPDATE {team2} SET fouls = ? WHERE id = 11',(player_23_fouls,))
            db1.commit()
            b_player_23.set(player_23_fouls)
            fouls_point_B.set(total_fouls_B)
            if player_23_fouls >= max_fouls:
                button_player_23["state"] = DISABLED
                button_player_23_scores["state"] = DISABLED
                button_player_23_scores_two["state"] = DISABLED
                button_player_23_scores_three['state'] = DISABLED
            fouls_point_B.set(min(total_fouls_B, 5))
            if total_fouls_B ==foul_team_B:
                fouls_point_B.set(5)
            db2.execute(f'UPDATE {name_of_match} SET fouls_B = ? WHERE quarter = ?',(fouls_der_b,quarter))
            db2.commit() 

        elif player_num == 24:
            global player_24_fouls
            fouls_der_b +=1
            total_fouls_B += 1
            name_of_match = name_match.get()
            player_24_fouls += 1
            team2 = team2_selected.get()
            db1.execute(f'UPDATE {team2} SET fouls = ? WHERE id = 12',(player_24_fouls,))
            db1.commit()
            b_player_24.set(player_24_fouls)
            fouls_point_B.set(total_fouls_B)
            if player_24_fouls >= max_fouls:
                button_player_24["state"] = DISABLED
                button_player_24_scores["state"] = DISABLED
                button_player_24_scores_two["state"] = DISABLED
                button_player_24_scores_three['state'] = DISABLED
            fouls_point_B.set(min(total_fouls_B, 5))
            if total_fouls_B ==foul_team_B:
                fouls_point_B.set(5)
            db2.execute(f'UPDATE {name_of_match} SET fouls_B = ? WHERE quarter = ?',(fouls_der_b,quarter))
            db2.commit() 
                
    
        
    #time-out
    def increase_timeout_A():
        global timeout_value_A
        global kho_timeouts_a
        global quarter
        if timeout_value_A < 4:
            kho_timeouts_a =+1
            timeout_value_A += 1
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET time_outs_A = ? WHERE quarter = ?',(kho_timeouts_a,quarter))
            db2.commit() 
            timeout_label_A.config(text=f"{timeout_value_A}")
    
    def increase_timeout_B():
        global timeout_value_B
        global kho_timeouts_b
        global quarter
        if timeout_value_B < 4:
            kho_timeouts_b =+ 1
            timeout_value_B += 1
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET time_outs_B = ? WHERE quarter = ?',(kho_timeouts_b,quarter))
            db2.commit() 
            timeout_label_B.config(text=f"{timeout_value_B}")
    
    
    #time out time A
    timeout_label_A = tk.Label(master, text="0",bg="#f3f1fc")
    button_A = tk.Button(master, text="OT", command=increase_timeout_A)
    timeout_label_A.place(x=145,y=292)
    timeout_label_A.config(background="#f3f1fc")
    button_A.place(x=200,y=300)

    timeout_label_B = tk.Label(master,text="0")
    button_B = tk.Button(master, text="OT",bg="#f3f1fc",command=increase_timeout_B)
    timeout_label_B.place(x=867,y=293)
    timeout_label_B.config(background="#f3f1fc")
    button_B.place(x=925,y=300)


    
    # timeout_label_B= Label(master, text="0")
    # button = Button(master, text="", command=increase_timeout_B)
    # button.place(x=1000,y=300)
    # button.config(width=3)
    #another team
        

    def reset_team_fouls():
        global quarter
        global total_fouls_A
        global total_fouls_B
        global fouls_der_a
        global fouls_der_b
        global kho_timeouts_a
        global kho_timeouts_b

        quarter += 1  # Increment the quarter first

        long_database()

        total_fouls_A = 0
        total_fouls_B = 0
        fouls_der_a = 0 
        fouls_der_b = 0
        kho_timeouts_a = 0
        kho_timeouts_b = 0

        # Update the database for the current quarter
        name_of_match = name_match.get()
        db2.execute(f'UPDATE {name_of_match} SET fouls_A = ?, fouls_B = ?, time_outs_A = ?, time_outs_B = ? WHERE quarter = ?', (fouls_der_a, fouls_der_b, kho_timeouts_a, kho_timeouts_b, quarter))
        db2.commit()

        fouls_point_A.set(0)
        fouls_point_B.set(0)


        


        
    

    def on_click_score_one_point(player_num):
        global total_point_A
        global total_point_B
        

        if player_num == 1:
            global player_1_scores
            player_1_scores += 1
            team1 = team1_selected.get()
            db1.execute(f'UPDATE {team1} SET scores = ? WHERE id = 1',(player_1_scores,))
            db1.commit()
            total_point_A +=1
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_A = ? WHERE quarter = ?',(total_point_A,quarter))
            db2.commit()
            s_player_1.set(player_1_scores)
            total_score_A.set(total_point_A)

        elif player_num == 2:
            global player_2_scores
            player_2_scores += 1
            team1 = team1_selected.get()
            db1.execute(f'UPDATE {team1} SET scores = ? WHERE id = 2',(player_2_scores,))
            db1.commit()
            total_point_A+=1
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_A = ? WHERE quarter = ?',(total_point_A,quarter))
            db2.commit()
            s_player_2.set(player_2_scores)
            total_score_A.set(total_point_A)
            
            
        elif player_num == 3:
            global player_3_scores
            player_3_scores += 1
            team1 = team1_selected.get()
            db1.execute(f'UPDATE {team1} SET scores = ? WHERE id = 3',(player_3_scores,))
            db1.commit()
            total_point_A +=1
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_A = ? WHERE quarter = ?',(total_point_A,quarter))
            db2.commit()
            s_player_3.set(player_3_scores)
            total_score_A.set(total_point_A)
            

        elif player_num == 4:
            global player_4_scores
            player_4_scores += 1
            team1 = team1_selected.get()
            db1.execute(f'UPDATE {team1} SET scores = ? WHERE id = 4',(player_4_scores,))
            db1.commit()
            total_point_A +=1
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_A = ? WHERE quarter = ?',(total_point_A,quarter))
            db2.commit()
            s_player_4.set(player_4_scores)
            total_score_A.set(total_point_A)
        

        elif player_num == 5:
            global player_5_scores
            player_5_scores += 1
            team1 = team1_selected.get()
            db1.execute(f'UPDATE {team1} SET scores = ? WHERE id = 5',(player_5_scores,))
            db1.commit()
            total_point_A +=1
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_A = ? WHERE quarter = ?',(total_point_A,quarter))
            db2.commit()
            s_player_5.set(player_5_scores)
            total_score_A.set(total_point_A)
        

        elif player_num == 6:
            global player_6_scores
            player_6_scores += 1
            team1 = team1_selected.get()
            db1.execute(f'UPDATE {team1} SET scores = ? WHERE id = 6',(player_6_scores,))
            db1.commit()
            total_point_A += 1 
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_A = ? WHERE quarter = ?',(total_point_A,quarter))
            db2.commit()
            s_player_6.set(player_6_scores)
            total_score_A.set(total_point_A)
        
        elif player_num == 7:
            global player_7_scores
            player_7_scores += 1
            team1 = team1_selected.get()
            db1.execute(f'UPDATE {team1} SET scores = ? WHERE id = 7',(player_7_scores,))
            db1.commit()
            total_point_A +=1
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_A = ? WHERE quarter = ?',(total_point_A,quarter))
            db2.commit()
            s_player_7.set(player_7_scores)
            total_score_A.set(total_point_A)
        
        elif player_num == 8:
            global player_8_scores
            player_8_scores += 1
            team1 = team1_selected.get()
            db1.execute(f'UPDATE {team1} SET scores = ? WHERE id = 8',(player_8_scores,))
            db1.commit()
            total_point_A +=1
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_A = ? WHERE quarter = ?',(total_point_A,quarter))
            db2.commit()
            s_player_8.set(player_8_scores)
            total_score_A.set(total_point_A)
        

        elif player_num == 9:
            global player_9_scores
            player_9_scores += 1
            team1 = team1_selected.get()
            db1.execute(f'UPDATE {team1} SET scores = ? WHERE id = 9',(player_9_scores,))
            db1.commit()
            total_point_A +=1
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_A = ? WHERE quarter = ?',(total_point_A,quarter))
            db2.commit()
            s_player_9.set(player_9_scores)
            total_score_A.set(total_point_A)
            

        elif player_num == 10:
            global player_10_scores
            player_10_scores += 1
            team1 = team1_selected.get()
            db1.execute(f'UPDATE {team1} SET scores = ? WHERE id = 10',(player_10_scores,))
            db1.commit()
            total_point_A+=1
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_A = ? WHERE quarter = ?',(total_point_A,quarter))
            db2.commit()
            s_player_10.set(player_10_scores)
            total_score_A.set(total_point_A)
        

        elif player_num == 11:
            global player_11_scores
            player_11_scores += 1
            team1 = team1_selected.get()
            db1.execute(f'UPDATE {team1} SET scores = ? WHERE id = 11',(player_11_scores,))
            db1.commit()
            total_point_A +=1
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_A = ? WHERE quarter = ?',(total_point_A,quarter))
            db2.commit()
            s_player_11.set(player_11_scores)
            total_score_A.set(total_point_A)
        

        elif player_num == 12:
            global player_12_scores
            player_12_scores += 1
            team1 = team1_selected.get()
            db1.execute(f'UPDATE {team1} SET scores = ? WHERE id =12',(player_12_scores,))
            db1.commit()
            total_point_A+=1
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_A = ? WHERE quarter = ?',(total_point_A,quarter))
            db2.commit()
            s_player_12.set(player_12_scores)
            total_score_A.set(total_point_A)
        
        #team B
        elif player_num == 13:
            global player_13_scores
            player_13_scores += 1
            team2 = team2_selected.get()
            db1.execute(f'UPDATE {team2} SET scores = ? WHERE id = 1',(player_13_scores,))
            db1.commit()
            total_point_B +=1
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_B = ? WHERE quarter = ?',(total_point_B,quarter))
            db2.commit()
            s_player_13.set(player_13_scores)
            total_score_B.set(total_point_B)
        

        elif player_num == 14:
            global player_14_scores
            player_14_scores += 1
            team2 = team2_selected.get()
            db1.execute(f'UPDATE {team2} SET scores = ? WHERE id = 2',(player_14_scores,))
            db1.commit()
            total_point_B +=1
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_B = ? WHERE quarter = ?',(total_point_B,quarter))
            db2.commit()
            s_player_14.set(player_14_scores)
            total_score_B.set(total_point_B)
            

        elif player_num == 15:
            global player_15_scores
            player_15_scores += 1
            team2 = team2_selected.get()
            db1.execute(f'UPDATE {team2} SET scores = ? WHERE id =3',(player_15_scores,))
            db1.commit()
            total_point_B +=1
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_B = ? WHERE quarter = ?',(total_point_B,quarter))
            db2.commit()
            s_player_15.set(player_15_scores)
            total_score_B.set(total_point_B)
            

        elif player_num == 16:
            global player_16_scores
            player_16_scores += 1
            team2 = team2_selected.get()
            db1.execute(f'UPDATE {team2} SET scores = ? WHERE id =4',(player_16_scores,))
            db1.commit()
            total_point_B +=1
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_B = ? WHERE quarter = ?',(total_point_B,quarter))
            db2.commit()
            s_player_16.set(player_16_scores)
            total_score_B.set(total_point_B)
        

        elif player_num == 17:
            global player_17_scores
            player_17_scores += 1
            team2 = team2_selected.get()
            db1.execute(f'UPDATE {team2} SET scores = ? WHERE id =5',(player_17_scores,))
            db1.commit()
            total_point_B +=1
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_B = ? WHERE quarter = ?',(total_point_B,quarter))
            db2.commit()
            s_player_17.set(player_17_scores)
            total_score_B.set(total_point_B)
        

        elif player_num == 18:
            global player_18_scores
            player_18_scores += 1
            team2 = team2_selected.get()
            db1.execute(f'UPDATE {team2} SET scores = ? WHERE id =6',(player_18_scores,))
            db1.commit()
            total_point_B +=1
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_B = ? WHERE quarter = ?',(total_point_B,quarter))
            db2.commit()
            s_player_18.set(player_18_scores)
            total_score_B.set(total_point_B)
            

        elif player_num == 19:
            global player_19_scores
            player_19_scores += 1
            team2 = team2_selected.get()
            db1.execute(f'UPDATE {team2} SET scores = ? WHERE id =7',(player_19_scores,))
            db1.commit()
            total_point_B +=1
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_B = ? WHERE quarter = ?',(total_point_B,quarter))
            db2.commit()
            s_player_19.set(player_19_scores)
            total_score_B.set(total_point_B)
        

        elif player_num == 20:
            global player_20_scores
            player_20_scores += 1
            team2 = team2_selected.get()
            db1.execute(f'UPDATE {team2} SET scores = ? WHERE id =8',(player_20_scores,))
            db1.commit()
            total_point_B +=1
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_B = ? WHERE quarter = ?',(total_point_B,quarter))
            db2.commit()
            s_player_20.set(player_20_scores)
            total_score_B.set(total_point_B)
            

        elif player_num == 21:
            global player_21_scores
            player_21_scores += 1
            team2 = team2_selected.get()
            db1.execute(f'UPDATE {team2} SET scores = ? WHERE id =9',(player_21_scores,))
            db1.commit()
            total_point_B +=1
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_B = ? WHERE quarter = ?',(total_point_B,quarter))
            db2.commit()
            s_player_21.set(player_21_scores)
            total_score_B.set(total_point_B)
            

        elif player_num == 22:
            global player_22_scores
            player_22_scores += 1
            team2 = team2_selected.get()
            db1.execute(f'UPDATE {team2} SET scores = ? WHERE id =10',(player_22_scores,))
            db1.commit()
            total_point_B +=1
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_B = ? WHERE quarter = ?',(total_point_B,quarter))
            db2.commit()
            s_player_22.set(player_22_scores)
            total_score_B.set(total_point_B)
            

        elif player_num == 23:
            global player_23_scores
            player_23_scores += 1
            team2 = team2_selected.get()
            db1.execute(f'UPDATE {team2} SET scores = ? WHERE id =11',(player_23_scores,))
            db1.commit()
            total_point_B+=1
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_B = ? WHERE quarter = ?',(total_point_B,quarter))
            db2.commit()
            s_player_23.set(player_23_scores)
            total_score_B.set(total_point_B)
            

        elif player_num == 24:
            global player_24_scores
            player_24_scores += 1
            team2 = team2_selected.get()
            db1.execute(f'UPDATE {team2} SET scores = ? WHERE id =12',(player_24_scores,))
            db1.commit()
            total_point_B +=1
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_B = ? WHERE quarter = ?',(total_point_B,quarter))
            db2.commit()
            s_player_24.set(player_24_scores)
            total_score_B.set(total_point_B)
            
        


    def on_click_score_two_point(player_num):
        global total_point_A
        global total_point_B
        

        if player_num == 1:
            global player_1_scores
            player_1_scores += 2
            team1 = team1_selected.get()
            db1.execute(f'UPDATE {team1} SET scores = ? WHERE id = 1',(player_1_scores,))
            db1.commit()
            total_point_A +=2
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_A = ? WHERE quarter = ?',(total_point_A,quarter))
            db2.commit()
            s_player_1.set(player_1_scores)
            total_score_A.set(total_point_A)

        elif player_num == 2:
            global player_2_scores
            player_2_scores += 2
            team1 = team1_selected.get()
            db1.execute(f'UPDATE {team1} SET scores = ? WHERE id = 2',(player_2_scores,))
            db1.commit()
            total_point_A+=2
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_A = ? WHERE quarter = ?',(total_point_A,quarter))
            db2.commit()
            s_player_2.set(player_2_scores)
            total_score_A.set(total_point_A)
            
            
        elif player_num == 3:
            global player_3_scores
            player_3_scores += 2
            team1 = team1_selected.get()
            db1.execute(f'UPDATE {team1} SET scores = ? WHERE id = 3',(player_3_scores,))
            db1.commit()
            total_point_A +=2
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_A = ? WHERE quarter = ?',(total_point_A,quarter))
            db2.commit()
            s_player_3.set(player_3_scores)
            total_score_A.set(total_point_A)
            

        elif player_num == 4:
            global player_4_scores
            player_4_scores += 2
            team1 = team1_selected.get()
            db1.execute(f'UPDATE {team1} SET scores = ? WHERE id = 4',(player_4_scores,))
            db1.commit()
            total_point_A +=2
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_A = ? WHERE quarter = ?',(total_point_A,quarter))
            db2.commit()
            s_player_4.set(player_4_scores)
            total_score_A.set(total_point_A)
        

        elif player_num == 5:
            global player_5_scores
            player_5_scores += 2
            team1 = team1_selected.get()
            db1.execute(f'UPDATE {team1} SET scores = ? WHERE id = 5',(player_5_scores,))
            db1.commit()
            total_point_A +=2
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_A = ? WHERE quarter = ?',(total_point_A,quarter))
            db2.commit()
            s_player_5.set(player_5_scores)
            total_score_A.set(total_point_A)
        

        elif player_num == 6:
            global player_6_scores
            player_6_scores += 2
            team1 = team1_selected.get()
            db1.execute(f'UPDATE {team1} SET scores = ? WHERE id = 6',(player_6_scores,))
            db1.commit()
            total_point_A += 2
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_A = ? WHERE quarter = ?',(total_point_A,quarter))
            db2.commit()
            s_player_6.set(player_6_scores)
            total_score_A.set(total_point_A)
        
        elif player_num == 7:
            global player_7_scores
            player_7_scores += 2
            team1 = team1_selected.get()
            db1.execute(f'UPDATE {team1} SET scores = ? WHERE id =7',(player_7_scores,))
            db1.commit()
            total_point_A +=2
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_A = ? WHERE quarter = ?',(total_point_A,quarter))
            db2.commit()
            s_player_7.set(player_7_scores)
            total_score_A.set(total_point_A)
        
        elif player_num == 8:
            global player_8_scores
            player_8_scores += 2
            team1 = team1_selected.get()
            db1.execute(f'UPDATE {team1} SET scores = ? WHERE id =8',(player_8_scores,))
            db1.commit()
            total_point_A +=2
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_A = ? WHERE quarter = ?',(total_point_A,quarter))
            db2.commit()
            s_player_8.set(player_8_scores)
            total_score_A.set(total_point_A)
        

        elif player_num == 9:
            global player_9_scores
            player_9_scores += 2
            team1 = team1_selected.get()
            db1.execute(f'UPDATE {team1} SET scores = ? WHERE id =9',(player_9_scores,))
            db1.commit()
            total_point_A +=2
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_A = ? WHERE quarter = ?',(total_point_A,quarter))
            db2.commit()
            s_player_9.set(player_9_scores)
            total_score_A.set(total_point_A)
            

        elif player_num == 10:
            global player_10_scores
            player_10_scores += 2
            team1 = team1_selected.get()
            db1.execute(f'UPDATE {team1} SET scores = ? WHERE id =10',(player_10_scores,))
            db1.commit()
            total_point_A+=2
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_A = ? WHERE quarter = ?',(total_point_A,quarter))
            db2.commit()
            s_player_10.set(player_10_scores)
            total_score_A.set(total_point_A)
        

        elif player_num == 11:
            global player_11_scores
            player_11_scores += 2
            team1 = team1_selected.get()
            db1.execute(f'UPDATE {team1} SET scores = ? WHERE id =11',(player_11_scores,))
            db1.commit()
            total_point_A +=2
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_A = ?WHERE quarter = ?',(total_point_A,quarter))
            db2.commit()
            s_player_11.set(player_11_scores)
            total_score_A.set(total_point_A)
        
        elif player_num == 12:
            global player_12_scores
            player_12_scores += 2
            team1 = team1_selected.get()
            db1.execute(f'UPDATE {team1} SET scores = ? WHERE id =12',(player_12_scores,))
            db1.commit()
            total_point_A+=2
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_A = ?WHERE quarter = ?',(total_point_A,quarter))
            db2.commit()
            s_player_12.set(player_12_scores)
            total_score_A.set(total_point_A)
        
        #team B
        
        elif player_num == 13:
            global player_13_scores
            player_13_scores += 2
            team2 = team2_selected.get()
            db1.execute(f'UPDATE {team2} SET scores = ? WHERE id =1',(player_13_scores,))
            db1.commit()
            total_point_B +=2
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_B = ? WHERE quarter = ?',(total_point_B,quarter))
            db2.commit()
            s_player_13.set(player_13_scores)
            total_score_B.set(total_point_B)
        

        elif player_num == 14:
            global player_14_scores
            player_14_scores += 2
            team2 = team2_selected.get()
            db1.execute(f'UPDATE {team2} SET scores = ? WHERE id =2',(player_14_scores,))
            db1.commit()
            total_point_B +=2
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_B = ? WHERE quarter = ?',(total_point_B,quarter))
            db2.commit()
            s_player_14.set(player_14_scores)
            total_score_B.set(total_point_B)
            

        elif player_num == 15:
            global player_15_scores
            player_15_scores += 2
            team2 = team2_selected.get()
            db1.execute(f'UPDATE {team2} SET scores = ? WHERE id =3',(player_15_scores,))
            db1.commit()
            total_point_B +=2
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_B = ? WHERE quarter = ?',(total_point_B,quarter))
            db2.commit()
            s_player_15.set(player_15_scores)
            total_score_B.set(total_point_B)
            

        elif player_num == 16:
            global player_16_scores
            player_16_scores += 2
            team2 = team2_selected.get()
            db1.execute(f'UPDATE {team2} SET scores = ? WHERE id =4',(player_16_scores,))
            db1.commit()
            total_point_B +=2
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_B = ? WHERE quarter = ?',(total_point_B,quarter))
            db2.commit()
            s_player_16.set(player_16_scores)
            total_score_B.set(total_point_B)
        

        elif player_num == 17:
            global player_17_scores
            player_17_scores += 2
            team2 = team2_selected.get()
            db1.execute(f'UPDATE {team2} SET scores = ? WHERE id =5',(player_17_scores,))
            db1.commit()
            total_point_B +=2
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_B = ? WHERE quarter = ?',(total_point_B,quarter))
            db2.commit()
            s_player_17.set(player_17_scores)
            total_score_B.set(total_point_B)
        

        elif player_num == 18:
            global player_18_scores
            player_18_scores += 2
            team2 = team2_selected.get()
            db1.execute(f'UPDATE {team2} SET scores = ? WHERE id =6',(player_18_scores,))
            db1.commit()
            total_point_B +=2
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_B = ? WHERE quarter = ?',(total_point_B,quarter))
            db2.commit()
            s_player_18.set(player_18_scores)
            total_score_B.set(total_point_B)
            

        elif player_num == 19:
            global player_19_scores
            player_19_scores += 2
            team2 = team2_selected.get()
            db1.execute(f'UPDATE {team2} SET scores = ? WHERE id =7 ',(player_19_scores,))
            db1.commit()
            total_point_B +=2
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_B = ? WHERE quarter = ?',(total_point_B,quarter))
            db2.commit()
            s_player_19.set(player_19_scores)
            total_score_B.set(total_point_B)
        

        elif player_num == 20:
            global player_20_scores
            player_20_scores += 2
            team2 = team2_selected.get()
            db1.execute(f'UPDATE {team2} SET scores = ? WHERE id =8',(player_20_scores,))
            db1.commit()
            total_point_B +=2
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_B = ? WHERE quarter = ?',(total_point_B,quarter))
            db2.commit()
            s_player_20.set(player_20_scores)
            total_score_B.set(total_point_B)
            

        elif player_num == 21:
            global player_21_scores
            player_21_scores += 2
            team2 = team2_selected.get()
            db1.execute(f'UPDATE {team2} SET scores = ? WHERE id =9',(player_21_scores,))
            db1.commit()
            total_point_B +=2
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_B = ? WHERE quarter = ?',(total_point_B,quarter))
            db2.commit()
            s_player_21.set(player_21_scores)
            total_score_B.set(total_point_B)
            

        elif player_num == 22:
            global player_22_scores
            player_22_scores += 2
            team2 = team2_selected.get()
            db1.execute(f'UPDATE {team2} SET scores = ? WHERE id =10',(player_22_scores,))
            db1.commit()
            total_point_B +=2
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_B = ? WHERE quarter = ?',(total_point_B,quarter))
            db2.commit()
            s_player_22.set(player_22_scores)
            total_score_B.set(total_point_B)
            

        elif player_num == 23:
            global player_23_scores
            player_23_scores += 2
            team2 = team2_selected.get()
            db1.execute(f'UPDATE {team2} SET scores = ? WHERE id =11',(player_23_scores,))
            db1.commit()
            total_point_B+=2
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_B = ? WHERE quarter = ?',(total_point_B,quarter))
            db2.commit()
            s_player_23.set(player_23_scores)
            total_score_B.set(total_point_B)
            

        elif player_num == 24:
            global player_24_scores
            player_24_scores += 2
            team2 = team2_selected.get()
            db1.execute(f'UPDATE {team2} SET scores = ? WHERE id =12',(player_24_scores,))
            db1.commit()
            total_point_B +=2
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_B = ? WHERE quarter = ?',(total_point_B,quarter))
            db2.commit()
            s_player_24.set(player_24_scores)
            total_score_B.set(total_point_B)
        


    def on_click_score_three_point(player_num):
        global total_point_A
        global total_point_B
        

        if player_num == 1:
            global player_1_scores
            player_1_scores += 3
            team1 = team1_selected.get()
            db1.execute(f'UPDATE {team1} SET scores = ? WHERE id =1',(player_1_scores,))
            db1.commit()
            total_point_A +=3
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_A = ? WHERE quarter = ?',(total_point_A,quarter))
            db2.commit()
            s_player_1.set(player_1_scores)
            total_score_A.set(total_point_A)

        elif player_num == 2:
            global player_2_scores
            player_2_scores += 3
            team1 = team1_selected.get()
            db1.execute(f'UPDATE {team1} SET scores = ? WHERE id =2',(player_2_scores,))
            db1.commit()
            total_point_A+=3
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_A = ? WHERE quarter = ?',(total_point_A,quarter))
            db2.commit()
            s_player_2.set(player_2_scores)
            total_score_A.set(total_point_A)
            
            
        elif player_num == 3:
            global player_3_scores
            player_3_scores += 3
            team1 = team1_selected.get()
            db1.execute(f'UPDATE {team1} SET scores = ? WHERE id =3',(player_3_scores,))
            db1.commit()
            total_point_A +=3
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_A = ? WHERE quarter = ?',(total_point_A,quarter))
            db2.commit()
            s_player_3.set(player_3_scores)
            total_score_A.set(total_point_A)
            

        elif player_num == 4:
            global player_4_scores
            player_4_scores += 3
            team1 = team1_selected.get()
            db1.execute(f'UPDATE {team1} SET scores = ? WHERE id =4',(player_4_scores,))
            db1.commit()
            total_point_A +=3
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_A = ? WHERE quarter = ?',(total_point_A,quarter))
            db2.commit()
            s_player_4.set(player_4_scores)
            total_score_A.set(total_point_A)
        

        elif player_num == 5:
            global player_5_scores
            player_5_scores += 3
            team1 = team1_selected.get()
            db1.execute(f'UPDATE {team1} SET scores = ? WHERE id =5',(player_5_scores,))
            db1.commit()
            total_point_A +=3
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_A = ? WHERE quarter = ?',(total_point_A,quarter))
            db2.commit()
            s_player_5.set(player_5_scores)
            total_score_A.set(total_point_A)
        

        elif player_num == 6:
            global player_6_scores
            player_6_scores += 3
            team1 = team1_selected.get()
            db1.execute(f'UPDATE {team1} SET scores = ? WHERE id =6',(player_6_scores,))
            db1.commit()
            total_point_A += 3
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_A = ? WHERE quarter = ?',(total_point_A,quarter))
            db2.commit()
            s_player_6.set(player_6_scores)
            total_score_A.set(total_point_A)
        
        elif player_num == 7:
            global player_7_scores
            player_7_scores += 3
            team1 = team1_selected.get()
            db1.execute(f'UPDATE {team1} SET scores = ? WHERE id =7',(player_7_scores,))
            db1.commit()
            total_point_A +=3
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_A = ? WHERE quarter = ?',(total_point_A,quarter))
            db2.commit()
            s_player_7.set(player_7_scores)
            total_score_A.set(total_point_A)
        
        elif player_num == 8:
            global player_8_scores
            player_8_scores += 3
            team1 = team1_selected.get()
            db1.execute(f'UPDATE {team1} SET scores = ? WHERE id =8',(player_8_scores,))
            db1.commit()
            total_point_A +=3
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_A = ? WHERE quarter = ?',(total_point_A,quarter))
            db2.commit()
            s_player_8.set(player_8_scores)
            total_score_A.set(total_point_A)
        

        elif player_num == 9:
            global player_9_scores
            player_9_scores += 3
            team1 = team1_selected.get()
            db1.execute(f'UPDATE {team1} SET scores = ? WHERE id =9',(player_9_scores,))
            db1.commit()
            total_point_A +=3
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_A = ? WHERE quarter = ?',(total_point_A,quarter))
            db2.commit()
            s_player_9.set(player_9_scores)
            total_score_A.set(total_point_A)
            

        elif player_num == 10:
            global player_10_scores
            player_10_scores += 3
            team1 = team1_selected.get()
            db1.execute(f'UPDATE {team1} SET scores = ? WHERE id =10',(player_10_scores,))
            db1.commit()
            total_point_A+=3
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_A = ? WHERE quarter = ?',(total_point_A,quarter))
            db2.commit()
            s_player_10.set(player_10_scores)
            total_score_A.set(total_point_A)
        

        elif player_num == 11:
            global player_11_scores
            player_11_scores += 3
            team1 = team1_selected.get()
            db1.execute(f'UPDATE {team1} SET scores = ? WHERE id =11',(player_11_scores,))
            db1.commit()
            total_point_A +=3
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_A = ? WHERE quarter = ?',(total_point_A,quarter))
            db2.commit()
            s_player_11.set(player_11_scores)
            total_score_A.set(total_point_A)
        

        elif player_num == 12:
            global player_12_scores
            player_12_scores += 3
            team1 = team1_selected.get()
            db1.execute(f'UPDATE {team1} SET scores = ? WHERE id =12',(player_12_scores,))
            db1.commit()
            total_point_A+=3
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_A = ? WHERE quarter = ?',(total_point_A,quarter))
            db2.commit()
            s_player_12.set(player_12_scores)
            total_score_A.set(total_point_A)
        

        #team B
        elif player_num == 13:
            global player_13_scores
            player_13_scores += 3
            team2 = team2_selected.get()
            db1.execute(f'UPDATE {team2} SET scores = ? WHERE id =1 ',(player_13_scores,))
            db1.commit()
            total_point_B +=3
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_B = ? WHERE quarter = ?',(total_point_B,quarter))
            db2.commit()
            s_player_13.set(player_13_scores)
            total_score_B.set(total_point_B)
        

        elif player_num == 14:
            global player_14_scores
            player_14_scores += 3
            team2 = team2_selected.get()
            db1.execute(f'UPDATE {team2} SET scores = ? WHERE id =2',(player_14_scores,))
            db1.commit()
            total_point_B +=3
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_B = ? WHERE quarter = ?',(total_point_B,quarter))
            db2.commit()
            s_player_14.set(player_14_scores)
            total_score_B.set(total_point_B)
            

        elif player_num == 15:
            global player_15_scores
            player_15_scores += 3
            team2 = team2_selected.get()
            db1.execute(f'UPDATE {team2} SET scores = ? WHERE id = 3',(player_15_scores,))
            db1.commit()
            total_point_B +=3
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_B = ? WHERE quarter = ?',(total_point_B,quarter))
            db2.commit()
            s_player_15.set(player_15_scores)
            total_score_B.set(total_point_B)
            

        elif player_num == 16:
            global player_16_scores
            player_16_scores += 3
            team2 = team2_selected.get()
            db1.execute(f'UPDATE {team2} SET scores = ? WHERE id =4',(player_16_scores,))
            db1.commit()
            total_point_B +=3
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_B = ? WHERE quarter = ?',(total_point_B,quarter))
            db2.commit()
            s_player_16.set(player_16_scores)
            total_score_B.set(total_point_B)
        

        elif player_num == 17:
            global player_17_scores
            player_17_scores += 3
            team2 = team2_selected.get()
            db1.execute(f'UPDATE {team2} SET scores = ? WHERE id =5',(player_17_scores,))
            db1.commit()
            total_point_B +=3
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_B = ? WHERE quarter = ?',(total_point_B,quarter))
            db2.commit()
            s_player_17.set(player_17_scores)
            total_score_B.set(total_point_B)
        

        elif player_num == 18:
            global player_18_scores
            player_18_scores += 3
            team2 = team2_selected.get()
            db1.execute(f'UPDATE {team2} SET scores = ? WHERE id =6',(player_18_scores,))
            db1.commit()
            total_point_B +=3
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_B = ? WHERE quarter = ?',(total_point_B,quarter))
            db2.commit()
            s_player_18.set(player_18_scores)
            total_score_B.set(total_point_B)
            

        elif player_num == 19:
            global player_19_scores
            player_19_scores += 3
            team2 = team2_selected.get()
            db1.execute(f'UPDATE {team2} SET scores = ? WHERE id =7',(player_19_scores,))
            db1.commit()
            total_point_B +=3
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_B = ? WHERE quarter = ?',(total_point_B,quarter))
            db2.commit()
            s_player_19.set(player_19_scores)
            total_score_B.set(total_point_B)
        

        elif player_num == 20:
            global player_20_scores
            player_20_scores += 3
            team2 = team2_selected.get()
            db1.execute(f'UPDATE {team2} SET scores = ? WHERE id =8',(player_20_scores,))
            db1.commit()
            total_point_B +=3
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_B = ? WHERE quarter = ?',(total_point_B,quarter))
            db2.commit()
            s_player_20.set(player_20_scores)
            total_score_B.set(total_point_B)
            

        elif player_num == 21:
            global player_21_scores
            player_21_scores += 3
            team2 = team2_selected.get()
            db1.execute(f'UPDATE {team2} SET scores = ? WHERE id =9',(player_21_scores,))
            db1.commit()
            total_point_B +=3
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_B = ? WHERE quarter = ?',(total_point_B,quarter))
            db2.commit()
            s_player_21.set(player_21_scores)
            total_score_B.set(total_point_B)
            

        elif player_num == 22:
            global player_22_scores
            player_22_scores += 3
            team2 = team2_selected.get()
            db1.execute(f'UPDATE {team2} SET scores = ? WHERE id =10',(player_22_scores,))
            db1.commit()
            total_point_B +=3
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_B = ? WHERE quarter = ?',(total_point_B,quarter))
            db2.commit()
            s_player_22.set(player_22_scores)
            total_score_B.set(total_point_B)
            

        elif player_num == 23:
            global player_23_scores
            player_23_scores += 3
            team2 = team2_selected.get()
            db1.execute(f'UPDATE {team2} SET scores = ? WHERE id =11',(player_23_scores,))
            db1.commit()
            total_point_B+=3
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_B = ? WHERE quarter = ?',(total_point_B,quarter))
            db2.commit()
            s_player_23.set(player_23_scores)
            total_score_B.set(total_point_B)
            

        elif player_num == 24:
            global player_24_scores
            player_24_scores += 3
            team2 = team2_selected.get()
            db1.execute(f'UPDATE {team2} SET scores = ? WHERE id =12',(player_24_scores,))
            db1.commit()
            total_point_B +=3
            name_of_match = name_match.get()
            db2.execute(f'UPDATE {name_of_match} SET total_scores_B = ? WHERE quarter = ?',(total_point_B,quarter))
            db2.commit()
            s_player_24.set(player_24_scores)
            total_score_B.set(total_point_B)

    def update_bg_A(*args):
        if fouls_point_A.get() == 5 :
            entry_total_A.config(bg="red")
        else:
            entry_total_A.config(bg="#f3f1fc")
    
    def update_bg_B(*args):
        if fouls_point_B.get() == 5 :
            entry_total_B.config(bg="red")
        else:
            entry_total_B.config(bg="#f3f1fc")

    

    #fouls
    entry_total_A = tk.Entry(master,textvariable=fouls_point_A,bg="#f3f1fc",font ='DBHelvethaicaX 20')
    entry_total_A.place(x=517, y =293)
    entry_total_A.config(width=3)
    fouls_point_A.trace("w", update_bg_A)

    entry_player_1 = Entry(master, textvariable=b_player_1)
    entry_player_1.place(x=590,y=400)
    entry_player_1.config(width=3)
    entry_player_2 = Entry(master, textvariable=b_player_2)
    entry_player_2.place(x=590,y=430)
    entry_player_2.config(width=3)
    entry_player_3 = Entry(master, textvariable=b_player_3)
    entry_player_3.place(x=590,y=460)
    entry_player_3.config(width=3)
    entry_player_4 = Entry(master, textvariable=b_player_4)
    entry_player_4.place(x=590,y=490)
    entry_player_4.config(width=3)
    entry_player_5 = Entry(master, textvariable=b_player_5)
    entry_player_5.place(x=590,y=520)
    entry_player_5.config(width=3)
    entry_player_6 = Entry(master, textvariable=b_player_6)
    entry_player_6.place(x=590,y=550)
    entry_player_6.config(width=3)
    entry_player_7 = Entry(master, textvariable=b_player_7)
    entry_player_7.place(x=590,y=580)
    entry_player_7.config(width=3)
    entry_player_8 = Entry(master, textvariable=b_player_8)
    entry_player_8.place(x=590,y=610)
    entry_player_8.config(width=3)
    entry_player_9 = Entry(master, textvariable=b_player_9)
    entry_player_9.place(x=590,y=640)
    entry_player_9.config(width=3)
    entry_player_10 = Entry(master, textvariable=b_player_10)
    entry_player_10.place(x=590,y=670)
    entry_player_10.config(width=3)
    entry_player_11 = Entry(master, textvariable=b_player_11)
    entry_player_11.place(x=590,y=700)
    entry_player_11.config(width=3)
    entry_player_12 = Entry(master, textvariable=b_player_12)
    entry_player_12.place(x=590,y=730)
    entry_player_12.config(width=3)

   
   
    button_reset = tk.Button(master,text="Next Q", command =reset_team_fouls,font="DBHelvethaicaX 20",bd=0)
    # button_reset.config(width=10)

    button_player_1 = Button(master, text="foul", command=lambda: on_click_fouls(1))
    button_player_2 = Button(master, text="foul", command=lambda: on_click_fouls(2))
    button_player_3 = Button(master, text="foul", command=lambda: on_click_fouls(3))
    button_player_4 = Button(master, text="foul", command=lambda: on_click_fouls(4))
    button_player_5 = Button(master, text="foul", command=lambda: on_click_fouls(5))
    button_player_6 = Button(master, text="foul", command=lambda: on_click_fouls(6))
    button_player_7 = Button(master, text="foul", command=lambda: on_click_fouls(7))
    button_player_8 = Button(master, text="foul", command=lambda: on_click_fouls(8))
    button_player_9 = Button(master, text="foul", command=lambda: on_click_fouls(9))
    button_player_10 = Button(master, text="foul", command=lambda: on_click_fouls(10))
    button_player_11 = Button(master, text="foul", command=lambda: on_click_fouls(11))
    button_player_12 = Button(master, text="foul", command=lambda: on_click_fouls(12))
    button_player_13 = Button(master, text="foul", command=lambda: on_click_fouls(13))
    button_player_14 = Button(master, text="foul", command=lambda: on_click_fouls(14))
    button_player_15 = Button(master, text="foul", command=lambda: on_click_fouls(15))
    button_player_16 = Button(master, text="foul", command=lambda: on_click_fouls(16))
    button_player_17 = Button(master, text="foul", command=lambda: on_click_fouls(17))
    button_player_18 = Button(master, text="foul", command=lambda: on_click_fouls(18))
    button_player_19 = Button(master, text="foul", command=lambda: on_click_fouls(19))
    button_player_20 = Button(master, text="foul", command=lambda: on_click_fouls(20))
    button_player_21 = Button(master, text="foul", command=lambda: on_click_fouls(21))
    button_player_22 = Button(master, text="foul", command=lambda: on_click_fouls(22))
    button_player_23 = Button(master, text="foul", command=lambda: on_click_fouls(23))
    button_player_24 = Button(master, text="foul", command=lambda: on_click_fouls(24))


    button_reset.place(x=1300, y =10)
    button_reset.config(width=10)
    button_player_1.place(x=550,y=400)
    button_player_1.config(width=4)
    button_player_2.place(x=550,y=430)
    button_player_2.config(width=4)
    button_player_3.place(x=550,y=460)
    button_player_3.config(width=4)
    button_player_4.place(x=550,y=490)
    button_player_4.config(width=4)
    button_player_5.place(x=550,y=520)
    button_player_5.config(width=4)
    button_player_6.place(x=550,y=550)
    button_player_6.config(width=4)
    button_player_7.place(x=550,y=580)
    button_player_7.config(width=4)
    button_player_8.place(x=550,y=610)
    button_player_8.config(width=4)
    button_player_9.place(x=550,y=640)
    button_player_9.config(width=4)
    button_player_10.place(x=550,y=670)
    button_player_10.config(width=4)
    button_player_11.place(x=550,y=700)
    button_player_11.config(width=4)
    button_player_12.place(x=550,y=730)
    button_player_12.config(width=4)


    button_player_1_scores = Button(master, text="1", command=lambda: on_click_score_one_point(1))
    button_player_1_scores.config(width=3)
    button_player_1_scores.place(x=380,y=400)
    button_player_2_scores = Button(master, text="1", command=lambda: on_click_score_one_point(2))
    button_player_2_scores.config(width=3)
    button_player_2_scores.place(x=380,y=430)
    button_player_3_scores = Button(master, text="1", command=lambda: on_click_score_one_point(3))
    button_player_3_scores.config(width=3)
    button_player_3_scores.place(x=380,y=460)
    button_player_4_scores = Button(master, text="1", command=lambda: on_click_score_one_point(4))
    button_player_4_scores.config(width=3)
    button_player_4_scores.place(x=380,y=490)
    button_player_5_scores = Button(master, text="1", command=lambda: on_click_score_one_point(5))
    button_player_5_scores.config(width=3)
    button_player_5_scores.place(x=380,y=520)
    button_player_6_scores = Button(master, text="1", command=lambda: on_click_score_one_point(6))
    button_player_6_scores.config(width=3)
    button_player_6_scores.place(x=380,y=550)
    button_player_7_scores= Button(master, text="1", command=lambda: on_click_score_one_point(7))
    button_player_7_scores.config(width=3)
    button_player_7_scores.place(x=380,y=580)
    button_player_8_scores = Button(master, text="1", command=lambda: on_click_score_one_point(8))
    button_player_8_scores.config(width=3)
    button_player_8_scores.place(x=380,y=610)
    button_player_9_scores = Button(master, text="1", command=lambda: on_click_score_one_point(9))
    button_player_9_scores.config(width=3)
    button_player_9_scores.place(x=380,y=640)
    button_player_10_scores = Button(master, text="1", command=lambda: on_click_score_one_point(10))
    button_player_10_scores.config(width=3)
    button_player_10_scores.place(x=380,y=670)
    button_player_11_scores = Button(master, text="1", command=lambda: on_click_score_one_point(11))
    button_player_11_scores.config(width=3)
    button_player_11_scores.place(x=380,y=700)
    button_player_12_scores = Button(master, text="1", command=lambda: on_click_score_one_point(12))
    button_player_12_scores.config(width=3)
    button_player_12_scores.place(x=380,y=730)
    button_player_13_scores = Button(master, text="1", command=lambda: on_click_score_one_point(13))
    button_player_14_scores = Button(master, text="1", command=lambda: on_click_score_one_point(14))
    button_player_15_scores = Button(master, text="1", command=lambda: on_click_score_one_point(15))
    button_player_16_scores = Button(master, text="1", command=lambda: on_click_score_one_point(16))
    button_player_17_scores = Button(master, text="1", command=lambda: on_click_score_one_point(17))
    button_player_18_scores = Button(master, text="1", command=lambda: on_click_score_one_point(18))
    button_player_19_scores = Button(master, text="1", command=lambda: on_click_score_one_point(19))
    button_player_20_scores = Button(master, text="1", command=lambda: on_click_score_one_point(20))
    button_player_21_scores = Button(master, text="1", command=lambda: on_click_score_one_point(21))
    button_player_22_scores = Button(master, text="1", command=lambda: on_click_score_one_point(22))
    button_player_23_scores = Button(master, text="1", command=lambda: on_click_score_one_point(23))
    button_player_24_scores = Button(master, text="1", command=lambda: on_click_score_one_point(24))
    
    

    button_player_1_scores_two = Button(master, text="2", command=lambda: on_click_score_two_point(1))
    button_player_1_scores_two.place(x=410,y=400)
    button_player_1_scores_two.config(width=3)
    button_player_2_scores_two = Button(master, text="2", command=lambda: on_click_score_two_point(2))
    button_player_2_scores_two.place(x=410,y=430)
    button_player_2_scores_two.config(width=3)
    button_player_3_scores_two = Button(master, text="2", command=lambda: on_click_score_two_point(3))
    button_player_3_scores_two.place(x=410,y=460)
    button_player_3_scores_two.config(width=3)
    button_player_4_scores_two = Button(master, text="2", command=lambda: on_click_score_two_point(4))
    button_player_4_scores_two.place(x=410,y=490)
    button_player_4_scores_two.config(width=3)
    button_player_5_scores_two = Button(master, text="2", command=lambda: on_click_score_two_point(5))
    button_player_5_scores_two.place(x=410,y=520)
    button_player_5_scores_two.config(width=3)
    button_player_6_scores_two = Button(master, text="2", command=lambda: on_click_score_two_point(6))
    button_player_6_scores_two.place(x=410,y=550)
    button_player_6_scores_two.config(width=3)
    button_player_7_scores_two= Button(master, text="2", command=lambda: on_click_score_two_point(7))
    button_player_7_scores_two.place(x=410,y=580)
    button_player_7_scores_two.config(width=3)
    button_player_8_scores_two = Button(master, text="2", command=lambda: on_click_score_two_point(8))
    button_player_8_scores_two.place(x=410,y=610)
    button_player_8_scores_two.config(width=3)
    button_player_9_scores_two = Button(master, text="2", command=lambda: on_click_score_two_point(9))
    button_player_9_scores_two.place(x=410,y=640)
    button_player_9_scores_two.config(width=3)
    button_player_10_scores_two = Button(master, text="2", command=lambda: on_click_score_two_point(10))
    button_player_10_scores_two.place(x=410,y=670)
    button_player_10_scores_two.config(width=3)
    button_player_11_scores_two = Button(master, text="2", command=lambda: on_click_score_two_point(11))
    button_player_11_scores_two.place(x=410,y=700)
    button_player_11_scores_two.config(width=3)
    button_player_12_scores_two = Button(master, text="2", command=lambda: on_click_score_two_point(12))
    button_player_12_scores_two.place(x=410,y=730)
    button_player_12_scores_two.config(width=3)
    button_player_13_scores_two = Button(master, text="2", command=lambda: on_click_score_two_point(13))
    button_player_14_scores_two = Button(master, text="2", command=lambda: on_click_score_two_point(14))
    button_player_15_scores_two = Button(master, text="2", command=lambda: on_click_score_two_point(15))
    button_player_16_scores_two = Button(master, text="2", command=lambda: on_click_score_two_point(16))
    button_player_17_scores_two = Button(master, text="2", command=lambda: on_click_score_two_point(17))
    button_player_18_scores_two = Button(master, text="2", command=lambda: on_click_score_two_point(18))
    button_player_19_scores_two = Button(master, text="2", command=lambda: on_click_score_two_point(19))
    button_player_20_scores_two = Button(master, text="2", command=lambda: on_click_score_two_point(20))
    button_player_21_scores_two = Button(master, text="2", command=lambda: on_click_score_two_point(21))
    button_player_22_scores_two = Button(master, text="2", command=lambda: on_click_score_two_point(22))
    button_player_23_scores_two = Button(master, text="2", command=lambda: on_click_score_two_point(23))
    button_player_24_scores_two = Button(master, text="2", command=lambda: on_click_score_two_point(24))



    button_player_1_scores_three = Button(master, text="3", command=lambda: on_click_score_three_point(1))
    button_player_1_scores_three.place(x=440,y=400)
    button_player_1_scores_three.config(width=3)
    button_player_2_scores_three = Button(master, text="3", command=lambda: on_click_score_three_point(2))
    button_player_2_scores_three.place(x=440,y=430)
    button_player_2_scores_three.config(width=3)
    button_player_3_scores_three = Button(master, text="3", command=lambda: on_click_score_three_point(3))
    button_player_3_scores_three.place(x=440,y=460)
    button_player_3_scores_three.config(width=3)
    button_player_4_scores_three = Button(master, text="3", command=lambda: on_click_score_three_point(4))
    button_player_4_scores_three.place(x=440,y=490)
    button_player_4_scores_three.config(width=3)
    button_player_5_scores_three = Button(master, text="3", command=lambda: on_click_score_three_point(5))
    button_player_5_scores_three.place(x=440,y=520)
    button_player_5_scores_three.config(width=3)
    button_player_6_scores_three = Button(master, text="3", command=lambda: on_click_score_three_point(6))
    button_player_6_scores_three.place(x=440,y=550)
    button_player_6_scores_three.config(width=3)
    button_player_7_scores_three= Button(master, text="3", command=lambda: on_click_score_three_point(7))
    button_player_7_scores_three.place(x=440,y=580)
    button_player_7_scores_three.config(width=3)
    button_player_8_scores_three = Button(master, text="3", command=lambda: on_click_score_three_point(8))
    button_player_8_scores_three.place(x=440,y=610)
    button_player_8_scores_three.config(width=3)
    button_player_9_scores_three = Button(master, text="3", command=lambda: on_click_score_three_point(9))
    button_player_9_scores_three.place(x=440,y=640)
    button_player_9_scores_three.config(width=3)
    button_player_10_scores_three = Button(master, text="3", command=lambda: on_click_score_three_point(10))
    button_player_10_scores_three.place(x=440,y=670)
    button_player_10_scores_three.config(width=3)
    button_player_11_scores_three = Button(master, text="3", command=lambda: on_click_score_three_point(11))
    button_player_11_scores_three.place(x=440,y=700)
    button_player_11_scores_three.config(width=3)
    button_player_12_scores_three = Button(master, text="3", command=lambda: on_click_score_three_point(12))
    button_player_12_scores_three.place(x=440,y=730)
    button_player_12_scores_three.config(width=3)
    button_player_13_scores_three = Button(master, text="3", command=lambda: on_click_score_three_point(13))
    button_player_14_scores_three = Button(master, text="3", command=lambda: on_click_score_three_point(14))
    button_player_15_scores_three = Button(master, text="3", command=lambda: on_click_score_three_point(15))
    button_player_16_scores_three = Button(master, text="3", command=lambda: on_click_score_three_point(16))
    button_player_17_scores_three = Button(master, text="3", command=lambda: on_click_score_three_point(17))
    button_player_18_scores_three = Button(master, text="3", command=lambda: on_click_score_three_point(18))
    button_player_19_scores_three = Button(master, text="3", command=lambda: on_click_score_three_point(19))
    button_player_20_scores_three = Button(master, text="3", command=lambda: on_click_score_three_point(20))
    button_player_21_scores_three = Button(master, text="3", command=lambda: on_click_score_three_point(21))
    button_player_22_scores_three = Button(master, text="3", command=lambda: on_click_score_three_point(22))
    button_player_23_scores_three = Button(master, text="3", command=lambda: on_click_score_three_point(23))
    button_player_24_scores_three = Button(master, text="3", command=lambda: on_click_score_three_point(24))


    entry_total_scores_A = tk.Entry(master,textvariable=total_score_A,bg='#212121', fg = 'white',font ='DBHelvethaicaX 35')
    entry_total_scores_A.place(x=635,y=80,height=50)
    entry_total_scores_A.config(width=3)
    entry_player_1_scores = Entry(master, textvariable=s_player_1,state='readonly')
    entry_player_1_scores.place(x=475,y=400)
    entry_player_1_scores.config(width=3)
    entry_player_2_scores = Entry(master, textvariable=s_player_2,state='readonly')
    entry_player_2_scores.place(x=475,y=430)
    entry_player_2_scores.config(width=3)
    entry_player_3_scores = Entry(master, textvariable=s_player_3,state='readonly')
    entry_player_3_scores.place(x=475,y=460)
    entry_player_3_scores.config(width=3)
    entry_player_4_scores = Entry(master, textvariable=s_player_4,state='readonly')
    entry_player_4_scores.place(x=475,y=490)
    entry_player_4_scores.config(width=3)
    entry_player_5_scores = Entry(master, textvariable=s_player_5,state='readonly')
    entry_player_5_scores.place(x=475,y=520)
    entry_player_5_scores.config(width=3)
    entry_player_6_scores = Entry(master, textvariable=s_player_6,state='readonly')
    entry_player_6_scores.place(x=475,y=550)
    entry_player_6_scores.config(width=3)
    entry_player_7_scores = Entry(master, textvariable=s_player_7,state='readonly')
    entry_player_7_scores.place(x=475,y=580)
    entry_player_7_scores.config(width=3)
    entry_player_8_scores = Entry(master, textvariable=s_player_8,state='readonly')
    entry_player_8_scores.place(x=475,y=610)
    entry_player_8_scores.config(width=3)
    entry_player_9_scores = Entry(master, textvariable=s_player_9,state='readonly')
    entry_player_9_scores.place(x=475,y=640)
    entry_player_9_scores.config(width=3)
    entry_player_10_scores = Entry(master, textvariable=s_player_10,state='readonly')
    entry_player_10_scores.place(x=475,y=670)
    entry_player_10_scores.config(width=3)
    entry_player_11_scores = Entry(master, textvariable=s_player_11,state='readonly')
    entry_player_11_scores.place(x=475,y=700)
    entry_player_11_scores.config(width=3)
    entry_player_12_scores = Entry(master, textvariable=s_player_12,state='readonly')
    entry_player_12_scores.place(x=475,y=730)
    entry_player_12_scores.config(width=3)



#show foul-team B
    entry_total_B = tk.Entry(master,textvariable=fouls_point_B,bg="#f3f1fc",font ='DBHelvethaicaX 20')
    entry_total_B.place(x=1225, y =293)
    entry_total_B.config(width=3)
    fouls_point_B.trace("w", update_bg_B)


    entry_player_13 = Entry(master, textvariable=b_player_13)
    entry_player_13.place(x=1295,y=400)
    entry_player_13.config(width=4)
    entry_player_14 = Entry(master, textvariable=b_player_14)
    entry_player_14.place(x=1295,y=430)
    entry_player_14.config(width=4)
    entry_player_15 = Entry(master, textvariable=b_player_15)
    entry_player_15.place(x=1295,y=460)
    entry_player_15.config(width=4)
    entry_player_16 = Entry(master, textvariable=b_player_16)
    entry_player_16.place(x=1295,y=490)
    entry_player_16.config(width=4)
    entry_player_17 = Entry(master, textvariable=b_player_17)
    entry_player_17.place(x=1295,y=520)
    entry_player_17.config(width=4)
    entry_player_18 = Entry(master, textvariable=b_player_18)
    entry_player_18.place(x=1295,y=550)
    entry_player_18.config(width=4)
    entry_player_19 = Entry(master, textvariable=b_player_19)
    entry_player_19.place(x=1295,y=580)
    entry_player_19.config(width=4)
    entry_player_20 = Entry(master, textvariable=b_player_20)
    entry_player_20.place(x=1295,y=610)
    entry_player_20.config(width=4)
    entry_player_21 = Entry(master, textvariable=b_player_21)
    entry_player_21.place(x=1295,y=640)
    entry_player_21.config(width=4)
    entry_player_22 = Entry(master, textvariable=b_player_22)
    entry_player_22.place(x=1295,y=670)
    entry_player_22.config(width=4)
    entry_player_23 = Entry(master, textvariable=b_player_23)
    entry_player_23.place(x=1295,y=700)
    entry_player_23.config(width=4)
    entry_player_24 = Entry(master, textvariable=b_player_24)
    entry_player_24.place(x=1295,y=730)
    entry_player_24.config(width=4)

    # button_reset = tk.Button(master,text="reset", command =reset_team_fouls,font="DBHelvethaicaX 20",bd=0)

    
    
    button_player_13.place(x=1255,y=400)
    button_player_14.place(x=1255,y=430)
    button_player_15.place(x=1255,y=460)
    button_player_16.place(x=1255,y=490)
    button_player_17.place(x=1255,y=520)
    button_player_18.place(x=1255,y=550)
    button_player_19.place(x=1255,y=580)
    button_player_20.place(x=1255,y=610)
    button_player_21.place(x=1255,y=640)
    button_player_22.place(x=1255,y=670)
    button_player_23.place(x=1255,y=700)
    button_player_24.place(x=1255,y=730)
    
    button_player_13.config(width=4)
    button_player_14.config(width=4)
    button_player_15.config(width=4)
    button_player_16.config(width=4)
    button_player_17.config(width=4)
    button_player_18.config(width=4)
    button_player_19.config(width=4)
    button_player_20.config(width=4)
    button_player_21.config(width=4)
    button_player_22.config(width=4)
    button_player_23.config(width=4)
    button_player_24.config(width=4)


    

    button_player_13_scores.place(x=1090,y=400)
    button_player_13_scores.config(width=3)
    button_player_14_scores.place(x=1090,y=430)
    button_player_14_scores.config(width=3)
    button_player_15_scores.place(x=1090,y=460)
    button_player_15_scores.config(width=3)
    button_player_16_scores.place(x=1090,y=490)
    button_player_16_scores.config(width=3)
    button_player_17_scores.place(x=1090,y=520)
    button_player_17_scores.config(width=3)
    button_player_18_scores.place(x=1090,y=550)
    button_player_18_scores.config(width=3)
    button_player_19_scores.place(x=1090,y=580)
    button_player_19_scores.config(width=3)
    button_player_20_scores.place(x=1090,y=610)
    button_player_20_scores.config(width=3)
    button_player_21_scores.place(x=1090,y=640)
    button_player_21_scores.config(width=3)
    button_player_22_scores.place(x=1090,y=670)
    button_player_22_scores.config(width=3)
    button_player_23_scores.place(x=1090,y=700)
    button_player_23_scores.config(width=3)
    button_player_24_scores.place(x=1090,y=730)
    button_player_24_scores.config(width=3)



    button_player_13_scores_two.place(x=1120,y=400)
    button_player_14_scores_two.place(x=1120,y=430)
    button_player_15_scores_two.place(x=1120,y=460)
    button_player_16_scores_two.place(x=1120,y=490)
    button_player_17_scores_two.place(x=1120,y=520)
    button_player_18_scores_two.place(x=1120,y=550)
    button_player_19_scores_two.place(x=1120,y=580)
    button_player_20_scores_two.place(x=1120,y=610)
    button_player_21_scores_two.place(x=1120,y=640)
    button_player_22_scores_two.place(x=1120,y=670)
    button_player_23_scores_two.place(x=1120,y=700)
    button_player_24_scores_two.place(x=1120,y=730)

    button_player_13_scores_two.config(width=3)
    button_player_14_scores_two.config(width=3)
    button_player_15_scores_two.config(width=3)
    button_player_16_scores_two.config(width=3)
    button_player_17_scores_two.config(width=3)
    button_player_18_scores_two.config(width=3)
    button_player_19_scores_two.config(width=3)
    button_player_20_scores_two.config(width=3)
    button_player_21_scores_two.config(width=3)
    button_player_22_scores_two.config(width=3)
    button_player_23_scores_two.config(width=3)
    button_player_24_scores_two.config(width=3)


    button_player_13_scores_three.place(x=1150,y=400)
    button_player_14_scores_three.place(x=1150,y=430)
    button_player_15_scores_three.place(x=1150,y=460)
    button_player_16_scores_three.place(x=1150,y=490)
    button_player_17_scores_three.place(x=1150,y=520)
    button_player_18_scores_three.place(x=1150,y=550)
    button_player_19_scores_three.place(x=1150,y=580)
    button_player_20_scores_three.place(x=1150,y=610)
    button_player_21_scores_three.place(x=1150,y=640)
    button_player_22_scores_three.place(x=1150,y=670)
    button_player_23_scores_three.place(x=1150,y=700)
    button_player_24_scores_three.place(x=1150,y=730)

    button_player_13_scores_three.config(width=3)
    button_player_14_scores_three.config(width=3)
    button_player_15_scores_three.config(width=3)
    button_player_16_scores_three.config(width=3)
    button_player_17_scores_three.config(width=3)
    button_player_18_scores_three.config(width=3)
    button_player_19_scores_three.config(width=3)
    button_player_20_scores_three.config(width=3)
    button_player_21_scores_three.config(width=3)
    button_player_22_scores_three.config(width=3)
    button_player_23_scores_three.config(width=3)
    button_player_24_scores_three.config(width=3)


    entry_total_scores_B = tk.Entry(master,textvariable=total_score_B,bg='#212121', fg = 'white',font ='DBHelvethaicaX 35')
    entry_total_scores_B.place(x=750,y=80,height=50)
    entry_total_scores_B.config(width=3)
    entry_player_13_scores = Entry(master, textvariable=s_player_13,state='readonly')
    entry_player_13_scores.place(x=1185,y=400)
    entry_player_14_scores = Entry(master, textvariable=s_player_14,state='readonly')
    entry_player_14_scores.place(x=1185,y=430)
    entry_player_15_scores = Entry(master, textvariable=s_player_15,state='readonly')
    entry_player_15_scores.place(x=1185,y=460)
    entry_player_16_scores = Entry(master, textvariable=s_player_16,state='readonly')
    entry_player_16_scores.place(x=1185,y=490)
    entry_player_17_scores = Entry(master, textvariable=s_player_17,state='readonly')
    entry_player_17_scores.place(x=1185,y=520)
    entry_player_18_scores = Entry(master, textvariable=s_player_18,state='readonly')
    entry_player_18_scores.place(x=1185,y=550)
    entry_player_19_scores = Entry(master, textvariable=s_player_19,state='readonly')
    entry_player_19_scores.place(x=1185,y=580)
    entry_player_20_scores = Entry(master, textvariable=s_player_20,state='readonly')
    entry_player_20_scores.place(x=1185,y=610)
    entry_player_21_scores = Entry(master, textvariable=s_player_21,state='readonly')
    entry_player_21_scores.place(x=1185,y=640)
    entry_player_22_scores = Entry(master, textvariable=s_player_22,state='readonly')
    entry_player_22_scores.place(x=1185,y=670)
    entry_player_23_scores = Entry(master, textvariable=s_player_23,state='readonly')
    entry_player_23_scores.place(x=1185,y=700)
    entry_player_24_scores = Entry(master, textvariable=s_player_24,state='readonly')
    entry_player_24_scores.place(x=1185,y=730)

    entry_player_13_scores.config(width=3)
    entry_player_14_scores.config(width=3)
    entry_player_15_scores.config(width=3)
    entry_player_16_scores.config(width=3)
    entry_player_17_scores.config(width=3)
    entry_player_18_scores.config(width=3)
    entry_player_19_scores.config(width=3)
    entry_player_20_scores.config(width=3)
    entry_player_21_scores.config(width=3)
    entry_player_22_scores.config(width=3)
    entry_player_23_scores.config(width=3)
    entry_player_24_scores.config(width=3)

    def destroyed():
        master.destroy


    button_finish = tk.Button(master, text="Finish", command=make_pdf,font="DBHelvethaicaX 20",bd=0)
    button_finish.place(x=1185,y=10)
    button_finish.config(width=10)

    

    master.mainloop()
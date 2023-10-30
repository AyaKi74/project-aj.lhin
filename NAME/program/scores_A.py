from tkinter import *
from PIL import Image, ImageTk
from tkinter.ttk import *
import sqlite3 
from tkinter import messagebox,simpledialog
from tkinter import font 


# team_1, team_2 = finish_botton()

conn = sqlite3.connect('teams.db')
db = conn.cursor()


    
team1 = None
team2 = None
foul_team = 5 
timeout_value = 0

total_fouls = 0
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

max_fouls = 5

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

total_point = 0


def tamlaew():
        
    root = Toplevel()
    root.geometry("1440x810")
    label_font = font.Font(size = 14)
    
    bg = Image.open(r"D:\Com\second\pyrhon\bas _score\ma01.png")
    bg = bg.resize((1440, 810), Image.ANTIALIAS)  # ปรับขนาดรูปให้ตรงกับหน้าต่างหลัก
    photo = ImageTk.PhotoImage(bg)
    canvas = Canvas(root, width=1440, height=810)
    canvas.pack()
    canvas.create_image(0, 0, anchor=NW, image=photo)
    
    
    def input_team():
        team1 = simpledialog.askstring("Input", "ชื่อทีม 1")
        team2 = simpledialog.askstring("Input", "ชื่อทีม 2")
        if team1 and team2:
            show_name_A(team1)
            show_name_B(team2)
            show_number_A(team1)
            show_number_B(team2)
            show_all_star_A(team1)
            show_all_star_B(team2)
        return team1,team2

    def show_name_A(team_1):
            if team_1:
                sql_cmd = f"SELECT player_name FROM {team_1}"
                for index, item in enumerate(db.execute(sql_cmd)):
                    Label(root, text=item,font=label_font).place(x=20, y=(index * 30) + 400)
                    
    def show_all_star_A(team1):
        label=Label(root, text = team1,font=label_font)
        label.place(x=400, y=110)
        label.config(background='#df5162')
        
    def show_all_star_B(team2):
        label2=Label(root, text = team2,font=label_font)
        label2.place(x=1020, y=110)
        label2.config(background='#3db2b8')
   
    def show_name_B(team_2):
            if team_2:
                sql_cmd = f"SELECT  player_name  FROM {team_2}"
                for index, item in enumerate(db.execute(sql_cmd)):
                    Label(root, text=item,font=label_font).place(x=800,y=(index * 30) + 400)
    
    def show_number_A(team1):
        sql_cmd = f'select player_number from {team1}'
        for index, item in enumerate(db.execute(sql_cmd)):
                    Label(root, text=item,font=label_font).place(x=120,y=(index * 30) + 400)
    
    def show_number_B(team2):
        sql_cmd = f'select player_number from {team2}'
        for index, item in enumerate(db.execute(sql_cmd)):
                    Label(root, text=item,font=label_font).place(x=900,y=(index * 30) + 400)
                   
                   

                

    button = Button(root, text="กรอกทีม", command=input_team)
    button.place(x=1000, y=10) 
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

    fouls_point  = IntVar()
    max_fouls_team = IntVar()


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
    total_score = IntVar()


    # b_one = IntVar()
    # b_two = IntVar()
    # b_three = IntVar()
    # b_total = IntVar()
   


        # def show_name():
        #     team_name = team_name_entry.g
        #     sql_cmd = f"select name from {team_name}"
        #     for item in db.execute(sql_cmd):
        #         Label(root, text=item).pack()

    # def show_number():
    #     sql_cmd = "select number from my_table"
    #     for item in db.execute(sql_cmd):
    #         Label(root, text = item).pack(anchor="w")

    # def add_one():
    #     global one 
    #     global total
    #     one += 1
    #     total += 1 
    #     b_total.set(total)
    #     b_one.set(one)




    def on_click_fouls_A(player_num):
        global max_fouls
        global total_fouls
        global foul_team
        

        
        if player_num == 1:
            global player_1_fouls
            player_1_fouls += 1
            b_player_1.set(player_1_fouls)
            fouls_point.set(total_fouls)
            
            if player_1_fouls >= max_fouls:
                button_player_1["state"] = DISABLED
                button_player_1_scores["state"] = DISABLED
                button_player_1_scores_two["state"] = DISABLED
                button_player_1_scores_three['state'] = DISABLED
                
            total_fouls += 1
            fouls_point.set(min(total_fouls, 5))  
            
            if total_fouls == foul_team:
                fouls_point.set(5)
            
            
            
        elif player_num == 2:
            global player_2_fouls
            player_2_fouls += 1
            b_player_2.set(player_2_fouls)
            fouls_point.set(total_fouls)
            if player_2_fouls >= max_fouls:
                button_player_2["state"] = DISABLED
                button_player_2_scores["state"] = DISABLED
                button_player_2_scores_two["state"] = DISABLED
                button_player_2_scores_three['state'] = DISABLED

            total_fouls += 1
            fouls_point.set(min(total_fouls, 5))
            if total_fouls == foul_team:
                fouls_point.set(5)
                
                
                
            
            
            
        elif player_num == 3:
            global player_3_fouls
            player_3_fouls += 1
            b_player_3.set(player_3_fouls)
            fouls_point.set(total_fouls)
            if player_3_fouls >= max_fouls:
                button_player_3["state"] = DISABLED
                button_player_3_scores["state"] = DISABLED
                button_player_3_scores_two["state"] = DISABLED
                button_player_3_scores_three['state'] = DISABLED
            total_fouls += 1
            fouls_point.set(min(total_fouls, 5))
            if total_fouls == foul_team:
                fouls_point.set(5)
                
        

        elif player_num == 4:
            global player_4_fouls
            
            player_4_fouls += 1
            b_player_4.set(player_4_fouls)
            fouls_point.set(total_fouls)
            if player_4_fouls >= max_fouls:
                button_player_4["state"] = DISABLED
                button_player_4_scores["state"] = DISABLED
                button_player_4_scores_two["state"] = DISABLED
                button_player_4_scores_three['state'] = DISABLED
            total_fouls += 1
            fouls_point.set(min(total_fouls, 5))
            if total_fouls == foul_team:
                fouls_point.set(5)
                
        

        elif player_num == 5:
            global player_5_fouls
            
            
            player_5_fouls += 1
            b_player_5.set(player_5_fouls)
            fouls_point.set(total_fouls)
            if player_5_fouls >= max_fouls:
                button_player_5["state"] = DISABLED
                button_player_5_scores["state"] = DISABLED
                button_player_5_scores_two["state"] = DISABLED
                button_player_5_scores_three['state'] = DISABLED
            total_fouls += 1
            fouls_point.set(min(total_fouls, 5))
            if total_fouls == foul_team:
                fouls_point.set(5)

        elif player_num == 6:
            global player_6_fouls
            
            
            player_6_fouls += 1
            b_player_6.set(player_6_fouls)
            fouls_point.set(total_fouls)
            if player_6_fouls >= max_fouls:
                button_player_6["state"] = DISABLED
                button_player_6_scores["state"] = DISABLED
                button_player_6_scores_two["state"] = DISABLED
                button_player_6_scores_three['state'] = DISABLED
            total_fouls += 1
            fouls_point.set(min(total_fouls, 5))
            if total_fouls == foul_team:
                fouls_point.set(5)
        

        elif player_num == 7:
            global player_7_fouls
            
            
            player_7_fouls += 1
            b_player_7.set(player_7_fouls)
            fouls_point.set(total_fouls)
            if player_7_fouls >= max_fouls:
                button_player_7["state"] = DISABLED
                button_player_7_scores["state"] = DISABLED
                button_player_7_scores_two["state"] = DISABLED
                button_player_7_scores_three['state'] = DISABLED
            total_fouls += 1
            fouls_point.set(min(total_fouls, 5))
            if total_fouls == foul_team:
                fouls_point.set(5)
        

        elif player_num == 8:
            global player_8_fouls
            
            
            player_8_fouls += 1
            b_player_8.set(player_8_fouls)
            fouls_point.set(total_fouls)
            if player_8_fouls >= max_fouls:
                button_player_8["state"] = DISABLED
                button_player_8_scores["state"] = DISABLED
                button_player_8_scores_two["state"] = DISABLED
                button_player_8_scores_three['state'] = DISABLED
            total_fouls += 1
            fouls_point.set(min(total_fouls, 5))
            if total_fouls == foul_team:
                fouls_point.set(5)

        elif player_num == 9:
            global player_9_fouls
            
            
            player_9_fouls += 1
            b_player_9.set(player_9_fouls)
            fouls_point.set(total_fouls)
            if player_9_fouls >= max_fouls:
                button_player_9["state"] = DISABLED
                button_player_9_scores["state"] = DISABLED
                button_player_9_scores_two["state"] = DISABLED
                button_player_9_scores_three['state'] = DISABLED
            total_fouls += 1
            fouls_point.set(min(total_fouls, 5))
            if total_fouls == foul_team:
                fouls_point.set(5)
        

        elif player_num == 10:
            global player_10_fouls
            
            
            player_10_fouls += 1
            b_player_10.set(player_10_fouls)
            fouls_point.set(total_fouls)
            if player_10_fouls >= max_fouls:
                button_player_10["state"] = DISABLED
                button_player_10_scores["state"] = DISABLED
                button_player_10_scores_two["state"] = DISABLED
                button_player_10_scores_three['state'] = DISABLED
            total_fouls += 1
            fouls_point.set(min(total_fouls, 5))
            if total_fouls == foul_team:
                fouls_point.set(5)
        

        elif player_num == 11:
            global player_11_fouls
            
            
            player_11_fouls += 1
            b_player_11.set(player_11_fouls)
            fouls_point.set(total_fouls)
            if player_11_fouls >= max_fouls:
                button_player_11["state"] = DISABLED
                button_player_11_scores["state"] = DISABLED
                button_player_11_scores_two["state"] = DISABLED
                button_player_11_scores_three['state'] = DISABLED
            total_fouls += 1
            fouls_point.set(min(total_fouls, 5))
            if total_fouls == foul_team:
                fouls_point.set(5)
        

        elif player_num == 12:
            global player_12_fouls
            
            
            player_12_fouls += 1
            b_player_12.set(player_12_fouls)
            fouls_point.set(total_fouls)
            if player_12_fouls >= max_fouls:
                button_player_12["state"] = DISABLED
                button_player_12_scores["state"] = DISABLED
                button_player_12_scores_two["state"] = DISABLED
                button_player_12_scores_three['state'] = DISABLED
            total_fouls += 1
            fouls_point.set(min(total_fouls, 5))
            if total_fouls == foul_team:
                fouls_point.set(5)
                
        
        
    # time-out
    def increase_timeout():
        global timeout_value
        if timeout_value < 4:
            timeout_value += 1
            timeout_label.config(text=f"{timeout_value}")
    
    
    timeout_label = Label(root, text="0")


    button = Button(root, text="", command=increase_timeout)

    timeout_label.place(x=110,y=300)
    
    button.place(x=140,y=300)
    button.config(width=3)
    #another team
        

    def reset_team_fouls():
        global total_fouls
        total_fouls = 0
        fouls_point.set(0)
        


    def on_click_score_one_point(player_num):
        global total_point
        

        if player_num == 1:
            global player_1_scores
            player_1_scores += 1
            total_point +=1
            s_player_1.set(player_1_scores)
            total_score.set(total_point)

        elif player_num == 2:
            global player_2_scores
            player_2_scores += 1
            total_point+=1
            s_player_2.set(player_2_scores)
            total_score.set(total_point)
            
            
        elif player_num == 3:
            global player_3_scores
            player_3_scores += 1
            total_point +=1
            s_player_3.set(player_3_scores)
            total_score.set(total_point)
            

        elif player_num == 4:
            global player_4_scores
            player_4_scores += 1
            total_point +=1
            s_player_4.set(player_4_scores)
            total_score.set(total_point)
        

        elif player_num == 5:
            global player_5_scores
            player_5_scores += 1
            total_point +=1
            s_player_5.set(player_5_scores)
            total_score.set(total_point)
        

        elif player_num == 6:
            global player_6_scores
            player_6_scores += 1
            total_point += 1 
            s_player_6.set(player_6_scores)
            total_score.set(total_point)
        
        elif player_num == 7:
            global player_7_scores
            player_7_scores += 1
            total_point +=1
            s_player_7.set(player_7_scores)
            total_score.set(total_point)
        
        elif player_num == 8:
            global player_8_scores
            player_8_scores += 1
            total_point +=1
            s_player_8.set(player_8_scores)
            total_score.set(total_point)
        

        elif player_num == 9:
            global player_9_scores
            player_9_scores += 1
            total_point +=1
            s_player_9.set(player_9_scores)
            total_score.set(total_point)
            

        elif player_num == 10:
            global player_10_scores
            player_10_scores += 1
            total_point+=1
            s_player_10.set(player_10_scores)
            total_score.set(total_point)
        

        elif player_num == 11:
            global player_11_scores
            player_11_scores += 1
            total_point +=1
            s_player_11.set(player_11_scores)
            total_score.set(total_point)
        

        elif player_num == 12:
            global player_12_scores
            player_12_scores += 1
            total_point+=1
            s_player_12.set(player_12_scores)
            total_score.set(total_point)
        
        


    def on_click_score_two_point(player_num):
        global total_point
        

        if player_num == 1:
            global player_1_scores
            player_1_scores += 2
            total_point +=2
            s_player_1.set(player_1_scores)
            total_score.set(total_point)

        elif player_num == 2:
            global player_2_scores
            player_2_scores += 2
            total_point+=2
            s_player_2.set(player_2_scores)
            total_score.set(total_point)
            
            
        elif player_num == 3:
            global player_3_scores
            player_3_scores += 2
            total_point +=2
            s_player_3.set(player_3_scores)
            total_score.set(total_point)
            

        elif player_num == 4:
            global player_4_scores
            player_4_scores += 2
            total_point +=2
            s_player_4.set(player_4_scores)
            total_score.set(total_point)
        

        elif player_num == 5:
            global player_5_scores
            player_5_scores += 2
            total_point +=2
            s_player_5.set(player_5_scores)
            total_score.set(total_point)
        

        elif player_num == 6:
            global player_6_scores
            player_6_scores += 2
            total_point += 2
            s_player_6.set(player_6_scores)
            total_score.set(total_point)
        
        elif player_num == 7:
            global player_7_scores
            player_7_scores += 2
            total_point +=2
            s_player_7.set(player_7_scores)
            total_score.set(total_point)
        
        elif player_num == 8:
            global player_8_scores
            player_8_scores += 2
            total_point +=2
            s_player_8.set(player_8_scores)
            total_score.set(total_point)
        

        elif player_num == 9:
            global player_9_scores
            player_9_scores += 2
            total_point +=2
            s_player_9.set(player_9_scores)
            total_score.set(total_point)
            

        elif player_num == 10:
            global player_10_scores
            player_10_scores += 2
            total_point+=2
            s_player_10.set(player_10_scores)
            total_score.set(total_point)
        

        elif player_num == 11:
            global player_11_scores
            player_11_scores += 2
            total_point +=2
            s_player_11.set(player_11_scores)
            total_score.set(total_point)
        
        elif player_num == 12:
            global player_12_scores
            player_12_scores += 2
            total_point+=2
            s_player_12.set(player_12_scores)
            total_score.set(total_point)
        





    def on_click_score_three_point(player_num):
        global total_point
        

        if player_num == 1:
            global player_1_scores
            player_1_scores += 3
            total_point +=3
            s_player_1.set(player_1_scores)
            total_score.set(total_point)

        elif player_num == 2:
            global player_2_scores
            player_2_scores += 3
            total_point+=3
            s_player_2.set(player_2_scores)
            total_score.set(total_point)
            
            
        elif player_num == 3:
            global player_3_scores
            player_3_scores += 3
            total_point +=3
            s_player_3.set(player_3_scores)
            total_score.set(total_point)
            

        elif player_num == 4:
            global player_4_scores
            player_4_scores += 3
            total_point +=3
            s_player_4.set(player_4_scores)
            total_score.set(total_point)
        

        elif player_num == 5:
            global player_5_scores
            player_5_scores += 3
            total_point +=3
            s_player_5.set(player_5_scores)
            total_score.set(total_point)
        

        elif player_num == 6:
            global player_6_scores
            player_6_scores += 3
            total_point += 3
            s_player_6.set(player_6_scores)
            total_score.set(total_point)
        
        elif player_num == 7:
            global player_7_scores
            player_7_scores += 3
            total_point +=3
            s_player_7.set(player_7_scores)
            total_score.set(total_point)
        
        elif player_num == 8:
            global player_8_scores
            player_8_scores += 3
            total_point +=3
            s_player_8.set(player_8_scores)
            total_score.set(total_point)
        

        elif player_num == 9:
            global player_9_scores
            player_9_scores += 3
            total_point +=3
            s_player_9.set(player_9_scores)
            total_score.set(total_point)
            

        elif player_num == 10:
            global player_10_scores
            player_10_scores += 3
            total_point+=3
            s_player_10.set(player_10_scores)
            total_score.set(total_point)
        

        elif player_num == 11:
            global player_11_scores
            player_11_scores += 3
            total_point +=3
            s_player_11.set(player_11_scores)
            total_score.set(total_point)
        

        elif player_num == 12:
            global player_12_scores
            player_12_scores += 3
            total_point+=3
            s_player_12.set(player_12_scores)
            total_score.set(total_point)
        


        elif player_num == 13:
            global player_13_scores
            player_13_scores += 3
            total_point +=3
            s_player_13.set(player_13_scores)
            total_score.set(total_point)
        

        elif player_num == 14:
            global player_14_scores
            player_14_scores += 3
            total_point +=3
            s_player_14.set(player_14_scores)
            total_score.set(total_point)
            

        elif player_num == 15:
            global player_15_scores
            player_15_scores += 3
            total_point +=3
            s_player_15.set(player_15_scores)
            total_score.set(total_point)
            

        elif player_num == 16:
            global player_16_scores
            player_16_scores += 3
            total_point +=3
            s_player_16.set(player_16_scores)
            total_score.set(total_point)
        

        elif player_num == 17:
            global player_17_scores
            player_17_scores += 3
            total_point +=3
            s_player_17.set(player_17_scores)
            total_score.set(total_point)
        

        elif player_num == 18:
            global player_18_scores
            player_18_scores += 3
            total_point +=3
            s_player_18.set(player_18_scores)
            total_score.set(total_point)
            

        elif player_num == 19:
            global player_19_scores
            player_19_scores += 3
            total_point +=3
            s_player_19.set(player_19_scores)
            total_score.set(total_point)
        

        elif player_num == 20:
            global player_20_scores
            player_20_scores += 3
            total_point +=3
            s_player_20.set(player_20_scores)
            total_score.set(total_point)
            

        elif player_num == 21:
            global player_21_scores
            player_21_scores += 3
            total_point +=3
            s_player_21.set(player_21_scores)
            total_score.set(total_point)
            

        elif player_num == 22:
            global player_22_scores
            player_22_scores += 3
            total_point +=3
            s_player_22.set(player_22_scores)
            total_score.set(total_point)
            

        elif player_num == 23:
            global player_23_scores
            player_23_scores += 3
            total_point+=3
            s_player_23.set(player_23_scores)
            total_score.set(total_point)
            

        elif player_num == 24:
            global player_24_scores
            player_24_scores += 3
            total_point +=3
            s_player_24.set(player_24_scores)
            total_score.set(total_point)
                
    
    entry_total = Entry(root,textvariable=fouls_point)
    entry_total = Entry(root, textvariable=fouls_point)
    entry_total.pack()
    
    entry_player_1 = Entry(root, textvariable=b_player_1)
    entry_player_1.place()
    entry_player_2 = Entry(root, textvariable=b_player_2)
    entry_player_2.place()
    entry_player_3 = Entry(root, textvariable=b_player_3)
    entry_player_3.place()
    entry_player_4 = Entry(root, textvariable=b_player_4)
    entry_player_4.place()
    entry_player_5 = Entry(root, textvariable=b_player_5)
    entry_player_5.place()
    entry_player_6 = Entry(root, textvariable=b_player_6)
    entry_player_6.place()
    entry_player_7 = Entry(root, textvariable=b_player_7)
    entry_player_7.place()
    entry_player_8 = Entry(root, textvariable=b_player_8)
    entry_player_8.place()
    entry_player_9 = Entry(root, textvariable=b_player_9)
    entry_player_9.place()
    entry_player_10 = Entry(root, textvariable=b_player_10)
    entry_player_10.place()
    entry_player_11 = Entry(root, textvariable=b_player_11)
    entry_player_11.place()
    entry_player_12 = Entry(root, textvariable=b_player_12)
    entry_player_12.place()

    button_reset = Button(root,text="reset", command =reset_team_fouls)

    button_player_1 = Button(root, text="foul", command=lambda: on_click_fouls_A(1))
    button_player_2 = Button(root, text="foul", command=lambda: on_click_fouls_A(2))
    button_player_3 = Button(root, text="foul", command=lambda: on_click_fouls_A(3))
    button_player_4 = Button(root, text="foul", command=lambda: on_click_fouls_A(4))
    button_player_5 = Button(root, text="foul", command=lambda: on_click_fouls_A(5))
    button_player_6 = Button(root, text="foul", command=lambda: on_click_fouls_A(6))
    button_player_7 = Button(root, text="foul", command=lambda: on_click_fouls_A(7))
    button_player_8 = Button(root, text="foul", command=lambda: on_click_fouls_A(8))
    button_player_9 = Button(root, text="foul", command=lambda: on_click_fouls_A(9))
    button_player_10 = Button(root, text="foul", command=lambda: on_click_fouls_A(10))
    button_player_11 = Button(root, text="foul", command=lambda: on_click_fouls_A(11))
    button_player_12 = Button(root, text="foul", command=lambda: on_click_fouls_A(12))



    # button_reset.pack()
    # button_player_1.pack()
    # button_player_2.pack()
    # button_player_3.pack()
    # button_player_4.pack()
    # button_player_5.pack()
    # button_player_6.pack()
    # button_player_7.pack()
    # button_player_8.pack()
    # button_player_9.pack()
    # button_player_10.pack()
    # button_player_11.pack()
    # button_player_12.pack()



    button_player_1_scores = Button(root, text="1", command=lambda: on_click_score_one_point(1))
    button_player_1_scores.config(width=3)
    button_player_1_scores.place(x=350,y=400)
    button_player_2_scores = Button(root, text="1", command=lambda: on_click_score_one_point(2))
    button_player_2_scores.config(width=3)
    button_player_2_scores.place(x=350,y=430)
    button_player_3_scores = Button(root, text="1", command=lambda: on_click_score_one_point(3))
    button_player_3_scores.config(width=3)
    button_player_3_scores.place(x=350,y=460)
    button_player_4_scores = Button(root, text="1", command=lambda: on_click_score_one_point(4))
    button_player_4_scores.config(width=3)
    button_player_4_scores.place(x=350,y=490)
    button_player_5_scores = Button(root, text="1", command=lambda: on_click_score_one_point(5))
    button_player_5_scores.config(width=3)
    button_player_5_scores.place(x=350,y=520)
    button_player_6_scores = Button(root, text="1", command=lambda: on_click_score_one_point(6))
    button_player_6_scores.config(width=3)
    button_player_6_scores.place(x=350,y=550)
    button_player_7_scores= Button(root, text="1", command=lambda: on_click_score_one_point(7))
    button_player_7_scores.config(width=3)
    button_player_7_scores.place(x=350,y=580)
    button_player_8_scores = Button(root, text="1", command=lambda: on_click_score_one_point(8))
    button_player_8_scores.config(width=3)
    button_player_8_scores.place(x=350,y=610)
    button_player_9_scores = Button(root, text="1", command=lambda: on_click_score_one_point(9))
    button_player_9_scores.config(width=3)
    button_player_9_scores.place(x=350,y=640)
    button_player_10_scores = Button(root, text="1", command=lambda: on_click_score_one_point(10))
    button_player_10_scores.config(width=3)
    button_player_10_scores.place(x=350,y=670)
    button_player_11_scores = Button(root, text="1", command=lambda: on_click_score_one_point(11))
    button_player_11_scores.config(width=3)
    button_player_11_scores.place(x=350,y=700)
    button_player_12_scores = Button(root, text="1", command=lambda: on_click_score_one_point(12))
    button_player_12_scores.config(width=3)
    button_player_12_scores.place(x=350,y=730)
    
   

    button_player_1_scores_two = Button(root, text="2", command=lambda: on_click_score_two_point(1))
    button_player_1_scores_two.place(x=380,y=400)
    button_player_1_scores_two.config(width=3)
    button_player_2_scores_two = Button(root, text="2", command=lambda: on_click_score_two_point(2))
    button_player_2_scores_two.place(x=380,y=430)
    button_player_2_scores_two.config(width=3)
    button_player_3_scores_two = Button(root, text="2", command=lambda: on_click_score_two_point(3))
    button_player_3_scores_two.place(x=380,y=460)
    button_player_3_scores_two.config(width=3)
    button_player_4_scores_two = Button(root, text="2", command=lambda: on_click_score_two_point(4))
    button_player_4_scores_two.place(x=380,y=490)
    button_player_4_scores_two.config(width=3)
    button_player_5_scores_two = Button(root, text="2", command=lambda: on_click_score_two_point(5))
    button_player_5_scores_two.place(x=380,y=520)
    button_player_5_scores_two.config(width=3)
    button_player_6_scores_two = Button(root, text="2", command=lambda: on_click_score_two_point(6))
    button_player_6_scores_two.place(x=380,y=550)
    button_player_6_scores_two.config(width=3)
    button_player_7_scores_two= Button(root, text="2", command=lambda: on_click_score_two_point(7))
    button_player_7_scores_two.place(x=380,y=580)
    button_player_7_scores_two.config(width=3)
    button_player_8_scores_two = Button(root, text="2", command=lambda: on_click_score_two_point(8))
    button_player_8_scores_two.place(x=380,y=610)
    button_player_8_scores_two.config(width=3)
    button_player_9_scores_two = Button(root, text="2", command=lambda: on_click_score_two_point(9))
    button_player_9_scores_two.place(x=380,y=640)
    button_player_9_scores_two.config(width=3)
    button_player_10_scores_two = Button(root, text="2", command=lambda: on_click_score_two_point(10))
    button_player_10_scores_two.place(x=380,y=670)
    button_player_10_scores_two.config(width=3)
    button_player_11_scores_two = Button(root, text="2", command=lambda: on_click_score_two_point(11))
    button_player_11_scores_two.place(x=380,y=700)
    button_player_11_scores_two.config(width=3)
    button_player_12_scores_two = Button(root, text="2", command=lambda: on_click_score_two_point(12))
    button_player_12_scores_two.place(x=380,y=730)
    button_player_12_scores_two.config(width=3)


    button_player_1_scores_three = Button(root, text="3", command=lambda: on_click_score_three_point(1))
    button_player_1_scores_three.place(x=410,y=400)
    button_player_1_scores_three.config(width=3)
    button_player_2_scores_three = Button(root, text="3", command=lambda: on_click_score_three_point(2))
    button_player_2_scores_three.place(x=410,y=430)
    button_player_2_scores_three.config(width=3)
    button_player_3_scores_three = Button(root, text="3", command=lambda: on_click_score_three_point(3))
    button_player_3_scores_three.place(x=410,y=460)
    button_player_3_scores_three.config(width=3)
    button_player_4_scores_three = Button(root, text="3", command=lambda: on_click_score_three_point(4))
    button_player_4_scores_three.place(x=410,y=490)
    button_player_4_scores_three.config(width=3)
    button_player_5_scores_three = Button(root, text="3", command=lambda: on_click_score_three_point(5))
    button_player_5_scores_three.place(x=410,y=520)
    button_player_5_scores_three.config(width=3)
    button_player_6_scores_three = Button(root, text="3", command=lambda: on_click_score_three_point(6))
    button_player_6_scores_three.place(x=410,y=550)
    button_player_6_scores_three.config(width=3)
    button_player_7_scores_three= Button(root, text="3", command=lambda: on_click_score_three_point(7))
    button_player_7_scores_three.place(x=410,y=580)
    button_player_7_scores_three.config(width=3)
    button_player_8_scores_three = Button(root, text="3", command=lambda: on_click_score_three_point(8))
    button_player_8_scores_three.place(x=410,y=610)
    button_player_8_scores_three.config(width=3)
    button_player_9_scores_three = Button(root, text="3", command=lambda: on_click_score_three_point(9))
    button_player_9_scores_three.place(x=410,y=640)
    button_player_9_scores_three.config(width=3)
    button_player_10_scores_three = Button(root, text="3", command=lambda: on_click_score_three_point(10))
    button_player_10_scores_three.place(x=410,y=670)
    button_player_10_scores_three.config(width=3)
    button_player_11_scores_three = Button(root, text="3", command=lambda: on_click_score_three_point(11))
    button_player_11_scores_three.place(x=410,y=700)
    button_player_11_scores_three.config(width=3)
    button_player_12_scores_three = Button(root, text="3", command=lambda: on_click_score_three_point(12))
    button_player_12_scores_three.place(x=410,y=730)
    button_player_12_scores_three.config(width=3)


    entry_total_scores = Entry(root,textvariable=total_score,state='readonly')
    entry_total_scores.place(x=650,y=20)
    entry_total_scores.config(width=3)
    entry_player_1_scores = Entry(root, textvariable=s_player_1,state='readonly')
    entry_player_1_scores.place(x=500,y=400)
    entry_player_1_scores.config(width=3)
    entry_player_2_scores = Entry(root, textvariable=s_player_2,state='readonly')
    entry_player_2_scores.place(x=500,y=430)
    entry_player_2_scores.config(width=3)
    entry_player_3_scores = Entry(root, textvariable=s_player_3,state='readonly')
    entry_player_3_scores.place(x=500,y=460)
    entry_player_3_scores.config(width=3)
    entry_player_4_scores = Entry(root, textvariable=s_player_4,state='readonly')
    entry_player_4_scores.place(x=500,y=490)
    entry_player_4_scores.config(width=3)
    entry_player_5_scores = Entry(root, textvariable=s_player_5,state='readonly')
    entry_player_5_scores.place(x=500,y=520)
    entry_player_5_scores.config(width=3)
    entry_player_6_scores = Entry(root, textvariable=s_player_6,state='readonly')
    entry_player_6_scores.place(x=500,y=550)
    entry_player_6_scores.config(width=3)
    entry_player_7_scores = Entry(root, textvariable=s_player_7,state='readonly')
    entry_player_7_scores.place(x=500,y=580)
    entry_player_7_scores.config(width=3)
    entry_player_8_scores = Entry(root, textvariable=s_player_8,state='readonly')
    entry_player_8_scores.place(x=500,y=610)
    entry_player_8_scores.config(width=3)
    entry_player_9_scores = Entry(root, textvariable=s_player_9,state='readonly')
    entry_player_9_scores.place(x=500,y=640)
    entry_player_9_scores.config(width=3)
    entry_player_10_scores = Entry(root, textvariable=s_player_10,state='readonly')
    entry_player_10_scores.place(x=500,y=670)
    entry_player_10_scores.config(width=3)
    entry_player_11_scores = Entry(root, textvariable=s_player_11,state='readonly')
    entry_player_11_scores.place(x=500,y=700)
    entry_player_11_scores.config(width=3)
    entry_player_12_scores = Entry(root, textvariable=s_player_12,state='readonly')
    entry_player_12_scores.place(x=500,y=730)
    entry_player_12_scores.config(width=3)


    root.mainloop()
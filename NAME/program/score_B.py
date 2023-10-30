from tkinter import *
import sqlite3 
from main_fisrt import finish_botton

conn = sqlite3.connect('my_database.db')
db = conn.cursor()


    
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
max_fouls = 5

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
total_point = 0

root = Tk()
root.geometry("1440x810")

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
fouls_point  = IntVar()

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


def create_team_table(team_name):
    conn.execute(f'''CREATE TABLE IF NOT EXISTS {team_name}
                 (player_id_a TEXT PRIMARY KEY, 
                  player_name_a TEXT,
                  player_number_a INTEGER,
                  position_a TEXT)''')
    db.commit()

def show_name():
    sql_cmd = "select name from my_table"
    for item in db.execute(sql_cmd):
        Label(root, text=item).pack()

def show_number():
    sql_cmd = "select number from my_table"
    for item in db.execute(sql_cmd):
        Label(root, text = item).pack(anchor="w")


def on_click_fouls_B(player_num):
    global max_fouls
    if player_num == 13:
        global player_13_fouls
        
        total_fouls += 1 
        player_13_fouls += 1
        b_player_13.set(player_13_fouls)
        fouls_point.set(total_fouls)
        if player_13_fouls >= max_fouls:
            button_player_13["state"] = DISABLED
            button_player_13_scores["state"] = DISABLED
            button_player_13_scores_two["state"] = DISABLED
            button_player_13_scores_three['state'] = DISABLED

    elif player_num == 14:
        global player_14_fouls
        
        total_fouls += 1 
        player_14_fouls += 1
        b_player_14.set(player_14_fouls)
        fouls_point.set(total_fouls)
        if player_14_fouls >= max_fouls:
            button_player_14["state"] = DISABLED
            button_player_14_scores["state"] = DISABLED
            button_player_14_scores_two["state"] = DISABLED
            button_player_14_scores_three['state'] = DISABLED

    elif player_num == 15:
        global player_15_fouls
        
        total_fouls += 1 
        player_15_fouls += 1
        b_player_15.set(player_15_fouls)
        fouls_point.set(total_fouls)
        if player_15_fouls >= max_fouls:
            button_player_15["state"] = DISABLED
            button_player_15_scores["state"] = DISABLED
            button_player_15_scores_two["state"] = DISABLED
            button_player_15_scores_three['state'] = DISABLED

    elif player_num == 16:
        global player_16_fouls
        
        total_fouls += 1 
        player_16_fouls += 1
        b_player_16.set(player_16_fouls)
        fouls_point.set(total_fouls)
        if player_16_fouls >= max_fouls:
            button_player_16["state"] = DISABLED
            button_player_16_scores["state"] = DISABLED
            button_player_16_scores_two["state"] = DISABLED
            button_player_16_scores_three['state'] = DISABLED

    elif player_num == 17:
        global player_17_fouls
        
        total_fouls += 1 
        player_17_fouls += 1
        b_player_17.set(player_17_fouls)
        fouls_point.set(total_fouls)
        if player_17_fouls >= max_fouls:
            button_player_17["state"] = DISABLED
            button_player_17_scores["state"] = DISABLED
            button_player_17_scores_two["state"] = DISABLED
            button_player_17_scores_three['state'] = DISABLED

    elif player_num == 18:
        global player_18_fouls
        
        total_fouls += 1 
        player_18_fouls += 1
        b_player_18.set(player_18_fouls)
        fouls_point.set(total_fouls)
        if player_18_fouls >= max_fouls:
            button_player_18["state"] = DISABLED
            button_player_18_scores["state"] = DISABLED
            button_player_18_scores_two["state"] = DISABLED
            button_player_18_scores_three['state'] = DISABLED

    elif player_num == 19:
        global player_19_fouls
        
        total_fouls += 1 
        player_19_fouls += 1
        b_player_19.set(player_19_fouls)
        fouls_point.set(total_fouls)
        if player_19_fouls >= max_fouls:
                button_player_19["state"] = DISABLED
                button_player_19_scores["state"] = DISABLED
                button_player_19_scores_two["state"] = DISABLED
                button_player_19_scores_three['state'] = DISABLED

    elif player_num == 20:
        global player_20_fouls
        
        total_fouls += 1 
        player_20_fouls += 1
        b_player_20.set(player_20_fouls)
        fouls_point.set(total_fouls)
        if player_20_fouls >= max_fouls:
            button_player_20["state"] = DISABLED
            button_player_20_scores["state"] = DISABLED
            button_player_20_scores_two["state"] = DISABLED
            button_player_20_scores_three['state'] = DISABLED
            

    elif player_num == 21:
        global player_21_fouls
        
        total_fouls += 1 
        player_21_fouls += 1
        b_player_21.set(player_21_fouls)
        fouls_point.set(total_fouls)
        if player_21_fouls >= max_fouls:
            button_player_21["state"] = DISABLED
            button_player_21_scores["state"] = DISABLED
            button_player_21_scores_two["state"] = DISABLED
            button_player_21_scores_three['state'] = DISABLED

    elif player_num == 22:
        global player_22_fouls
        
        total_fouls += 1 
        player_22_fouls += 1
        b_player_22.set(player_22_fouls)
        fouls_point.set(total_fouls)
        if player_22_fouls >= max_fouls:
            button_player_22["state"] = DISABLED
            button_player_22_scores["state"] = DISABLED
            button_player_22_scores_two["state"] = DISABLED
            button_player_22_scores_three['state'] = DISABLED

    elif player_num == 23:
        global player_23_fouls
        
        total_fouls += 1 
        player_23_fouls += 1
        b_player_23.set(player_23_fouls)
        fouls_point.set(total_fouls)
        if player_23_fouls >= max_fouls:
            button_player_23["state"] = DISABLED
            button_player_23_scores["state"] = DISABLED
            button_player_23_scores_two["state"] = DISABLED
            button_player_23_scores_three['state'] = DISABLED

    elif player_num == 24:
        global player_24_fouls
        
        total_fouls += 1 
        player_24_fouls += 1
        b_player_24.set(player_24_fouls)
        fouls_point.set(total_fouls)
        if player_24_fouls >= max_fouls:
            button_player_24["state"] = DISABLED
            button_player_24_scores["state"] = DISABLED
            button_player_24_scores_two["state"] = DISABLED
            button_player_24_scores_three['state'] = DISABLED


def reset_team_fouls():
    global total_fouls
    total_fouls = 0
    fouls_point.set(0)


def on_click_score_one_point(player_num):
    global total_point
    if player_num == 13:
        global player_13_scores
        player_13_scores += 1
        total_point +=1
        s_player_13.set(player_13_scores)
        total_score.set(total_point)
       

    elif player_num == 14:
        global player_14_scores
        player_14_scores += 1
        total_point +=1
        s_player_14.set(player_14_scores)
        total_score.set(total_point)
        

    elif player_num == 15:
        global player_15_scores
        player_15_scores += 1
        total_point +=1
        s_player_15.set(player_15_scores)
        total_score.set(total_point)
        

    elif player_num == 16:
        global player_16_scores
        player_16_scores += 1
        total_point +=1
        s_player_16.set(player_16_scores)
        total_score.set(total_point)
       

    elif player_num == 17:
        global player_17_scores
        player_17_scores += 1
        total_point +=1
        s_player_17.set(player_17_scores)
        total_score.set(total_point)
       

    elif player_num == 18:
        global player_18_scores
        player_18_scores += 1
        total_point +=1
        s_player_18.set(player_18_scores)
        total_score.set(total_point)
        

    elif player_num == 19:
        global player_19_scores
        player_19_scores += 1
        total_point +=1
        s_player_19.set(player_19_scores)
        total_score.set(total_point)
       

    elif player_num == 20:
        global player_20_scores
        player_20_scores += 1
        total_point +=1
        s_player_20.set(player_20_scores)
        total_score.set(total_point)
        

    elif player_num == 21:
        global player_21_scores
        player_21_scores += 1
        total_point +=1
        s_player_21.set(player_21_scores)
        total_score.set(total_point)
        

    elif player_num == 22:
        global player_22_scores
        player_22_scores += 1
        total_point +=1
        s_player_22.set(player_22_scores)
        total_score.set(total_point)
        

    elif player_num == 23:
        global player_23_scores
        player_23_scores += 1
        total_point+=1
        s_player_23.set(player_23_scores)
        total_score.set(total_point)
        

    elif player_num == 24:
        global player_24_scores
        player_24_scores += 1
        total_point +=1
        s_player_24.set(player_24_scores)
        total_score.set(total_point)


def on_click_score_two_point(player_num):
    global total_point
    if player_num == 13:
        global player_13_scores
        player_13_scores += 2
        total_point +=2
        s_player_13.set(player_13_scores)
        total_score.set(total_point)
       

    elif player_num == 14:
        global player_14_scores
        player_14_scores += 2
        total_point +=2
        s_player_14.set(player_14_scores)
        total_score.set(total_point)
        

    elif player_num == 15:
        global player_15_scores
        player_15_scores += 2
        total_point +=2
        s_player_15.set(player_15_scores)
        total_score.set(total_point)
        

    elif player_num == 16:
        global player_16_scores
        player_16_scores += 2
        total_point +=2
        s_player_16.set(player_16_scores)
        total_score.set(total_point)
       

    elif player_num == 17:
        global player_17_scores
        player_17_scores += 2
        total_point +=2
        s_player_17.set(player_17_scores)
        total_score.set(total_point)
       

    elif player_num == 18:
        global player_18_scores
        player_18_scores += 2
        total_point +=2
        s_player_18.set(player_18_scores)
        total_score.set(total_point)
        

    elif player_num == 19:
        global player_19_scores
        player_19_scores += 2
        total_point +=2
        s_player_19.set(player_19_scores)
        total_score.set(total_point)
       

    elif player_num == 20:
        global player_20_scores
        player_20_scores += 2
        total_point +=2
        s_player_20.set(player_20_scores)
        total_score.set(total_point)
        

    elif player_num == 21:
        global player_21_scores
        player_21_scores += 2
        total_point +=2
        s_player_21.set(player_21_scores)
        total_score.set(total_point)
        

    elif player_num == 22:
        global player_22_scores
        player_22_scores += 2
        total_point +=2
        s_player_22.set(player_22_scores)
        total_score.set(total_point)
        

    elif player_num == 23:
        global player_23_scores
        player_23_scores += 2
        total_point+=2
        s_player_23.set(player_23_scores)
        total_score.set(total_point)
        

    elif player_num == 24:
        global player_24_scores
        player_24_scores += 2
        total_point +=2
        s_player_24.set(player_24_scores)
        total_score.set(total_point)

def on_click_score_three_point(player_num):
    global total_point
    if player_num == 13:
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
entry_total.grid()

entry_player_13 = Entry(root, textvariable=b_player_13)
entry_player_13.grid()
entry_player_14 = Entry(root, textvariable=b_player_14)
entry_player_14.grid()
entry_player_15 = Entry(root, textvariable=b_player_15)
entry_player_15.grid()
entry_player_16 = Entry(root, textvariable=b_player_16)
entry_player_16.grid()
entry_player_17 = Entry(root, textvariable=b_player_17)
entry_player_17.grid()
entry_player_18 = Entry(root, textvariable=b_player_18)
entry_player_18.grid()
entry_player_19 = Entry(root, textvariable=b_player_19)
entry_player_19.grid()
entry_player_20 = Entry(root, textvariable=b_player_20)
entry_player_20.grid()
entry_player_21 = Entry(root, textvariable=b_player_21)
entry_player_21.grid()
entry_player_22 = Entry(root, textvariable=b_player_22)
entry_player_22.grid()
entry_player_23 = Entry(root, textvariable=b_player_23)
entry_player_23.grid()
entry_player_24 = Entry(root, textvariable=b_player_24)
entry_player_24.grid()

button_reset = Button(root,text="reset", command =reset_team_fouls)

button_player_13 = Button(root, text="foul", command=lambda: on_click_fouls_B(13))
button_player_14 = Button(root, text="foul", command=lambda: on_click_fouls_B(14))
button_player_15 = Button(root, text="foul", command=lambda: on_click_fouls_B(15))
button_player_16 = Button(root, text="foul", command=lambda: on_click_fouls_B(16))
button_player_17 = Button(root, text="foul", command=lambda: on_click_fouls_B(17))
button_player_18 = Button(root, text="foul", command=lambda: on_click_fouls_B(18))
button_player_19 = Button(root, text="foul", command=lambda: on_click_fouls_B(19))
button_player_20 = Button(root, text="foul", command=lambda: on_click_fouls_B(20))
button_player_21 = Button(root, text="foul", command=lambda: on_click_fouls_B(21))
button_player_22 = Button(root, text="foul", command=lambda: on_click_fouls_B(22))
button_player_23 = Button(root, text="foul", command=lambda: on_click_fouls_B(23))
button_player_24 = Button(root, text="foul", command=lambda: on_click_fouls_B(24))

button_player_13.grid()
button_player_14.grid()
button_player_15.grid()
button_player_16.grid()
button_player_17.grid()
button_player_18.grid()
button_player_19.grid()
button_player_20.grid()
button_player_21.grid()
button_player_22.grid()
button_player_23.grid()
button_player_24.grid()


button_player_13_scores = Button(root, text="1", command=lambda: on_click_score_one_point(13))
button_player_14_scores = Button(root, text="1", command=lambda: on_click_score_one_point(14))
button_player_15_scores = Button(root, text="1", command=lambda: on_click_score_one_point(15))
button_player_16_scores = Button(root, text="1", command=lambda: on_click_score_one_point(16))
button_player_17_scores = Button(root, text="1", command=lambda: on_click_score_one_point(17))
button_player_18_scores = Button(root, text="1", command=lambda: on_click_score_one_point(18))
button_player_19_scores = Button(root, text="1", command=lambda: on_click_score_one_point(19))
button_player_20_scores = Button(root, text="1", command=lambda: on_click_score_one_point(20))
button_player_21_scores = Button(root, text="1", command=lambda: on_click_score_one_point(21))
button_player_22_scores = Button(root, text="1", command=lambda: on_click_score_one_point(22))
button_player_23_scores = Button(root, text="1", command=lambda: on_click_score_one_point(23))
button_player_24_scores = Button(root, text="1", command=lambda: on_click_score_one_point(24))

button_player_13_scores.grid()
button_player_14_scores.grid()
button_player_15_scores.grid()
button_player_16_scores.grid()
button_player_17_scores.grid()
button_player_18_scores.grid()
button_player_19_scores.grid()
button_player_20_scores.grid()
button_player_21_scores.grid()
button_player_22_scores.grid()
button_player_23_scores.grid()
button_player_24_scores.grid()



button_player_13_scores_two = Button(root, text="2", command=lambda: on_click_score_two_point(13))
button_player_14_scores_two = Button(root, text="2", command=lambda: on_click_score_two_point(14))
button_player_15_scores_two = Button(root, text="2", command=lambda: on_click_score_two_point(15))
button_player_16_scores_two = Button(root, text="2", command=lambda: on_click_score_two_point(16))
button_player_17_scores_two = Button(root, text="2", command=lambda: on_click_score_two_point(17))
button_player_18_scores_two = Button(root, text="2", command=lambda: on_click_score_two_point(18))
button_player_19_scores_two = Button(root, text="2", command=lambda: on_click_score_two_point(19))
button_player_20_scores_two = Button(root, text="2", command=lambda: on_click_score_two_point(20))
button_player_21_scores_two = Button(root, text="2", command=lambda: on_click_score_two_point(21))
button_player_22_scores_two = Button(root, text="2", command=lambda: on_click_score_two_point(22))
button_player_23_scores_two = Button(root, text="2", command=lambda: on_click_score_two_point(23))
button_player_24_scores_two = Button(root, text="2", command=lambda: on_click_score_two_point(24))

button_player_13_scores_two.grid()
button_player_14_scores_two.grid()
button_player_15_scores_two.grid()
button_player_16_scores_two.grid()
button_player_17_scores_two.grid()
button_player_18_scores_two.grid()
button_player_19_scores_two.grid()
button_player_20_scores_two.grid()
button_player_21_scores_two.grid()
button_player_22_scores_two.grid()
button_player_23_scores_two.grid()
button_player_24_scores_two.grid()

button_player_13_scores_three = Button(root, text="3", command=lambda: on_click_score_three_point(13))
button_player_14_scores_three = Button(root, text="3", command=lambda: on_click_score_three_point(14))
button_player_15_scores_three = Button(root, text="3", command=lambda: on_click_score_three_point(15))
button_player_16_scores_three = Button(root, text="3", command=lambda: on_click_score_three_point(16))
button_player_17_scores_three = Button(root, text="3", command=lambda: on_click_score_three_point(17))
button_player_18_scores_three = Button(root, text="3", command=lambda: on_click_score_three_point(18))
button_player_19_scores_three = Button(root, text="3", command=lambda: on_click_score_three_point(19))
button_player_20_scores_three = Button(root, text="3", command=lambda: on_click_score_three_point(20))
button_player_21_scores_three = Button(root, text="3", command=lambda: on_click_score_three_point(21))
button_player_22_scores_three = Button(root, text="3", command=lambda: on_click_score_three_point(22))
button_player_23_scores_three = Button(root, text="3", command=lambda: on_click_score_three_point(23))
button_player_24_scores_three = Button(root, text="3", command=lambda: on_click_score_three_point(24))

button_player_13_scores_three.grid()
button_player_14_scores_three.grid()
button_player_15_scores_three.grid()
button_player_16_scores_three.grid()
button_player_17_scores_three.grid()
button_player_18_scores_three.grid()
button_player_19_scores_three.grid()
button_player_20_scores_three.grid()
button_player_21_scores_three.grid()
button_player_22_scores_three.grid()
button_player_23_scores_three.grid()
button_player_24_scores_three.grid()

entry_player_13_scores = Entry(root, textvariable=s_player_13,state='readonly')
entry_player_13_scores.grid()
entry_player_14_scores = Entry(root, textvariable=s_player_14,state='readonly')
entry_player_14_scores.grid()
entry_player_15_scores = Entry(root, textvariable=s_player_15,state='readonly')
entry_player_15_scores.grid()
entry_player_16_scores = Entry(root, textvariable=s_player_16,state='readonly')
entry_player_16_scores.grid()
entry_player_17_scores = Entry(root, textvariable=s_player_17,state='readonly')
entry_player_17_scores.grid()
entry_player_18_scores = Entry(root, textvariable=s_player_18,state='readonly')
entry_player_18_scores.grid()
entry_player_19_scores = Entry(root, textvariable=s_player_19,state='readonly')
entry_player_19_scores.grid()
entry_player_20_scores = Entry(root, textvariable=s_player_20,state='readonly')
entry_player_20_scores.grid()
entry_player_21_scores = Entry(root, textvariable=s_player_21,state='readonly')
entry_player_21_scores.grid()
entry_player_22_scores = Entry(root, textvariable=s_player_22,state='readonly')
entry_player_22_scores.grid()
entry_player_23_scores = Entry(root, textvariable=s_player_23,state='readonly')
entry_player_23_scores.grid()
entry_player_24_scores = Entry(root, textvariable=s_player_24,state='readonly')
entry_player_24_scores.grid()

root.mainloop()
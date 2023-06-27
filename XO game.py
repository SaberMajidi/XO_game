import tkinter as tk
from tkinter.messagebox import showinfo
from PIL import ImageTk, Image
from functools import partial

def game_page():
    window = tk.Tk()
    window.title('XO Game')

    global turn, results, player_points
    turn = "X"
    results = ['', '', '', '', '', '', '', '', '']
    player_points = [0, 0]

    def clicked(btn):
        global turn
        btn = int(btn)
        if results[btn] == "":
            if turn == "X":
                results[btn] = "X"
                buttons[btn]['bg'] = 'red'
                buttons[btn]["fg"] = 'white'
                buttons[btn]["text"] = "X"
                turn = "O"
            else:
                results[btn] = "O"
                buttons[btn]['bg'] = 'blue'
                buttons[btn]["fg"] = 'white'
                buttons[btn]["text"] = "O"
                turn = "X"
        #print(results)
        rule()
            

    def rule():
        if (results[0]==results[1]==results[2] and results[0]!=""):
            show_winner(results[0])
        elif(results[3]==results[4]==results[5] and results[3]!=""):
            show_winner(results[3])
        elif(results[6]==results[7]==results[8] and results[6]!=""):
            show_winner(results[6])
        elif(results[0]==results[3]==results[6] and results[0]!=""):
            show_winner(results[0])
        elif(results[1]==results[4]==results[7] and results[1]!=""):
            show_winner(results[1])
        elif(results[2]==results[5]==results[8] and results[2]!=""):
            show_winner(results[2])
        elif(results[0]==results[4]==results[8] and results[0]!=""):
            show_winner(results[0])
        elif(results[2]==results[4]==results[6] and results[2]!=""):
            show_winner(results[2])
        else:
            check_draw()

    def show_winner(winner):
        if winner == "X":
            player_points[0] += 1
            showinfo("The game is over", "Player #1 wins")
            reset()
        else:
            player_points[1] += 1
            showinfo("The game is over", "Player #2 wins")
            reset()
                
    def reset():
        global results, turn
        results = ["", "", "", "", "", "", "", "", ""]
        turn = "X"
        points()
        board()

    def check_draw():
        if "" not in results:
            showinfo("The game is over", "The game equalised")
            reset()

    def points():
        board_frame = tk.Frame(window)
        board_frame.grid(row=0)
        label_player_one = tk.Label(board_frame, text="Player 1", font=(16), padx=10)
        label_player_two = tk.Label(board_frame, text="Player 2", font=(16), padx=10)
        label_player_one.grid(row=0, column=0)
        label_player_two.grid(row=0, column=1)

        point_frame = tk.Frame(window)
        point_frame.grid(row=1)
        point_player_one = tk.Label(point_frame, text=player_points[0], padx=20, font=(18))
        point_player_two = tk.Label(point_frame, text=player_points[1], padx=20, font=(18))
        point_player_one.grid(row=0, column=0)
        point_player_two.grid(row=0, column=1)

    def board():
        global buttons
        buttons = []
        counter = 0
        board_frame = tk.Frame(window)
        board_frame.grid(row=2)
        for row in range(1, 4):
            for column in range(1, 4):
                index = counter
                buttons.append(index)
                buttons[index] = tk.Button(board_frame, command=lambda x=f"{index}":clicked(x))
                buttons[index].config(width=10, height=4, font=("N.one", 18, "bold"))
                buttons[index].grid(row=row, column=column)
                counter += 1


    points()
    board()

    window.mainloop()

def main_page():
    window_main = tk.Tk()
    window_main.title("XO GAME")
    window_main.geometry("400x400")
    
    bg = ImageTk.PhotoImage(Image.open("alpaca_2.jpg"))
    
    label1 = tk.Label( window_main, image = bg)
    label1.place(x = 0, y = 0)
    
    label2 = tk.Label( window_main, text = "Welcome")
    label2.pack(pady = 10)
    

    btn = tk.Button(window_main, text = 'Click to open the game!', command=game_page )
    btn.pack(pady = 170)
    btn.config(fg='red',bg='yellow')

    btn.pack(side = 'top')  

    window_main.mainloop()

def setup():
	menu = tk.Tk()
	menu.geometry("250x250")
	menu.title("setup")
	wpl = partial(game_page)

	head = tk.Button(menu, text="setup",
				activeforeground='red',
				activebackground="yellow", bg="red",
				fg="yellow", width=500, font='summer', bd=5)
    

	B2 = tk.Button(menu, text="Multi Player", command=wpl, activeforeground='red',
				activebackground="yellow", bg="red", fg="yellow",
				width=500, font='summer', bd=5)

	B3 = tk.Button(menu, text="Exit", command=menu.quit, activeforeground='red',
				activebackground="yellow", bg="red", fg="yellow",
				width=500, font='summer', bd=5)
	head.pack(side='top')
	B2.pack(side='top')
	B3.pack(side='top')
	menu.mainloop()
        

main_page()
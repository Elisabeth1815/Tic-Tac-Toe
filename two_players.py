from tkinter import *
import random

# Constants
FONT = "roboto"
BG_COLOR = "#FAF6F0"
BG_COL_BUTTON = "#F1EFEF"
INTRO_COLOR = "#2D9596"
WIN_COLOR = "#98D8AA"
TIE_COLOR = "#F4F27E"


def button_clicked(x, y, label):
	global player
	# global computer

	if board[x][y]["text"] == "" and win() is False:
		if player == characters[0]:

			board[x][y]["text"] = player

			if win() is False:
				player = characters[1]
				label.config(text=(characters[1] + "'s turn"))

			elif win() is True:
				label.grid_forget()

			elif win() == "Tie":
				label.grid_forget()

		else:

			board[x][y]["text"] = player

			if win() is False:
				player = characters[0]
				label.config(text=(characters[0] + "'s turn"))

			elif win() is True:
				label.grid_forget()

			elif win() == "Tie":
				label.grid_forget()


def win():
	for x in range(3):
		if board[x][0]["text"] == board[x][1]["text"] == board[x][2]["text"] != "":
			board[x][0].config(bg=WIN_COLOR)
			board[x][1].config(bg=WIN_COLOR)
			board[x][2].config(bg=WIN_COLOR)
			return True

	for y in range(3):
		if board[0][y]["text"] == board[1][y]["text"] == board[2][y]["text"] != "":
			board[0][y].config(bg=WIN_COLOR)
			board[1][y].config(bg=WIN_COLOR)
			board[2][y].config(bg=WIN_COLOR)
			return True

	if board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] != "":
		board[0][0].config(bg=WIN_COLOR)
		board[1][1].config(bg=WIN_COLOR)
		board[2][2].config(bg=WIN_COLOR)
		return True

	elif board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] != "":
		board[0][2].config(bg=WIN_COLOR)
		board[1][1].config(bg=WIN_COLOR)
		board[2][0].config(bg=WIN_COLOR)
		return True

	elif empty_buttons() is False:
		for x in range(3):
			for y in range(3):
				board[x][y].config(bg=TIE_COLOR)
		return "Tie"

	else:
		return False


def empty_buttons():
	full_spaces = 0
	for x in range(3):
		for y in range(3):
			if board[x][y]["text"] != "":
				full_spaces += 1

	if full_spaces == 9:
		return False
	else:
		return True


def game_human():
	for x in range(3):
		for y in range(3):
			board[x][y] = Button(game_board,
			                     text="",
			                     command=lambda row=x, column=y: button_clicked(row, column, label),
			                     height=4, width=8,
			                     font=FONT,
			                     highlightthickness=20,
			                     background=BG_COL_BUTTON)
			board[x][y].grid(row=x, column=y)

	label = Label(text=player + "'s turn", background=BG_COLOR, font=FONT)
	label.grid(column=1)


def game_intro():
	# Label
	label1 = Label(text="WELCOME TO TIC TAC TOE GAME!",
	               font=FONT,
	               fg=INTRO_COLOR,
	               bg=BG_COLOR, )
	label1.place(x=25, y=50)

	# Buttons
	choose_button1 = Button(text="Game",
	                        command=game_human,
	                        height=2,
	                        font=FONT, )
	choose_button1.place(x=160, y=140)

	mainloop()


game_board = Tk()
game_board.title("Tic Tac Toe")
game_board.config(width=400, height=400, bg=BG_COLOR)

board = [
	["", "", ""],
	["", "", ""],
	["", "", ""],
]

buttons = []

characters = ["X", "O"]
player = random.choice(characters)

menubar = Menu(game_board)
file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(label="Two Players", command=game_human)
file_menu.add_command(label="Exit", command=exit)

menubar.add_cascade(label="Game", menu=file_menu)

game_board.config(menu=menubar)

if __name__ == "__main__":
	game_intro()
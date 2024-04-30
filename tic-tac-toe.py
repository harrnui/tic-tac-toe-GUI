from tkinter import *


#need to fix the counter when a button is pressed twice 


def restart():

  global player
  global counter

  player = characters[0]

  #restarting the counter 
  counter = [1,2,3,4,5,6,7,8,9]

  label.config(text=player+ " 's turn")


  #updates button text to blank spaces

  grid()



def next_turn(row, column):

  global player 

  
  #trying to put the change of characters logic in 
  if counter[0]%2 != 0:

    player = characters[0] #the character X starts the game and every next odd number in the counter is this characters 
    del counter[0] #to delete the value of the counter 
    

    #checks if the button is empty and if the game hasn't finished
    if buttons[row][column]['text'] == "" and check_winner() is False:
      
      buttons[row][column]['text'] = player
    
    if check_winner() is True:

      label.config(text=player + " won")

  else:

    #O's turn
    player = characters[1]
    
    if buttons[row][column]['text'] == "" and check_winner() is False and counter[0]%2 == 0:
      
      del counter[0]
      
      buttons[row][column]['text'] = player
 
    if check_winner() is True:
      
      label.config(text=player + " won")

  if len(counter) == 0:

    label.config(text="Game is a Tie")
    


def check_winner():

    for row in range(3):

        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != '':

            return True

    for column in range(3):

    #if all the buttons in a row have matching text that is not equal to a blank space

        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != '':

            return True
    
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":

        return True

    if buttons[2][0]['text'] == buttons[1][1]['text'] == buttons[0][2]['text'] != "":

        return True

    #then we check for ties

    if empty_spaces() is False:

      return "Tie"

    else:

      return False
  


def empty_spaces():

  spaces = 9

  for row in range(3):

    for column in range(3):

      if buttons[row][column]['text']!='':

        spaces-=1

        if spaces == 0:

         return False

        else:

          return True

def grid(): #creates a 3x3 with Buttons

  for row in range(3):

    for column in range(3):

      buttons[row][column] = Button(frame, text ="",font=('consolas',40), width=5, height=2, command=lambda row=row, column=column:next_turn(row,column)  )

      buttons[row][column].grid(row=row,column=column)



board = Tk()

board.title("Tic-Tac-Toe")

characters = ["x","o"]

counter = [1,2,3,4,5,6,7,8,9]

player = "x"

buttons = [['','',''],
           ['','',''],
           ['','','']]

label = Label(text=player+ "'s turn", font=("futura",40))

label.pack(side="top")


new_game_button = Button(text="New Game", font=("futura",20), command=restart)

new_game_button.pack(side="top")


frame = Frame(board)

frame.pack()

grid()

board.mainloop()
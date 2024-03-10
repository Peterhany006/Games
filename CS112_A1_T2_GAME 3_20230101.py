# File: CS112_A1_T2_3_20230101.py
# Purpose: Subtract a square
# Author: Peter Hany Rufeat shaker
# ID: 20230101

def play (number_coins):
    move=1 
    list_move=[ x ** 2 for x in range (1,21)] # the list containing the square numbers from 1 to 400 
    while move !=0: # if move = 0 the game will end and the will be determind
      print('The number of coins ',number_coins)
      valid =False
      while valid ==False: # check the number entered by the player 1 is vaild according to the rules of the game 
        move=input('player 1 ,enter your move.\n')
        if move.isdigit():
         move=int(move)
        if type(move)==str:
          valid == False
          print('please, enter number not string ')
        elif move ==1 and number_coins==1: 
          break
        elif move in list_move and move < number_coins:
          valid==True
          break
        else :# if the number entered by the player 1 is invalid, he tries to enter it again  
          print('The number is not squared or not less than the number of coins')
          print('please, enter a valid number')
          valid == False   
      number_coins -= move 
      if number_coins==0:
        print('player 1 is winner.\n')
        break
      print('The number of coins ',number_coins)
      valid =False
      while valid ==False: # check the number entered by the player 2 is vaild according to the rules of the game 
        move=input('player 2 ,enter your move.\n')
        if move.isdigit():
         move=int(move)
        if type(move)==str:
          valid == False
          print('please, enter number not string ')
        elif move ==1 and number_coins==1: 
          break
        elif move in list_move and move < number_coins:
          break
        else : # if the number entered by the player 2 is invalid, he tries to enter it again 
          print('The number is not squared or not less than the number of coins')
          print('please, enter a valid number')
          valid == False   
      number_coins -= move
      if number_coins==0:
          print('player 2 is winner.\n')
          break    
# Explanation of the game       
print('The game is simple, two players take turns draws from a set of coins, and the player who draws the last coin wins.\n ')
print('Rules:')
print('  The number you draw from the coins must be a perfect square [1,4,9,16,......] and less than the remaining number of coins.')       
import random 
while True: # start the game 
  print('A) Start the game')
  print('B) Quit the game')
  choise = input().upper()
  if choise=='A':
    print('How to determine the number of coins ')
    print('A) Choose the number of coins ')
    print('B) play with a random number of coins ')
    choise_two = input().upper() 
    if choise_two=="A":
      check=True
      while check :
       number_coins = input("input number of coins ")
       if number_coins.isdigit():
        number_coins=int(number_coins)
        if number_coins <= 10000 and number_coins >= 50 :
          break
        else :
           check == True
           print("Sorry, minimum number of coins 50 and maximum number of coins 10000")
           print("please , input number of coins again")
       else: 
         check == True
         print('please, input number not string ')   
    elif choise_two =='B':
      number_coins = random.randrange(100,500)
    else :
      print('please selct a valid choise')    
      continue
    play(number_coins)
  elif choise=="B":
    print('good bye')
    break
  else :
    print('please selct a valid choise')    

     
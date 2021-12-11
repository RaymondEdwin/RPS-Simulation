import random
import json
import statistics
win_list_100_plays=[]
loss_list_100_plays=[]
def rps_Simulation():
  draw_count=0
  u1_win_count=0
  u2_win_count=0
  u1_loss_count=0
  u2_loss_count=0
  for i in range (100):
    game_play_1=""
    game_play_2=""
    list1=["r","p","s"]
    rand_ai_1=random.randint(0,2)
    user_1_choice=list1[rand_ai_1]
    rand_ai_2=random.randint(0,2)
    user_2_choice=list1[rand_ai_2]
    if user_1_choice==user_2_choice:
      #print("draw")
      draw_count=draw_count+1
    elif user_1_choice=="p" and user_2_choice=="s" or user_1_choice=="s" and user_2_choice=="r" or user_1_choice=="r" and user_2_choice=="p":
      u1_loss_count=u1_loss_count+1
      u2_win_count=u2_win_count+1
      #print("u2 wins")
    else:
      u1_win_count=u1_win_count+1
      u2_loss_count=u2_loss_count+1
  win_list_100_plays.append(u1_win_count)
  loss_list_100_plays.append(u1_loss_count)
    
  #print("u1 wins, ",u1_win_count )
  #print("u2 wins, ",u2_win_count )
  #print(draw_count)
def Repeat():
  for i in range (int(input("How many times to run simulation of 100 games of rps: "))):
    rps_Simulation()
  print("Win lists")
  print("\n")
  win_list_100_plays.sort()
  loss_list_100_plays.sort()
  with open('Wins.txt', 'a') as f:
    f.write(json.dumps(win_list_100_plays))
  with open("losses.txt","a") as f:
    f.write(json.dumps(loss_list_100_plays))
  
  mean_=statistics.mean(win_list_100_plays)
  sd=statistics.pstdev(win_list_100_plays)
  print("sd=",sd)
  print("mean=",mean_)
  print("Median=",statistics.median(win_list_100_plays))

Repeat()


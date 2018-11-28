my_num = 51

while True:
    
    ur_num_str = input("Guess my number (1-100): ")
    
    if not ur_num_str.isdigit():
        print("Hey, please choose a NUMBER !")
    else:
        
        ur_num = int(ur_num_str)
        
        if ur_num == my_num:
            print("Bingo!!")
            break
        elif (not ur_num >= 1 or not ur_num <= 100 or not ur_num_str.isdigit()):
            print("Hey, please choose a number from 1 to 100!")
        elif (ur_num < (my_num / 2)):
            print("Too small :(")
        elif (ur_num < my_num):
            print("A litte small !!")
        elif (ur_num > (my_num * 2)):
            print("Too large !!!")
        else:
            print("A little large!")

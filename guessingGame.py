import random

def getUserPick():
    while True:
        user1=int(input('User1, pick a number between 1 and 10:'))
        user2=int(input('User2, pick a number between 1 and 10:'))
        computer= random.randint(1,10)
        print(f"Actual number is {computer}")
    
        L=[user1,user2]
        
        diff=min(L,key=lambda x:abs(x-computer))
        if diff==user1:
                print("User 1 is closest!")
        else:
                print("User 2 is closest!")
        ask= input("Play again?(y/n)")
    
        if ask=='y':
        
          pass
        else:
            break 
    
    
getUserPick()
         
        
    
    
    
    
import random

print("Welcome to the game of 'stone','paper' and 'scissors'")
print("Here your opponent is computer which is operating according to the language instruction of python")
print(".....")
print("General rules are as follows\n 1. Stone and scissors, stone wins\n 2. Stone and paper, paper wins\n 3. Scissor and paper, scissor wins")
print("If you are ready to go, then type 'ENTER' in your keyboard and hit ENTER key in your keyboard")


n=input("")

if(n=="ENTER"):
    
    i=0
    for i in range(0,15):
        
            
        ps=["stone","paper","scissors"]
        p=random.choice(ps)
        s=input("Enter your choice (in small letters):")
        print(p)
        if(p=="stone"and s=="scissors"):
            print("Machine wins the game")
            
        if(p=="stone"and s=="paper"):
            print("Congratulations you are the winner") 
           
        if(p=="stone"and s=="stone"):
            print("Tie")

        if(p=="paper"and s=="scissors"):
            print("Congratulations you are the winner") 
            
        if(p=="paper"and s=="paper"):
            print("Tie")
           
        if(p=="paper"and s=="stone"):
            print("Machine wins the game")  

        if(p=="scissors"and s=="scissors"):
            print("Tie")
            
        if(p=="scissors"and s=="paper"):
            print("Machine wins the game")
           
        if(p=="scissors"and s=="stone"):
            print("Congratulations you are the winner")          

        if(s=="stone" and p=="scissor"):
            print("Congratulations you are the winner") 
          
        if(s=="stone"and p=="paper"):
            print("Machine wins the game")
           
        if(s=="stone"and p=="stone"):
            print("Tie")

        if(s=="paper" and p=="scissor"):
            print("Machine wins the game")
          
        if(s=="paper"and p=="paper"):
            print("Tie")
           
        if(s=="paper"and p=="stone"):
            print("Congratulations you are the winner") 

        if(s=="scissors" and p=="scissors"):
            print("Tie")
          
        if(s=="scissors"and p=="paper"):
            print("Congratulations you are the winner") 
            
           
        if(s=="scissors"and p=="stone"):
            print("Machine wins the game")
                
        i=i+1
def Draw():
    x = int(input("Please input a number to draw a diamond: "))
    z = 0
    for i in range(x):
        z = i + i
        print(" "*(x-i) + "*"*(z+1))
    for i in range(x,-1,-1):
        z = i + i
        print(" "*(x-i) + "*"*(z+1))
    
draw = 'yes' or 'y' or 'Yes'
Draw()
while draw == "Yes" or draw == "yes" or draw == "y":
    Draw()
    draw = input("Would you like to draw again? \nYes or No ")
    
        
    

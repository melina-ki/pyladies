from random import randint


def draw_map(list_of_coordinates, fruit_list=[],size=10):
    """Draws a grid for the snake to move. Adds fruits as "o" in the grid"""
    gameboard = []
    for x in range (size):
        gameboard.append(["."])
        for j in range(size):
            gameboard[x].append(".")
     
    if fruit_list != []:
        for i in fruit_list:
            x=i[0]
            y=i[1]
            gameboard[x][y] = "o"

    for i in list_of_coordinates:
        x=i[0]
        y=i[1]
        gameboard[x][y] = "x"
    for row in gameboard:
        print(row,end="\n")


def movement_grow(coordinates, direction):
    """The snake moves one position according to a specified direction and grows by one grid position"""
    direction_keys=["n","s","e","w"]
    while direction in direction_keys:
        if direction=="e":
            i=coordinates[-1]
            x=i[0]
            y=i[1]+1
        elif direction=="w":
            i=coordinates[-1]
            x=i[0]
            y=i[1]-1
        elif direction=="n":
            i=coordinates[-1]
            x=i[0]-1
            y=i[1]
        elif direction=="s":
            i=coordinates[-1]
            x=i[0]+1
            y=i[1]
        #check for hitting the borders:
        if 0<=x<gameboard_size and 0<=y<=gameboard_size:    
            coordinates.append((x,y))
            #print(coordinates)
            return coordinates
        else:
            direction=input("Change direction!")        
    

def movement(coordinates, direction):
    """The snake moves one position according to a specified direction """
    direction_keys=["n","s","e","w"]
    while isinstance(direction,str):
    #I'm sure this could be written better. I think I still haven't fully grasped how to write proper while loops.
        if direction=="e":
            i=coordinates[-1]
            x=i[0]
            y=i[1]+1
        elif direction=="w":
            i=coordinates[-1]
            x=i[0]
            y=i[1]-1
        elif direction=="n":
            i=coordinates[-1]
            x=i[0]-1
            y=i[1]
        elif direction=="s":
            i=coordinates[-1]
            x=i[0]+1
            y=i[1]
        #i'm not sure how to syntax this better..i want  this condition to be evaluated after the above.
        if 0<=x<gameboard_size and 0<=y<=gameboard_size: 
            coordinates.append((x,y))
            del coordinates[0]
            #print(coordinates)
            return(coordinates)
        else:
            direction=input("Change direction!")    


#The game starts here:
#Initial position of the snake:
starting_point=[(0,0),(0,1),(0,2)]
direction_keys=["n","s","e","w"]
print("Let's play snake!")
gameboard_size=int(input("How big should the grid be? choose an integer >= 10: "))
adding_fruits=str(input("would you like to add some fruits? y/n: "))
fruit_list=[]
if adding_fruits=='y':
    how_many=int(input("how many fruits? select from 1-5: "))
    for number in range(0,how_many):
        fruit_list.append((randint(0,gameboard_size-1), randint(0,gameboard_size-1)))
        #print(fruit_list)
#not all fruit lists work..with some I get an error that the list index is out of range, even though it is in range (i think..)
user_direction=input("Which direction do you want to send the snake? You can exit the game by typing 'end': ")
while user_direction!="end":
    if user_direction not in direction_keys:
        print("Please choose a valid direction!")
        user_direction=input("n, s, e or w?")
        continue
    moving_snake=movement(starting_point,user_direction)
    draw_map(moving_snake,fruit_list, gameboard_size)
    #finding fruits:
    for apple in fruit_list:
        if moving_snake[-1] in fruit_list: 
            apple=moving_snake[-1]
            growing_snake=movement_grow(moving_snake,user_direction)
            print("miam miam! an apple!")
            fruit_list.remove(apple)
            fruit_list.append((randint(0,gameboard_size-1), randint(0,gameboard_size-1)))
        break
    user_direction=input("Which direction do you want to send the snake? You can exit the game by typing 'end': ")
    #checking if the snake runs into itself:
    if moving_snake[-1] in moving_snake[:-2]:
        print("You lost!")
        break
    
    
# Algorithm:
# 1. Byrjum á að setja upp staðsetninguna á x og y og inputið þar sem þú setur inn áttina 
# 2. Setjum síðan upp fjögur föll sem taka inn inputin um áttina og bæta við eða draga frá 
# 3. Gerum föll sem segja hvar veggirnir eru og hvaða áttir eru mögulegar
def plus_direction(A):
    A += 1
    return A

def minus_direction(A):
    A -= 1
    return A

def check_direction(A):
    A = fixed_format(A)
    if A == possible_north:
        return 
    elif A == possible_south:
        return
    elif A == possible_east:
        return
    elif A == possible_west:
        return
    else:
        return False
    
def fixed_format(A):
    if A == "N" or A == "n":
        A = possible_north
    elif A == "S" or A == "s":
        A = possible_south
    elif A == "E" or A == "e":
        A = possible_east
    elif A == "W" or A == "w":
        A = possible_west
    else:
        return A
    return A

def possible_direction_x()

x = 1
y = 1

while x != 3 and y != 3:
    possible_north = possible_direction_y(y)
    possible_south = possible_direction_y(y)
    possible_east = possible_direction_x(x)
    possible_west = possible_direction_x(x)

    if possible_north == None:

        if possible_south == None:

            if possible_east == None:

                if possible_west == None:
                    print("Þú geriðir kraftaverk")
                
                else:
                    print("You can travel: {}.".format(possible_west))
            
            elif possible_west == None:
                print("You can travel: {}.".format(possible_east))
            
            else:
                print("You can travel: {} or {}.".format(possible_east,possible_west))

        elif possible_east == None:
            if possible_west == None:
                print("You can travel: {}.".format(possible_south))
            
            else:
                print("You can travel: {} or {}.".format(possible_south,possible_west))
        else:
            if possible_west == None:
                print("You can travel: {} or {}.".format(possible_east,possible_south))
            
            else:
                print("You can travel: {} or {} or {}.".format(possible_east,possible_south,possible_west))
    
    else: 
        if possible_south == None:

            if possible_east == None:

                if possible_west == None:
                    print("You can travel: {}.".format(possible_north))

                else:
                    print("You can travel: {} or {}.".format(possible_north,possible_west))

            elif possible_west == None:
                print("You can travel: {} or {}.".format(possible_north,possible_east))

            else: 
                print("You can travel: {} or {} or {}.".format(possible_north,possible_east,possible_west))

        elif possible_east == None:

            if possible_west == None:
                print("You can travel: {} or {}.".format(possible_north,possible_south))

            else:
                print("You can travel: {} or {} or {}.".format(possible_north,possible_south,possible_west))
        
        else:
            if possible_west == None:
                print("You can travel: {} or {} or {}.".format(possible_north,possible_east,possible_south))

            else:
                print("You can travel: {} or {} or {} or {}.".format(possible_north,possible_east,possible_south,possible_west))

    chosen_direction=input('Direction: ')
    is_it_possible = check_direction(chosen_direction)
    if is_it_possible == False:
        continue
    else:
        if chosen_direction == 'N' or chosen_direction == 'n':
            y=plus_direction(y)
        elif chosen_direction == 'E' or chosen_direction == 'e':
            x=plus_direction(x)
        elif  chosen_direction == 'S' or chosen_direction == 's':
            y=minus_direction(y)
        else:
            x=minus_direction(x)


        
        






    # How_many_are_available = check_none_nopes(possible_north,possible_east,possible_south,possible_west)

    # if How_many_are_available == 1:
    #     The_direction = Which_direction(possible_north,possible_east,possible_south,possible_west)

    #     print("You can travel: {}".format(The_direction))

    # elif How_many_are_available == 2:
    #     The_direction == Which_direction(possible_north,possible_east,possible_south,possible_west)

    #     second_direction == Which_direction()

    



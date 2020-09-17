# Algorithm:
# 1. Byrjum á að setja upp staðsetninguna á x og y 
# 2. Setjum síðan upp tvö föll sem taka inn input um áttina og bæta við eða draga frá 
# 3. Gerum föll sem segja hvar veggirnir eru og hvaða áttir eru mögulegar
# 4. Setjum upp while lykkju sem prentar út hvaða áttir er hægt að fara í og tekur inn hvaða átt maður vill

def plus_direction(A):
    A += 1
    return A

def minus_direction(A):
    A -= 1
    return A

def check_direction(A):
    A = fixed_format(A)
    if A == None:
        return False
    else:
        return A

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
        return None
    return A

def north(A):
    B = A + 1
    check = walls_y(x, A, B)
    if check == True:
        return ("(N)orth")

def south(A):
    B = A - 1
    check = walls_y(x, A, B)
    if check == True:
        return ("(S)outh")

def east(A):
    B = A + 1
    check = walls_x(A, y, B)
    if check == True:
        return ("(E)ast")

def west(A):
    B = A - 1
    check = walls_x(A, y, B)
    if check == True:
        return ("(W)est")

def walls_y(A, B, C):
    if C > 0 and C < 4:
        if A == 2 and (C == 3 or B == 3):
            return None
        else: 
            return True

def walls_x(A, B, C):
    if C > 0 and C < 4:
        if B != 1:
            if B == 2 and (C == 3 or A == 3):
                return None
            else: 
                return True


x = 1
y = 1

while x != 3 or y != 1:
    possible_north = north(y)
    possible_south = south(y)
    possible_east = east(x)
    possible_west = west(x)

    if possible_north == None:

        if possible_south == None:

            if possible_east == None:

                if possible_west == None:
                    print("Þú gerðir kraftaverk")
                
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
        print("Not a valid direction!")
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
else: 
    print("Victory!")
def pyramid(num1):                                          #create function
    i=int(num1)                                             #turn input into an integer
    j= 1                                                    #start a coutner
    while i != 0:                                           #while num1 isn't 0
        print(" " * i + "x"*j)                            #make as many white spaces as there are num1 and print as many x as there are 2j so it's an even pyramid
        i=i-1                                               #reduce i by 1
        j=j+2                                               #augment j by 2
pyramid(input("How many layers should your pyramid have?")) #call function and get input

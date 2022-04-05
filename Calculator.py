def calculation():  
    num1 = ""
    num2 = ""
    action = ""
    while num1 != "Q" or num2 != "Q" or action != "Q":                                                      #Creation of function
        num1 = input("What's the first number? Press Q at any point to quit.")
        if num1 == "Q":                         #if num1 is Q, break
            break
        else:   
            num2 = input("What's the second number?")    #if num 2 is Q, break
            if num2 == "Q":
                break
            else:
                action = input("What would you like to do with the numbers?")
                if action != "Q":                                               #if action is Q, break
                    num1 = int(num1)
                    num2 = int(num2)
                    answer = 0
                    if action == 'add' or action == '+':            #If the action requested is add
                        answer = num1 + num2 
                                                                 #Add num 1 and num 2
                    elif action == 'subtract' or action == '-':     #If it's subtract
                        answer =num1-num2
                                                                  #subtract them
                    elif action == 'multiply' or action == '*':     #if it's multiply   
                        answer = num1*num2
                                                                 #multiply them
                    elif action == 'divide' or action == '/':       #if it's divide
                        answer = num1/num2
                                                                     #divide them
                    else: 
                        answer = str(answer)                                  
                        answer == ("I didn't catch that, please try again.")        #if the action is incorrect, function displays a message
                    print(answer)        #print answer
                    calculation()          #function calls itself to start again


calculation()

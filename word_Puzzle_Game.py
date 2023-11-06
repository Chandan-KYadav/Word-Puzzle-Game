#WORD PUZZLE GAME
def lower_case(str) :
    str.lower()
    return str.lower()

def check(j , lst) :
    flag = 0
    correct_list = ['father' , 'break' , 'country' , 'green' , 'aeroplane']
   
    if(lst[j].strip()==correct_list[j]) :
        print("correct")
        flag = 1
        return flag
    else :
        print("wrong")
        return flag 

#-------------------Driven code---------------------#
display = ['RAEHTF' , 'KABRE' , 'CYROTNU' , 'RENEG' , 'OAERELANP']
user_list = [] #empty list 
str_list = [] #empty list for str
answer = 0
i = 0

while(i<len(display)) :
    print("Arrange the letters to form a valid word:")
    print(display[i])

    user_output = input() #output given by users
    user_output_new = lower_case(user_output)
    user_list.append(user_output_new)

    marks = check(i,user_list)

    if marks == 1 :
        answer+=1
    else :
        answer-=1

    i+=1

print("Net score is",answer)


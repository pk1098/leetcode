input_str = "aacabdkacaa"
length = len(input_str)

answer = 0
answer_length = 0
answer_i = 0
answer_j = 0



def longest_plaindrom(temp_str):
    global answer_length
    global answer_i
    global answer_j
    n = len(temp_str)
    # inner_list = [0 for i in range(n)]
    # x = [inner_list for i in range(n)]
    x = [[0 for i in range(n)] for j in range(n)]
    
        

    for i in range(1,n):
        for j in range(n):
            if((j+i)<n):
                if i== 1:
                    if(temp_str[j] == temp_str[j+i]):
                        print(temp_str[j])
                        print(temp_str[j+i])
                        print('----------------------------------------',i,j)
                        x[j+i][j] = 1
                        if((((j+i) - j)+1) > answer_length):
                            answer_length = (((j+i) - j)+1)
                            answer_i = j
                            answer_j = j+i
                else:
                    if(temp_str[j] == temp_str[j+i]):
                        if(x[(j+i)-1][j+1] == 1 or (   ((((j+i)-j)+1)==3)      and    temp_str[j+1] == temp_str[(j+i)-1])):
                            x[j+i][j] = 1
                            print(temp_str[j])
                            print(temp_str[j+i])
                            print('--------------------------other--------------',i,j,x[(j+i)-1][j+1],temp_str[(j+i)-1],temp_str[j+1])
                            if((((j+i) - j)+1) > answer_length):
                                answer_length = (((j+i) - j)+1)
                                answer_i = j
                                answer_j = j+i
            else:
                break
    return x


                


    

if __name__ == "__main__":
    x = longest_plaindrom(input_str)
    # inner_list = [0 for i in range(3)]
    # value = [inner_list for i in range(3)]
    answer = ""
    print(answer_length)
    print(answer_i)
    print(answer_j)
    print(x)
    if(answer_length == 0):
        print(input_str[0])
    else:
        for i in range(answer_length):
            answer = answer + input_str[i + answer_i]
    print(answer)
    # arr = [[0 for i in range(3)] for j in range(3)]
    # arr[0][2] = 9
    # print(arr)
    

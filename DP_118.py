def generate(n):
    final_answer = []
    temp_answer = list()
    for i in range(n):
        if i ==0:
            final_answer.append([1])
        elif i == 1:
            value = [1,1]
            temp_answer = [1,1]
            final_answer.append(value)
        else:
            length = len(temp_answer)
            j = 0
            value = list()
            value.append(1)
            while((j+1)<=(length-1)):
                value.append(temp_answer[j] + temp_answer[j+1])
                j = j + 1
                print(j)
            value.append(1)
            
            temp_answer = value
            final_answer.append(value)


    return final_answer

if __name__ == "__main__":
    value = generate(5)
    print(value)
#PYTHON HACKER RANK QUESTION 

def count_substring(string, sub_string):
    state=0
    count=0
    while state!=-1:
        state = string.find(sub_string,state)
        if state!=-1:
            count+=1
            state+=1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

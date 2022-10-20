#Python hacker rank question

if __name__ == '__main__':
    new_name=[]
    new_score=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        new_name.append(name)
        new_score.append(score)
  
  
    a=list(new_score)
    a.sort()
    b=list(set(a))
    b.sort()
    second_list=[]
    for index,value in enumerate(new_score):
        if value == b[1]:
            second_list.append(new_name[index])
        second_list.sort()
    for i in second_list:
        print(i)      

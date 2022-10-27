#HACKER RANK PYTHON QUESTION

if __name__ == '__main__':
    s = input()
    v1=False
    v2=False
    v3=False
    v4=False
    v5=False
    
    for i in s:
        if i.isalnum():
            v1=True
        if i.isalpha():
            v2=True
        if i.isdigit():
            v3=True
        if i.islower():
            v4=True
        if i.isupper():
            v5=True
    print(v1)
    print(v2)
    print(v3)
    print(v4)
    print(v5)
    
        

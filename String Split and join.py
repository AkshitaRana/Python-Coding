# PYTHON HACKER RANK QUESTION

def split_and_join(line):
    # write your code here
    splt=[]
    splt=line.split(" ")
    splt="-".join(splt)
    return splt
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

#Python Hacker rank question

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    average=0
    count=0
    total=0
    for name in student_marks:
        if name == query_name:
            for score in student_marks[name]:
                total+=score
                count+=1
            average=total/count
            print("{:.2f}".format(average))         

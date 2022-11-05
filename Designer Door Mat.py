# PYTHON HACKER RANK QUESTION

N = int((input().split(' '))[0])
M = 3*N
for i in range(1,N,2):
    print(('.|.'*i).center(M,'-'))
print('WELCOME'.center(M,'-'))
for i in range(1,N,2):
    print(('.|.'*(N-1-i)).center(M,'-'))

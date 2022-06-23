#3의 배수일때 :fizz(done)
#5의 배수일때 :buzz(done)
#15의 배수일때:fizzbuzz
#나머지는 숫자로 출력 (done)

for i in range(1,46):
    if i%15 == 0:
        print('fizzbuzz')
    elif i%3 == 0:
        print('fizz')
    elif i%5 == 0:
        print('buzz')
    else:
        print(i)


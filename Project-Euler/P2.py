# Fibonacci sequence → each new term is generated by adding the previous two terms
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...

fib_terms = []
index = 0
num1 = 1
num2 = 0
sum = 0
score = 0

# Consider all fib sequence numbers whose values do not exceed 4,000,000
# if 4,000,000 is the sum, it will still get logged in the list bc sum is read in and logged after the loop is run
while sum < 4000000:
    sum = num1 + num2
    fib_terms.append(sum)
    
    num1 = fib_terms[index-1]
    num2 = sum

    index += 1

for i in fib_terms:
    if i%2 == 0:
        score += i

print(score)
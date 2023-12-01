fibonacci = ((0 if i == 0 else 1 if i == 1 else fibonacci[i-1] + fibonacci[i-2]) for i in range(10))
print(list(fibonacci))

#Challenge 31
#Write a generator expression that generates the first 10 Fibonacci numbers.
# Idk I gave up on this one tbh. It breaks when it runs.
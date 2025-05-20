numbers = input("Type your numbers: ")

numbers = [int(num) for num in numbers.strip().split()]

if not numbers:
    print("Please, type at least one number.")
else:
    n = len(numbers)
    
    total = [1] * n

    for i in range(n):
        for j in range(n):
            if i != j:
                total[i] *= numbers[j]
    
    print(f"In: {numbers}\n")
    print(f"Out: {total}")
    
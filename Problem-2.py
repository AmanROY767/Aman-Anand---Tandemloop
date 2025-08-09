# Problem-2: Generate first a odd numbers

def generate_odd_series(a):
    result = []
    for i in range(a):
        result.append(2 * i + 1)
    return result



a = int(input("Enter a: "))
print("Output:", generate_odd_series(a))

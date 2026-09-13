print("Print current and previous number sum in a range(10)")

previous_num = 0

for i in range(10):
    sum = previous_num + i
    print(f"Current Number: {i} Previous Number: {previous_num} Sum: {sum}")
    previous_num = i
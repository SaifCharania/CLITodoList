tasks = []
tasks.append(input("What is your plan for today?\nEnter: "))
count = 0
while(input("Do you have any other plans?(y/n)") != 'n'):
    tasks.append(input("What is your plan?\nEnter: "))
    count = count + 1
print()
print("=" * 50)
for i in range(count + 1):
    print(tasks[i])
print("=" * 50)
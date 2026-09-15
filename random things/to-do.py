tasks = []
task1 = input('What do you have to do?')
tasks.append(task1)
while input('Anything else? (Y) = Yes (N) = No').lower() != 'n':
    task = input('Enter your task: ')
    tasks.append(task)

print('\nStuff To Do:\n')
for t in tasks:
    print('\n' + t + '\n')
file = open('scratch.txt', 'r')
todos = file.readlines()
file.close()

while True:
    userAction = input("\nType add, show, edit, complete or x: ")

    match userAction.lower().strip():
        case 'add':
            while True:

                todo = input('Enter a todo: ')
                if todo.lower() == 'x':
                    break
                elif todo+'\n' in todos:
                    continue
                else:
                    todos.append(todo + '\n')
                    file = open('scratch.txt', 'w')
                    file.writelines(todos)
                    file.close()

        case 'show':

            print('\ntodo list: \n---------')
            for x, i in enumerate(todos):
                print(f"{x}. {i.title()}")

        case 'edit':
            print('\ntodo list: \n---------')
            for x, i in enumerate(todos):
                print(f'{x}. {i.title()}')
            while True:
                number = int(input('\nnumber of the todo to edit: '))
                print('editing: ', todos[number],'\n')
                todos[number] = input('Edit or replace with: ')

                print('\ntodo list: \n---------')
                for x, i in enumerate(todos):
                    print(f'{x}. {i.title()}')

                doneEditing = input('\nAre you done editing? y/n: ')
                if doneEditing == 'y':
                    break

        case 'x':
            file.close()
            break

        case 'complete':
            while True:
                print(f'todos: ')
                for x, i in enumerate(todos):
                    print(f'{x}. {i.title()}')
                while True:
                    complete = input('\nEnter a todo to complete: ')
                    if complete.lower() in todos:
                        break
                    else:
                        complete = input('Invalid entry, Enter a todo to complete: ')
                todos.remove(complete.lower())
                print(f'todos: ')
                for x, i in enumerate(todos):
                    print(f'{x}. {i.title()}')
                break


        case invalid:
            print('invalid command')


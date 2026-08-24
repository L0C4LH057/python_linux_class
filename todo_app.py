tasks = [] # Empty backpack

while True:
    print("\n--- My To-Do List ---")
    print(f"Current tasks: {tasks}")
    action = input("Do you want to (add), (remove), or (quit)? ")
    
    if action == "add":
        new_task = input("What do you need to do? ")
        tasks.append(new_task) # Puts item in list
    elif action == "remove":
        done_task = input("Which task is finished? ")
        if done_task in tasks:
            tasks.remove(done_task)
        else:
            print("Task not found!")
    elif action == "quit":
        print("Goodbye!")
        break

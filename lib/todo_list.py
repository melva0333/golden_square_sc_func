def todo_list(task_list):
    #Parameters: list representing list of tasks
    #return : any task with #TODO in the string
    #sideffects:  none
    new_list = []
    for i in task_list:
        if "#TODO" in i:
            new_list.append(i)
    return new_list 

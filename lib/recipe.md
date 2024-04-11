# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So that I can keep track of my tasks
I want to check if a text includes the string `#TODO`.


## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE
def todo_list():
    #Parameters: list representing list of tasks
    #return : any task with #TODO in the string
    #sideffects:  none
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._
```python
# EXAMPLE
'''
Given an empty list
returns an empty list
'''
todo_list([])=> []

'''
Given a list without #TODO 
returns an empty list
'''
todo_list(["Shopping"])=> []

'''
Given a list with just one task with a #TODO
returns a list with that string 
'''
todo_list(["I need #TODO shopping" ])=> ["I need #TODO shopping" ]

'''
Given a list with multiple tasks
return a list with tasks that have #TODO
'''
todo_list("I need #TODO shopping" , "I need to do washing up")=> ["I need #TODO shopping"]

"""

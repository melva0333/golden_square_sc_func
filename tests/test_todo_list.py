from lib.todo_list import *

'''
Given an empty list
returns an empty list
'''
def test_empty_list_return_empty_list():
    result = todo_list([""])
    assert result == []

'''
Given a list without #TODO 
returns an empty list
'''
def test_list_without_todo_return_empty_list():
    result = todo_list(["Shopping"])
    assert result == []

'''
Given a list with just one task with a #TODO
returns a list with that string 
'''
def test_list_with_one_todo_return_list():
    result = todo_list(["I need #TODO shopping"])
    assert result == ["I need #TODO shopping"]

'''
Given a list with multiple tasks
return a list with tasks that have #TODO
'''
def test_list_with_multiple_todo_return_todo_list():
    result = todo_list(["I need #TODO shopping" , "I need to do washing up"])
    assert result == ["I need #TODO shopping"]

'''
Given a list with multiple tasks
return a list with tasks that have #TODO
'''
def test_list_2_with_multiple_todo_return_todo_list():
    result = todo_list(["I need #TODO shopping" , "I need #TODO washing up", "I need to get haircut"])
    assert result == ["I need #TODO shopping" , "I need #TODO washing up"]
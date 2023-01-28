from timeit import default_timer as timer

'''

QUESTION 1:

Alice has some cards with numbers written on them. She arranges the cards in decreasing order, and lays them
out face down in a sequence on a table. She challenges Bob to pick out the card containing a given number by
turning over as few cards as possible. Write a function to help Bob locate the card.

Input
cards: A list of numbers sorted in decreasing order. E.g. [13, 11, 10, 7, 4, 3, 1, 0]
query: A number, whose position in the array is to be determined. E.g. 7

Output
position: The position of query in the list cards. E.g. 3 in the above case (counting from 0)

'''

def linear_search(arr:list[int] , target:int) ->int:
    n = len(arr)

    for i in range(n):
        if arr[i] == target:
            return i
    return -1


def test_location(arr:list[int] , target: int , mid:int) -> str:
    result = arr[mid]
    
    if result == target:
        if mid - 1>= 0 and result == arr[mid-1]:
            return "left"
        else:
            return "found"
    
    elif result < target:
        return "left"
    
    else:
        return "right"
    
    
def binary_search(arr:list[int] , target:int) -> int:
    low , hi = 0 , len(arr) -1

    while low <= hi:
        mid = (low+hi)//2

        result = test_location(arr , target , mid)

        if result == "found":
            return mid
        elif result == "left":
            hi = mid-1
        else:
            low = mid+1
    return -1



if __name__ == "__main__":
# FOR QUESTION 1
    tests = [{
    'input': {
        'arr': [13, 11, 10, 7, 4, 3, 1, 0],
        'target': 1
    },
    'output': 6
},{
    'input': {
        'arr': [4, 2, 1, -1],
        'target': 4
    },
    'output': 0
},{
    'input': {
        'arr': [3, -1, -9, -127],
        'target': -127
    },
    'output': 3
},{
    'input': {
        'arr': [6],
        'target': 6
    },
    'output': 0 
},{
    'input': {
        'arr': [9, 7, 5, 2, -9],
        'target': 4
    },
    'output': -1
},{
    'input': {
        'arr': [],
        'target': 7
    },
    'output': -1
},{
    'input': {
        'arr': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'target': 3
    },
    'output': 7
},{
    'input': {
        'arr': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'target': 6
    },
    'output': 2
}]
    for test in tests:
        print(f"For Test {tests.index(test)}")
        start = timer()
        output = binary_search(**test['input'])
        end = timer()
        if output == test['output']:
            print(f"Test Case passed in time {end - start} \n")
        else:
            print(f"Test Case Failed \n , {output}")
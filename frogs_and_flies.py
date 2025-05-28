from typing import List

def frogs(X: List[int], S: List[int], Y: List[int]) -> List[int]:
    # Initialize a list to store the number of flies each frog can eat
    result = [1]

    # Recurse Y with X
    for index in range(len(X)):
        print(index)
        result.append(recursive_count(X[index], S[index], Y))

    return result

def recursive_count(x: int, s: int, Y: List[int]) -> int:
    # Base case: if Y is empty or x is less than or equal to 0, return 0
    if len(Y) <= 0 or x <= 0:
        return 0

    # Initialize a sum to count the number of flies
    sum = 0
    for y in Y:
        # Check if the absolute difference between x and y is less than or equal to s
        if abs(x - y) <= s:
            sum += 1

    return sum

# R E A D M E
# DO NOT CHANGE the code below, we use it to grade your submission. If changed your submission will be failed automatically.
if __name__ == '__main__':  
    line = input()
    x = [int(i) for i in line.strip().split()]
    line = input()
    s = [int(i) for i in line.strip().split()]
    line = input()
    y = [int(i) for i in line.strip().split()]
    output = frogs(x, s,y)
    if output == []:
        print('[]')
    else:
        print('[%s]' % ','.join(map(str, output)))
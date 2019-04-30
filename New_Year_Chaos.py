""" 
Function Description

Complete the function minimumBribes in the editor below. It must print an integer representing the minimum number of bribes necessary, or Too chaotic if the line configuration is not possible.

minimumBribes has the following parameter(s):

    q: an array of integers
"""

# Complete the minimumBribes function below.
def minimumBribes(q):
    TotalBribes = 0
    bribe = True
    people = len(q)

    # Traverse through all array elements
    for i in range(people):
 
        # Last i elements are already in place
        for j in range(0, people-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if q[j] > q[j+1] :
                q[j], q[j+1] = q[j+1], q[j]
                TotalBribes += 1
    print(q)
    print(TotalBribes)
        





q = [2,1,5,3,4]
minimumBribes(q)

""" 
Function Description

Complete the function minimumBribes in the editor below. It must print an integer representing the minimum number of bribes necessary, or Too chaotic if the line configuration is not possible.

minimumBribes has the following parameter(s):

    q: an array of integers
"""

# Complete the minimumBribes function below.
def minimumBribes(q):
    TotalBribes = 0
    #bribe = True
    people = n
    #chaos = True
    if 0 < q[0]-3:
        TotalBribes = "Too chaotic"

    # Traverse through all array elements
    for i in range(people):
        #print("Person", i, "is", q[i-1])
        if TotalBribes == "Too chaotic":
            break
 
        # Last i elements are already in place
        for j in range(0, people-i-1):
            if (i == 0 and j+1 < q[j+1]-3):
                TotalBribes = "Too chaotic"
                #print(q[j+1],"Too chaotic at position", j+1, 'j =', j)
                
                break

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if q[j] > q[j+1] :
                q[j], q[j+1] = q[j+1], q[j]
                TotalBribes += 1
    print(q)
    print(TotalBribes)
        




n = 5
q = [2,5,1,3,4]
minimumBribes(q)

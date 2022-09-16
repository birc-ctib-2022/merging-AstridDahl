"""Code for merging two sorted lists."""


def merge(x: list[int], y: list[int]) -> list[int]:
    """
    Merge two sorted lists.

    Returns a list that contains all the elements in x and y
    in sorted order.

    >>> merge([1, 2, 4, 6], [1, 3, 4, 5])
    [1, 1, 2, 3, 4, 4, 5, 6]
    """
    i, j = 0, 0
    z = []  # a new list to copy elements into
    # FIXME: fill out the loop so you merge the lists
    # until one of them is empty

    x_s=sorted(x)
    y_s=sorted(y)

    while i < len(x_s) and j < len(y_s):
        
        if x_s[i] < y_s[j]:
            z.append(x_s[i])
            i += 1
        else:
            z.append(y_s[j])
            j += 1
        
    #    break  # FIXME: you shouldn't just break here
    # At least one of the lists is empty now. Copy the
    # remainder of the other into z.

        # if i == len(x):
        #     for j in range(j, len(y)):
        #         z.append(y[j])

        # if j == len(y) and i != len(x):
        #     for i in range(i, len(x)):
        #         z.append(x[i])
        
        if i == len(x):
            z.extend(y[j:len(y)])

        if j == len(y) and i != len(x):
            z.extend(x[i:len(x)])
            # z.extend() adds the index content of one list to the list z, 
            # whereas z.append() adds a list to the list z, so it becomes nested z=[i,i,i[i,i]]

    return z

# Terminates because the while loop condition must become false as we increment i/j for each step.

x=[7,7,6,1,2,3]
y=[1,2,3,8]

merge_list=merge(x,y)

#print(x,y)
print(merge(x,y))
#print(f'The merged list: {merge_list}')

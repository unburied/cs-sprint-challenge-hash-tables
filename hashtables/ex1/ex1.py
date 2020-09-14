def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    pairwise sum all weights from first and second list
    add those sums and their index to a dict.
    if limit in dict, return index
    """
    # Your code here
    sums = {}
    i,j = 0, length-1

    while True:
        # check if the desired value is in dict
        if limit in sums:
            return sums[limit]

        # when last element of array is reached and limit not found, break
        # if lenght is 1 also break, no pair to return
        if i == length or length == 1:
            break

        # sum values, add to dict, and decrement j to itterate
        key = weights[i] + weights[j]
        sums[key] = (j,i)
        j -= 1

        # reset j and increment i when j is adjacent to i
        if j == (i+1):
            i += 1
            j = length - 1
        
        

    return None

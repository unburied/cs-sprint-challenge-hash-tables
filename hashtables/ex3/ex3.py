def intersection(arrays):
    """
    Given an array of arrays
    add elements to dict along with current array index
    and a false flag. if value is in next array, update with
    a true flag and current array index
    return keys of values == true
    """
    # Your code here
    nums = {}

    # traverse each array in arrays
    for i in range(len(arrays)):
        # check if item is already in nums from previous array, update dict if it isnt
        for j in arrays[i]:
            if j in nums:
                # use index i in a tuple to check which array updated value
                if nums[j][1] != i:
                    nums[j] = (True, i)
            else:
                nums[j] = (False, i)
    
    # break nums into its k,v and add key to list if the value is set to true
    result = [key for key,val in nums.items() if val[0]]

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))

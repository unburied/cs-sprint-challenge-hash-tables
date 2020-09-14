def has_negatives(a):
    """
    Add all elements to the a dict with a false flag
    itterate over the dict to check if each key made
    negative is in the dict, if so assign a true
    flag. Return all keys with val true
    """
    # Your code here

    nums = {num:False for num in a}

    for key in nums:
        make_neg = key * -1
        
        # check if the positive value has a neg in the dict
        if key > 0 and make_neg in nums:
            nums[key] = True

    # add all keys whose value is true to return list
    result = [k for k,v in nums.items() if v]
    
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

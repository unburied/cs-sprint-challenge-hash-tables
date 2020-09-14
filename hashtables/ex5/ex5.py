# Your code here



def finder(files, queries):
    """
    Use dict to allow for easy lookup of file path
    set up keys to be a last element of split file names
    with that value as the original
    THen use queries to check if any element of the 
    query is in the key
    """
    # Your code here
    paths = {}

    for f in files:
        # key is last element of file name
        key = f.split('/')[-1]

        # val is full file name, and there may be multpily paths with same name
        if key in paths:
            paths[key].append(f)
        else:
            paths[key] = [f]

    # adds file path to result if the query is in the dict
    result = []
    
    for q in queries:
        if q in paths:
            result.extend(paths[q])

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))

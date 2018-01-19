def isUnique(str):
    if len(str) > 128:
       return False
    
    char_set = [False for _ in range(128)]

    for c in string:
        val = ord(c)

        if char_set[val]:
            return False
        
        char_set[val] = True

    return True

#Runs in O(n) time, where n is len(str)
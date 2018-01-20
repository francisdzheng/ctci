def urlify(str, length):

    ind = len(str)

    for i in reversed(range(length)):
        if str[i] == ' ':
            str[ind - 3:ind] = '%20'
            ind -=3
        else:
            str[ind - 1] = str[i]
            ind -= 1

    return str

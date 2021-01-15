def MarginOfError(x,y):
    errorbar = []
    if type(x) is list:
        for i in range(len(x)):
            for j in range(len(y)):
                precent1 = x[i]/y[j]
                precent = precent1 * 100
                errorbar.append(precent)
    elif type(x) is int:
        precent1 = x/y
        precent = precent1 * 100
        return precent

    else:
        print('error')

    return errorbar
        

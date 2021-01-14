def extract_data(filename):
    infile = open(filename,'r')
    infile.readline() # Skip the first line
    numbers = []
    for line in infile:
        words = line.split()
        num = words[1]
        numbers.append(num)
    infile.close()
    return numbers

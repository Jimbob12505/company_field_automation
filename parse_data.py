
def parse_data(raw_data):
    
    data = []

    for lines in raw_data:

        if len(lines[10]) != 0:
            data.append(lines[10])
        else:
            data.append(lines[9])
    
    return data
#Adds members to an array if they are "Senior" or "Open"

def openOrSenior(data):
    # Hmmm.. Where to start?
    values = []
    for x in data[:]:
        if x[0] > 54:
            if x[1] > 7:
                values.append("Senior")
            else:
                values.append("Open")
        else:
            values.append("Open")
    return values
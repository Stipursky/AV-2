h = int

def AM(a): 
    global h
    if h == 24:
        h = h - 24
        return h
    if h < 12:
        return h
    if h == 12:
        h = h - 12
        return h

def PM(p):
    global h
    if h == 12:
        return h
    if h > 12:
        h = h - 12
        return h

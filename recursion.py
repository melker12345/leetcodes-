target  = 10

i = 0
def add(target, i):
    if i < target:
        print("i < target")
        add(target, i + 1)

    else:
        print("i == target")
    i += 1
    
    
add(target, i)
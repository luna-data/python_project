count = 0

def increment_global():
    global count
    count += 1

def print_count():
    print("현재 count 값 : ", count)

increment_global()
increment_global()
print_count()
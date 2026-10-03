def count_up(num):
    if(num == 0):
        return
    count_up(num-1)
    print(num)


count_up(5)
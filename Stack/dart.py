def dart(expression):
    num_li = [None] * len(expression)
    dim = 0
    num_flag = 0
    for ch in expression:  # make num list
        if ch == "0":
            if dim == 0:
                num_li[dim] = "0"
                dim += 1
            elif dim > 0 and num_li[dim-1] and num_flag == 0:
                num_li[dim-1] += "0"
            else:
                num_li[dim] = "0"
                dim += 1
            num_flag = 0
        elif ch.isdigit():
            num_flag = 0
            num_li[dim] = ch
            dim += 1
        else:
            num_flag = 1
    dim = 0
    while num_li[-1] is None:
        num_li.pop()
    num_li = list(map(int, num_li))
    print("num_li:", num_li)

    for ch in expression:
        if ch == "S":
            print("ch: S, dim:", dim)
            dim += 1
        elif ch == "D":
            print("ch: D, dim:", dim)
            num_li[dim] = num_li[dim] * num_li[dim]
            dim += 1
        elif ch == "T":
            print("ch: T, dim:", dim)
            num_li[dim] = num_li[dim] * num_li[dim] * num_li[dim]
            dim += 1
        elif ch == "*":
            print("ch: *, dim:", dim)
            if dim - 2 >= 0:
                num_li[dim-1] = num_li[dim-1] * 2
                num_li[dim-2] = num_li[dim-2] * 2
            else:
                num_li[dim-1] = num_li[dim-1] * 2
        elif ch == "#":
                print("ch: #, dim:", dim)
                num_li[dim-1] = num_li[dim-1] * -1
        else:
            continue

        print(num_li)
    return sum(num_li)
    


print(dart("1S*2T*3S"))

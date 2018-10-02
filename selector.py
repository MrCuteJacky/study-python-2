def select(items):

    for x in range(len(items)):
        print("\033[32m" + str(x) + ")\033[0m " + items[x] + "")

    selected = -1

    while selected < 0 or selected >= len(items):

        selected = input("\033[32m請選擇：\033[0m")

        if selected.isnumeric():
            selected = int(selected)
        else:
            selected = -1

        if selected < 0 or selected >= len(items):
            print("\033[31m超出範圍了哦！只允許輸入0~" + str(len(items) - 1) + "，請重新輸入！\033[0m")

    return selected
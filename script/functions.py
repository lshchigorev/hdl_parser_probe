def InOutRegWireCnt(file_name, target):
    file = open(file_name)

    one_str_comment = 0
    mult_str_comment = 0
    cnt = 0

    for row in file:
        if mult_str_comment:
            if '*/' in row:
                mult_str_comment = 0
                continue
        elif '/*' in row:
            mult_str_comment = 1
            continue

        elif target in row:
            cnt += 1
            print(row)

    file.close()
    return cnt

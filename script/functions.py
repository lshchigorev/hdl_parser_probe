import re
def PortCnt(file_name, target, debug):
    file = open(file_name)

    one_str_comment = 0
    mult_str_comment = 0
    cnt = 0

    print(target)
    for row in file:
        #reg_exp_match = '(^\s*){}(\s+)(?P<type>wire|reg)?(\s*)(?P<width>\[\w*[:]\w*)?(\s*)(?P<few_names>\w+[,])?(?P<last_name>\w+)(;)'.format(target)
        #reg_exp_match = '(^\s*){}(\s+)(?P<type>wire|reg)?(\s*)(?P<width>\[\w*[:]\w*\])?(\s*)(?P<few_names>\w+(\s*)[,])?(\s*)(?P<last_name>\w+(\s*)[;])'.format(target)
        #reg_exp_match = '(^\s*){}(\s+)(?P<type>wire|reg)?(\s*)(?P<width>\[\w*[:]\w*\](\s*))?((?P<few_names>\w+(\s*)[,](\s*))*)(\s*)(?P<last_name>\w+(\s*))([;])'.format(target)
        
        reg_exp_match = '(^\s*){}(\s+)(?P<type>wire|reg)?(\s*)(?P<width>\[\w*[:]\w*\](\s*))?(\s*)((?P<few_names>\w+(\s*)[,](\s*))*)(?P<last_name>\w+(\s*))([;])'.format(target)
        match = re.search(reg_exp_match, row)
        #match = re.findall(reg_exp_match, row)
        reg_exp_one_str_comment = '(^\s*)(//)(.*)'
        one_str_comment = re.search(reg_exp_one_str_comment, row)
        
        if mult_str_comment:
            if '*/' in row:
                mult_str_comment = 0
                continue
        elif '/*' in row:
            mult_str_comment = 1
            continue
        elif one_str_comment:
            continue

        elif match:
            cnt += 1
            if debug:
                print(match)
                print('type group is ', match.group('type'))
                print('width group is ', match.group('width'))
                #print(match.group('few_names'))
                print('last_name group is ', match.group('last_name'))


    file.close()
    return cnt

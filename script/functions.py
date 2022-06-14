import re
def PortCnt(file_name, target, debug):
    file = open(file_name)

    one_str_comment = 0
    mult_str_comment = 0
    cnt = 0

    if debug: print("\nTarget is",target)
    for row in file:
        #reg_exp_match = '(^\s*){}(\s+)(?P<type>wire|reg)?(\s*)(?P<width>\[\w*[:]\w*)?(\s*)(?P<few_names>\w+[,])?(?P<last_name>\w+)(;)'.format(target)
        #reg_exp_match = '(^\s*){}(\s+)(?P<type>wire|reg)?(\s*)(?P<width>\[\w*[:]\w*\])?(\s*)(?P<few_names>\w+(\s*)[,])?(\s*)(?P<last_name>\w+(\s*)[;])'.format(target)
        #reg_exp_match = '(^\s*){}(\s+)(?P<type>wire|reg)?(\s*)(?P<width>\[\w*[:]\w*\](\s*))?((?P<few_names>\w+(\s*)[,](\s*))*)(\s*)(?P<last_name>\w+(\s*))([;])'.format(target)
        
        #width group doesn't sensitiive to param
        #reg_exp_match = '(^\s*){}(\s+)(?P<type>wire|reg)?(\s*)(?P<width>\[\w*[+|-|*|/]?\w*[:]\w*\](\s*))?(\s*)((?P<few_names>\w+(\s*)[,](\s*))*)(?P<last_name>\w+(\s*))([;])'.format(target)
        reg_exp_match = '(^\s*){}(\s+)(?P<type>wire|reg)?(\s*)(?P<width>(\[\s*\w*\s*[\+|\-|\*|\/]?\s*\w*\s*?[:]\s*\w*\s*[\+|\-|\*|\/]?\s*\w*\s*?\]))?(\s*)(?P<last_name>\w+(\s*))([;|,])'.format(target)
        reg_exp_param = '(^\s*){}(\s+)(?P<param_name>\w*)(\s*)[=](\s*)(\w+)(\s*)[;]'.format(target)
        reg_exp_alw = '(^\s*){}(\s*)[@]'.format(target)
        reg_exp_assign = '(^\s*){}(\s+)(?P<assign_name>\w*)(\s*)[=]'.format(target)
        
        match = re.search(reg_exp_match, row)
        match_param = re.search(reg_exp_param, row)
        match_assign = re.search(reg_exp_assign, row)
        match_alw = re.search(reg_exp_alw, row)
        
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

        elif match_assign:
            cnt +=1
            if debug:
                print(match_assign)
                print('assign name is:', match_assign.group('assign_name'))

        elif match_alw:
            cnt += 1

        elif match_param:
            cnt += 1
            if debug:
                print(match_param)
                print('parameter name is:', match_param.group('param_name'))
        
        elif match:
            cnt += 1
            if debug:
                print(match)
                print('type group is (for in/out only):', match.group('type'))
                print('width group is:', match.group('width'))
                #print(match.group('few_names'))
                print('last_name group is:', match.group('last_name'))


    file.close()
    return cnt

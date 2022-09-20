def build_truth_table_exec(args, bool_equation):
    locals_dict = {'out': {arg: [] for arg in args}}
    locals_dict['out']['result'] = []
    to_exec = ''
    indent_count = 0
    for arg in args:
        to_exec += ' ' * indent_count + f'for {arg} in range(2):\n'
        indent_count += 1
    for arg in args:
        to_exec += ' ' * indent_count + f'out["{arg}"].append({arg})\n'
    to_exec += ' ' * indent_count + 'out["result"].append(bool(' + bool_equation + '))'
    exec(to_exec, {}, locals_dict)
    return locals_dict['out']


def pythonize_bool_equation(bool_equation):
    out = ''
    for i in range(len(bool_equation)):
        c = bool_equation[i]
        if c == '→':
            raise ValueError("ptythonizing -> is tedious, please reduce \
            'a -> b' to 'not a or b' yourself")
        elif c == '≠':
            out += '!='
        elif c == '≡':
            out += '=='
        elif c == '∨':
            out += ' or '
        elif c == '∧':
            out += ' and '
        elif c == '¬':
            out += ' not '
        else:
            out += c
    return out


def count_paths_to_num(visit_list, add_list, mult_list, exclude_list):
    def _count_paths_to_num_internal(_start, _finish):
        if _start > _finish:
            return 0
        for el in exclude_list:
            if _finish == el:
                return 0
        if _start == _finish:
            return 1
        _out = 0
        for el in mult_list:
            if _finish % el == 0:
                _out += _count_paths_to_num_internal(_start, _finish / el)
        for el in add_list:
            _out += _count_paths_to_num_internal(_start, _finish - el)
        return _out

    out = 1
    visit_list.sort()
    for i in range(len(visit_list) - 1):
        out *= _count_paths_to_num_internal(visit_list[i], visit_list[i + 1])
    return out


if __name__ == '__main__':
    print(count_paths_to_num([1, 18, 9], [1, 5], [2], [11]))

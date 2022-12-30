priorities = {'L': 3, 'M': 2, 'S': 1}


def check_t_shirts(a, b):
    last_size_a = a[-1]
    a_priority = priorities[a[-1]]
    last_size_b = b[-1]
    b_priority = priorities[b[-1]]
    if a_priority > b_priority:
        return '>'
    elif a_priority < b_priority:
        return '<'
    else:
        if last_size_a == 'L' and len(a) > len(b):
            return '>'
        elif last_size_a == 'L' and len(a) < len(b):
            return '<'
        elif last_size_a == 'S' and len(a) > len(b):
            return '<'
        elif last_size_a == 'S' and len(a) < len(b):
            return '>'
        else:
            return '='


test_cases = int(input())

for i in range(test_cases):
    t_shirt_size_a, t_shirt_size_b = input().split()
    print(check_t_shirts(t_shirt_size_a, t_shirt_size_b))

from typing import Tuple, Literal, List

class Flames:
    F: str = 'Friends'
    L: str = 'Lovers'
    A: str = 'Affectionate'
    M: str = 'Marriage'
    E: str = 'Enemies'
    S: str = 'Siblings'

def remove_common_chars(str1: str, str2: str) -> Tuple[str, str]:
    op_str1: str = ''
    op_str2: str = ''

    for lett in str1:
        for i in range(len(str2)):
            if lett == str2[i]: # letter found
                str2 = str2[:i] + str2[i+1:]
                break
        else:
            op_str1 += lett
    
    op_str2 = str2
    
    return op_str1, op_str2

def calculate_flames_code(str1: str, str2: str) -> Literal['F', 'L', 'A', 'M', 'E', 'S']:
    flames: List = list('FLAMES')

    maxx = len(str1) + len(str2)
    i = 0
    while len(flames) > 1:
        i = (i + maxx - 1) % len(flames)
        flames.pop(i)
    
    return flames[0]


if __name__ == '__main__':
    name1: str = 'AJAY'
    name2: str = 'PRIYA'

    # remove common characters
    uni_name1, uni_name2 = remove_common_chars(name1, name2)

    flames = Flames()
    print(getattr(flames, calculate_flames_code(uni_name1, uni_name2)))
from typing import Tuple, Literal

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

if __name__ == '__main__':
    name1: str = 'AJAY'
    name2: str = 'PRIYA'

    print(remove_common_chars(name1, name2))
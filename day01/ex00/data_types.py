
def data_types():
    varss = (
        1,
        'text',
        4.2,
        False,
        [1, 2, 3, 'pom'],
        {'one': 1, 'ttt': 2},
        (1, 'str', True),
        {1, 2, 3, 4}
    )

    output = '['
    for i in varss:
        output += type(i).__name__ + ', '
    output = output[:-2] + ']'

    print(output)

if __name__ == '__main__':
    data_types()
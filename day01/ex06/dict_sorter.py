def dict_sorter():
    list_of_tuples = [
        ('Russia', '25'),
        ('France', '132'),
        ('Germany', '132'),
        ('Spain', '178'),
        ('Italy', '162'),
        ('Portugal', '17'),
        ('Finland', '3'),
        ('Hungary', '2'),
        ('The Netherlands', '28'),
        ('The USA', '610'),
        ('The United Kingdom', '95'),
        ('China', '83'),
        ('Iran', '76'),
        ('Turkey', '65'),
        ('Belgium', '34'),
        ('Canada', '28'),
        ('Switzerland', '26'),
        ('Brazil', '25'),
        ('Austria', '14'),
        ('Israel', '12')
    ]
    my_dict = dict((x, y) for x, y in list_of_tuples)
    print(my_dict, '\n')
    sort_list = sorted(my_dict.items(), key=lambda item : item[0])
    print(sort_list, '\n')
    sort_dict = {k: v for k, v in sort_list}
    print(sort_dict, '\n')
    sort_list = sorted(my_dict.items(), key=lambda item: (-int(item[1]), item[0]))
    print(sort_list, '\n')
    sort_dict = {k: v for k, v in sort_list}
    print(sort_dict, '\n')

    for i in sort_dict:
        print('%s' % i)

if  __name__ == '__main__':
    dict_sorter()

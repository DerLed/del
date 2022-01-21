class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def find(arr, value):
    for i in arr:
        if i == value:
            return True
    return False


def find_index(arr, value):
    result = []
    index = 0
    for i in arr:
        if i == value:
            result.append(index)
        index += 1
    return result


def find_weight(arr, value):
    total = 0
    for i in arr:
        if i == value:
            print('find!!', i)
            print('next', arr.index(i))
            total = 1 + find_weight(arr, arr.index(i))
    return total


def bar(arr):
    root = arr.index(-1)
    maxim = 0
    idx = 0
    l = find_index(arr, root)
    if l:
        print('pusto')


def foo(arr, value):
    print('пришло:')
    if find(arr, value):
        return foo(arr, arr.index(value))
    else:
        return value





def too(conect):
    bbb = {x: y for x, y in enumerate(conect)}
    print(bbb)

    for t in bbb:
        if bbb[t] == -1:
            key = t
            break

    # print(comand(bbb, key))
    # flag = True
    # for t in bbb:
    #     if bbb[t] == key:
    #         flag = False
    #         print("тут надо уходить в рекурсию")
    # if flag:
    #     print('ничего не нашлось')

# ---------почти то что нужно-------------
# def get_result(connections):
#     a = connections.index(-1)
#     return foo(connections, a)
# def command_f(massiv, value):
#     list_index = find_index(massiv, value)
#     print('получили такой масиив индексов:', list_index)
#     if not list_index:  # если ничего не найдено возвращаем пустоту
#         print('и он оказался пустым')
#         return list_index
#     else:
#         print('он оказался не пустым')
#         if len(list_index) == 1:
#             print('его длина 1, value=', value)
#             return [value, command_f(massiv, list_index[0]), []]
#         elif len(list_index) == 2:
#             print('его длина 2, value=', value)
#             return [value, command_f(massiv, list_index[0]), command_f(massiv, list_index[0])]
# ----------------------------------------------------------------------------


def command_f(massiv, value):
    list_index = find_index(massiv, value)
    print('получили такой масиив индексов:', list_index)
    if not list_index:  # если ничего не найдено возвращаем пустоту
        print('и он оказался пустым')
        return [value,[],[]]
    else:
        print('он оказался не пустым')
        if len(list_index) == 1:
            yyy = [value, command_f(massiv, list_index[0]), []]
            print('его длина 1, value=', yyy)
            return yyy
        elif len(list_index) == 2:
            xxx = [value, command_f(massiv, list_index[0]), command_f(massiv, list_index[1])]
            print('его длина 2, value=', xxx)
            return xxx


if __name__ == '__main__':
    connections = [2, 2, 1, 5, 3, -1, 4, 5, 2, 3]
    # connections2 = [1, 2, -1]
    # connections3 = [3, 2, 1, -1]
    # connections4 = [3, 4, 1, -1, 3]
    # connections5 = [3, 4, 1, -1, 3]
    # # # print('tttttt', get_result(connections5))
    # # # print(find_index(connections5, 3))
    # # tt = find_index(connections5, 3)
    # # for i in tt:
    # #     print(foo(connections5, i))
    # # bar(connections5)
    # too(connections5)

    # myTree = ['a',   #root
    #       ['b', ['d' [], []], ['e' [], []] ], ['c',  #right subtree
    #        ['f'[ [], []],
    #        [] ]
    #      ]

    mt = [5,
          [7, [], []],
          [3,
                [4,
                    [6, [], []],
                 []],

                [9, [], []]
        ]
          ]
    # print(mt[0])  # root
    # print(mt[1])  # left
    # print(mt[2])  # left
    # print(mt[2][1][1][2])  # left
    # a = [[], []]
    # if a:
        # print(a)


    def pre_order(node, mmm=[]):
        if node:
            mmm.append(node[0])
            print('>', node[0])
            pre_order(node[1], mmm)
            pre_order(node[2], mmm)
        return mmm


    pre_order(mt)

    print(find_index(connections, 0))
    a = [1, 2]
    c = [3, 4]
    a + c
    print(a + c)

    b1 = command_f(connections, 5)
    print(b1)
    print(mt)

    print(pre_order(b1))

def find(arr, value):
    for i in arr:
        if i == value:
            return True
    return False


# def cu(arr, index):
#     it = 0
#     for i in arr:
#         if i == index:
#             print('нашли', i, 'его индекс', arr.index(i))
#             it = arr.index(i)
#             cu(arr, arr.index(i))
#     print('it=', it)
#     return index

def find1(arr, value):
    total = 0
    for i in arr:
        if i == value:
            total = 1 + find1(arr, arr.index(i))
    return total


def fff(arr, value):
    if find(arr, value):
        return fff(arr, arr.index(value))
    else:
        return value


def get_result(connections):
    a = connections.index(-1)
    return find1(connections, a)


if __name__ == '__main__':
    connections = [2, 2, 1, 5, 3, -1, 4, 5, 2, 3]
    connections2 = [1, 2, -1]
    connections3 = [3, 2, 1, -1]
    connections4 = [3, 4, 1, -1, 3]
    print('tttttt', get_result(connections))
    # print("Сумма элементов равна:", sum1([[1, 2], [3, 4]]))

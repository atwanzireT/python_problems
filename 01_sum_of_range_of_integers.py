import builtins

lst = [0, 1, 2, 3, 4, 5]

sum = 0
for i in lst:  # Looping through the list
    sum += i
    i += 1
print(sum)


# 2nd Case
def sum_it_up(n):
    sum = 0
    for i in range(n + 1):
        sum += i
        i += 1
    return sum


print(sum_it_up(5))


# Better Soln
# print([i for i in range(5 + 1)])

def even_better(n):
    """
    @func even_better
    :param n: 
    :return: the sum of 0 to n
    """
    try:
        result = builtins.sum(range(n + 1))
    except TypeError:
        return 0

    return result

print(even_better(5))
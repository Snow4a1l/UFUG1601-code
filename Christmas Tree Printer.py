def print_tree(rows):
    for i in range(1,rows+1):
        print(' ' * (rows - i) + '*' * (2 * i - 1))

rows=int(input())
if rows>0:
    print_tree(rows)
    print(' ' * (rows - 1) + '|')
    print(' ' * (rows - 1) + '|')
elif rows==0:
    print("Error. Row shall not be 0.")

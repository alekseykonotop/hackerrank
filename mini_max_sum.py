def miniMaxSum(arr):
    new_arr = sorted(arr)
    if len(new_arr) == 5:
        print('{0} {1}'.format(sum(new_arr[:-1]), sum(new_arr[1:])))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    print('arr', arr)
    miniMaxSum(arr)
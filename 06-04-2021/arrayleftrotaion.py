arr = [1, 2, 3, 6, 4, 5, 7]
shift = 2
for i in range(0, shift):
    temp = arr[0]

    for j in range(0, len(arr) - 1):
        arr[j] = arr[j + 1]
    arr[len(arr)-1] = temp
for i in range(0, len(arr)):
    print(arr[i])

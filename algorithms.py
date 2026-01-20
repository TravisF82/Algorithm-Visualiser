def BubbleSort(data: list[int]):
    swaps = 1
    while swaps > 0:
        swaps = 0
        for i in range(len(data) - 1):
            if data[i] > data[i + 1]:
                temp = data[i]
                data[i] = data[i + 1]
                data[i + 1] = temp
                swaps += 1
def SelectionSort(data: list[int]):
    n = len(data)
    for i in range(n):
        current = data[i]
        smallest = current
        smallestIndex = i
        for j in range(i, n):
            if data[j] < data[smallestIndex]:
                smallest = data[j]
                smallestIndex = j
            frames += 1

        data[i] = smallest
        data[smallestIndex] = current
        
def InsertionSort(data: list[int]) -> list[int]:
    n = len(data)
    for i in range(n):
        ...
                
InsertionSort([1, 8, 9, 3, 7, 2, 4, 3, 9, 10, 14, 13, 11])

def QuickSort(data: list[int]) -> list[int]:
    ...


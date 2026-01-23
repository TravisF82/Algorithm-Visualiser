from bar import Bar

def BubbleSort():
    swaps = 1
    while swaps > 0:
        swaps = 0
        for i in range(len(Bar.bars) - 1):
            yield i
            if Bar.bars[i].val > Bar.bars[i + 1].val:
                temp = Bar.bars[i]
                Bar.bars[i] = Bar.bars[i + 1]
                Bar.bars[i + 1] = temp
                swaps += 1

"""
Time Complexity: O(n^2)
"""
def SelectionSort():
    n = len(Bar.bars)
    for i in range(n):
        current = Bar.bars[i]
        smallest = current
        smallestIndex = i
        for j in range(i, n):
            yield j
            if Bar.bars[j].val < Bar.bars[smallestIndex].val:
                smallest = Bar.bars[j]
                smallestIndex = j

        Bar.bars[i] = smallest
        Bar.bars[smallestIndex] = current
        
def InsertionSort(data: list[int]) -> list[int]:
    n = len(data)
    for i in range(n):
        ...

def QuickSort():
    ...

def HeapSort():
    

def MergeSort():
    pass
import sys


class MaxHeap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = sys.maxsize

    def insert(self, ele):
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.Heap[self.size] = ele
        i = self.size
        temp = self.Heap[i]

        while i > 1 and temp > self.Heap[i // 2]:
            self.Heap[i] = self.Heap[i // 2]
            i = i // 2

        self.Heap[i] = temp

    def delete(self):
        x = self.Heap[1]
        self.Heap[1] = self.Heap[self.size]
        self.Heap[self.size] = x
        i = 1
        j = i * 2

        while j < self.size - 1:
            if self.Heap[j + 1] > self.Heap[j]:
                j = j + 1
            if self.Heap[i] < self.Heap[j]:
                self.Heap[i], self.Heap[j] = self.Heap[j], self.Heap[i]
                i = j
                j = 2 * j
            else:
                break
        self.size -= 1
        return x

    def display(self):
        print(self.Heap[1:self.size+1])


def main():
    arr = [10, 20, 30, 25, 5, 40, 35]
    h = MaxHeap(15)
    for i in range(len(arr)):
        h.insert(arr[i])
    print(h.delete())
    print(h.delete())
    h.display()


if __name__ == '__main__':
    main()

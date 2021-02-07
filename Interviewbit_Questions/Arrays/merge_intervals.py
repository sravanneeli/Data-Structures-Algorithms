def insert(intervals, new_interval):
    intervals.append(new_interval)
    intervals.sort(key=lambda x: x[0])
    output = [intervals[0]]
    for i in range(1, len(intervals)):
        if intervals[i][0] <= output[-1][1]:
            output[-1][1] = max(output[-1][1], intervals[i][1])
        else:
            output.append(intervals[i])

    return output


def main():
    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    new_interval = [4, 9]
    print(f"Merged after insertion of new interval {insert(intervals, new_interval)}")


if __name__ == '__main__':
    main()

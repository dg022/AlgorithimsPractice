from __future__ import print_function

#Time Complexity: O(nlogn)
#Space Complexity: O(n)
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


def merge(intervals):
    merged = []

    # Sort the intervals array, based on the start property
    intervals.sort(key=lambda x: x.start)

    start = intervals[0].start
    end = intervals[0].end

    for i in range(1, len(intervals)):

        # Visuallly, this means there is overlao, either partial or complee
        if intervals[i].start <= end:
            end = max(end, intervals[i].end)
        else:
            merged.append(Interval(start, end))
            start = intervals[i].start
            end = intervals[i].end

    merged.append(Interval(start, end))
    return merged


def main():
    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
        i.print_interval()
    print()


main()
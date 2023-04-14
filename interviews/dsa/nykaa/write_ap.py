def write_ap(start, end, diff):
    if diff < 0 and start < end:
        return

    if start > end and diff > 0:
        return
    print(start)
    write_ap(start + diff, end, diff)


if __name__ == '__main__':
    write_ap(2, -5, -1)

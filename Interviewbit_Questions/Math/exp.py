def time2min(time):
    if "AM" in time:
        if time[:2] != '12':
            ans = int(time[:2]) * 60 + int(time[3:5])
        else:
            ans = int(time[3:5])
    else:
        if time[:2] != '12':
            ans = (int(time[:2]) + 12) * 60 + int(time[3:5])
        else:
            ans = 720 + int(time[3:5])

    return ans


def main():
    time1 = "01:01 PM"
    time2 = "02:01 AM"
    print(time2min(time1), time2min(time2))


if __name__ == '__main__':
    main()

# hackerRank Time conversion


def timeConversion(s):
    if s[-2:] == "AM" and s[:2] == "12":
        return "00" + s[2:-2]
    elif s[-2:] == "AM":
        return s[:-2]
    elif s[-2:] == "PM" and s[:2] == "12":
        return s[:-2]
    else:
        ans = int(s[:2]) + 12
        return str(str(ans) + s[2:8])


print(timeConversion("07:05:45PM"))
print(timeConversion("12:00:00AM"))
print(timeConversion("12:00:00PM"))

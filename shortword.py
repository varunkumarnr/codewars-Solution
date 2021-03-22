def find_short(s):
    arr = s.split(" ")
    arr.sort(key=len)
    return len(arr[0])


find_short("bitcoin take over the world maybe who knows perhaps")
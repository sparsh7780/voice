hr = int(input("Enter number of hours\n"))
min = int(input("Enter number of minutes\n"))
sec = int(input("Enter number of seconds\n"))
ps = float(input("Enter playback speed\n"))


total_sec = hr*60*60 + min*60 + sec

print(total_sec)

time = total_sec/ps
print(time)

hr_sec = time/3600
min_sec = time/60

print(f"{hr_sec}: hours")
print(f"{min_sec}: mins")

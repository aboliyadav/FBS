# Convert the time entered in hh,min and sec into seconds.

hour =int(input("Enter hours :"))
minute = int(input("Enter minute :"))
seconds = int(input("Enter seconds:"))

total_seconds = hour * 3600 + minute * 60 + seconds

print('Total seconds', total_seconds)

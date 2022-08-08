t = int(input('Enter which time in seconds do you want to transform to hours, minutes and seconds:'))
h = t // 3600
s = t % 60
m = ((t - t % 60) // 60) - h * 60
print(f'{h:02}:{m:02}:{s:02}')




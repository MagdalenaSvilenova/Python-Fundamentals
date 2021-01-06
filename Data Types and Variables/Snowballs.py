snowballs = int(input())
max_value = 0
max_snow = 0
max_time = 0
max_quality = 0

for n in range(1, snowballs+1):
    snow = int(input())
    time = int(input())
    quality = int(input())
    value = (snow / time) ** quality
    if max_value < value:
        max_value = value
        max_snow=snow
        max_time=time
        max_quality=quality
    value = 0

print(f'{max_snow} : {max_time} = {int(max_value)} ({max_quality})')

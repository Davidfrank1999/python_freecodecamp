import re



def add_time(start, duration,day=''):
    
    pattern= "[:\s]"
    start= re.split(pattern, start)
    duration= re.split(pattern, duration)
    
    add_hr= int(start[0]) + int(duration[0])
    min_add=int(start[1]) + int(duration[1])
    
    time_hr=0
    time_min=0
    unit=''
    n_day=0
    
    # Calculating Min of the time
    
    if min_add<60:
        time_min= min_add
    else:
        time_min= min_add - 60
        add_hr +=1
        
    if time_min<10:
        time_min=f'0{time_min}'

    
    # convert to 24hrs
    if start[2]=="PM":
        add_hr+= 12
        
    # detr\ermining n_days
    n_day=add_hr//24
    add_hr=add_hr%24
    unit='AM'
    # 24 hrs to 12hrs
    if add_hr==0:
        add_hr=12
        unit='AM'
    elif add_hr>12:
        add_hr-=12
        unit='PM'
    elif add_hr==12:
        unit='PM'
    
    time_hr=add_hr

    
    
    
    new_time=(f'{time_hr}:{time_min} {unit}')
    

 
        
    if n_day==1:
        # determining days
        if day:
            day=day_convertion(day,n_day)
            new_time=(f'{time_hr}:{time_min} {unit}, {day} (next day)')
        else:
            new_time=(f'{time_hr}:{time_min} {unit} (next day)')
    elif n_day>1:
        # determining days
        if day:
            day=day_convertion(day,n_day)
            new_time=(f'{time_hr}:{time_min} {unit}, {day} ({n_day} days later)')
        else:
            new_time=(f'{time_hr}:{time_min} {unit} ({n_day} days later)')
    elif day:
        new_time=(f'{time_hr}:{time_min} {unit}, {day}')
 
    return new_time

# Determining the Day of the week
def day_convertion(start_day,n_day):
    day_of_week=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    day_of_week_lower=[day.lower() for day in day_of_week]
        
    day_index=day_of_week_lower.index(start_day.lower())
    
    # Incrementing n days
    day_index+= n_day

    if day_index>=7:
        day_index= day_index%7
    

    return day_of_week[day_index]


print(add_time('3:00 PM', '3:10'))
print(add_time('11:30 AM', '2:32', 'Monday'))
print(add_time('2:59 AM', '24:00'))

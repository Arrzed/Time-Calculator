def add_time(starting_time,duration_time,day=False):
    times = starting_time.split()
    time_of_day = times[1]
    st_time = times[0].split(':') # 'starting time' that tracks the result

    d_time = duration_time.split(':')
    hours = int(d_time[0]) # hours to add
    minutes = int(d_time[1]) # minutes to add

    day_count = 0 # keeps track of counting extra days

    st_time[0] = int(st_time[0]) + hours
    st_time[1] = int(st_time[1]) + minutes

    if st_time[1] >= 60 :
        st_time[0] = st_time[0] + 1
        st_time[1] = st_time[1] - 60
    
    while st_time[0] > 12 :
        if time_of_day == 'PM' :
            day_count = day_count + 1
            time_of_day = 'AM'
        else :
            time_of_day = 'PM'

        st_time[0] = st_time[0] - 12

    if st_time[0] == 12 :
        if time_of_day == 'PM' :
            day_count = day_count + 1
            time_of_day = 'AM'
            #st_time[0] = 0
        else :
            time_of_day = 'PM'

    # formatted time to return
    total = str(st_time[0]) + ':' + str(st_time[1]).zfill(2)
    total = total + ' ' + time_of_day
  
    if day is False and day_count > 1 :
        total = total + ' (' + str(day_count) + ' days later)'
    if day is False and day_count == 1 :
        total = total + ' (next day)'
    
    if day is not False :
        if day_count > 0 :
            # create list with days of the week to show correct day        
            week = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
            day = day.lower().capitalize()
            i = 0
            while i < len(week) - 1 :
                if week[i] == day :
                    break
                i += 1

            i = i + day_count
            
            while i > 6 :
                i = i - 7

            if day_count == 1 :
                total = total + ', ' + week[i] + ' (next day)'
            else:
                total = total + ', ' + week[i] + ' (' + str(day_count) + ' days later)'
        else :
            total = total + ', ' + day

    return(total)

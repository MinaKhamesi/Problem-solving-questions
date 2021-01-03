def calendarMatching( calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
    updatedCalendar1 = updateCalendar(calendar1, dailyBounds1)
    updatedCalendar2 = updateCalendar(calendar2, dailyBounds2)
    mergedCalendar = merge(updatedCalendar1, updatedCalendar2)
    calendar = flatten(mergedCalendar)
    return findAvailabilities(calendar , meetingDuration)

def updateCalendar(calendar , bound):
    newCalendar = calendar[:]
    newCalendar.insert(0,['0:00',bound[0]])
    newCalendar.append([bound[1] , '23:59'])
    return list(map( lambda x: [timeToMinutes(x[0]) , timeToMinutes(x[1])],newCalendar))

def merge(calendar1 , calendar2):
    merged = []
    idx1 , idx2 = 0, 0
    while idx1 < len(calendar1) and idx2 < len(calendar2):
        if calendar1[idx1][0] < calendar2[idx2][0]:
            merged.append(calendar1[idx1])
            idx1 += 1
        else:
            merged.append(calendar2[idx2])
            idx2 += 1
    while idx1 < len(calendar1):
        merged.append(calendar1[idx1])
        idx1 += 1
    while idx2 < len(calendar2):
        merged.append(calendar2[idx2])
        idx2 += 1
    return merged

def flatten(calendar):
    if not len(calendar) : return []
    result = [calendar[0]]
    prev = result[-1]
    for i in range(1 ,len(calendar)):
        start , end = calendar[i]
        if start <= prev[1]:
            prev[1] = max(end , prev[1])
        else:
            result.append(calendar[i])
            prev = result[-1]
    return result

def findAvailabilities(calendar , duration):
    availabilities = []
    for i in range(1, len(calendar)):
        currentStart = calendar[i][0]
        prevEnd = calendar[i - 1][1]
        if currentStart - prevEnd >= duration:
            availabilities.append([prevEnd , currentStart])
    return list(map(lambda time: [minutesToTime(time[0]) , minutesToTime(time[1])],availabilities))

def timeToMinutes(time):
    hours , minutes = list(map( int ,time.split(':')))
    totalMins = hours * 60 + minutes
    return totalMins

def minutesToTime(minutes):
    hours = minutes // 60
    mins = minutes % 60
    hourStr = str(hours)
    minsStr = str(mins) if mins > 10 else '0'+str(mins)
    return ':'.join([hourStr , minsStr])

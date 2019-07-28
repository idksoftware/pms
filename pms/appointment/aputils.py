'''
Created on Feb 19, 2014

@author: wzw7yn
'''


from datetime import datetime
from datetime import timedelta

def dayStr(idx):
    day = "Mon","Tues","Wen","Thur","Fri","Sat","Sun","Mon","Tues","Wen","Thur","Fri","Sat","Sun"
    return day[idx]

def MonthStr(idx):
    
    if idx > 12:
        idx = idx % 12
    if idx < 0:
        idx = 12 + idx
    idx = idx - 1
    month = ( "Jan", "Feb", "March", "April", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec")
    return month[idx]


def GetSelectDayStr(date):
    day = date.day
    month = date.month
    year = date.year
    start = datetime(year, month, day, 01, 01, 00)
    end = datetime(year, month, day, 23, 01, 00)
    startStr = start.strftime("%d-%m-%Y %H:%M")
    endStr = end.strftime("%d-%m-%Y %H:%M")
    return "select * from appointment, patent where time between \'"+ startStr + "\' and \'" + endStr + "\' and Appointment.patent_id = patent.patent_id;"

def lastDayOfMonth(dt):
    next_month = (dt.month % 12) + 1
    end_date = datetime(dt.year, next_month, 1)
    end_date = end_date - timedelta(days=1)
    return end_date

def lastDayOfYear(dt):
    next_year = (dt.year + 1)
    end_date = datetime(next_year, 1, 1)
    end_date = end_date - timedelta(days=1)
    return end_date

def GetSelectMonthStr(date, mth):

    if mth < 13:
        month = date.month + mth
        year = date.year
    else:
        month = date.month + mth % 12
        year = date.year + mth / 12
    start = datetime(year, month, 1, 00, 01, 00)
    end = lastDayOfMonth(start)
    startStr = start.strftime("%d-%m-%Y %H:%M")
    endStr = end.strftime("%d-%m-%Y %H:%M")
    return "select * from appointment, patent where time between \'"+ startStr + "\' and \'" + endStr + "\' and Appointment.patent_id = patent.patent_id;"
    #return "select * from patent where surname like " + whereStr[idx] + " order by time;"

def GetSelectYearStr(self, date):

        year = date.year
        start = datetime(year, 1, 1, 01, 01, 00)
        end = self.lastDayOfYear(start)
        startStr = start.strftime("%d-%m-%Y %H:%M")
        endStr = end.strftime("%d-%m-%Y %H:%M")
        return "select * from appointment, patent where time between \'"+ startStr + "\' and \'" + endStr + "\' and Appointment.patent_id = patent.patent_id;"
        #return "select * from patent where surname like " + whereStr[idx] + " order by time;"

def GetSelectAllStr(self):

    return "select * from appointment, patent where Appointment.patent_id = patent.patent_id;"

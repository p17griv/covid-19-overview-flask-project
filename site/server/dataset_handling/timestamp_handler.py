def format_handler(time_list):
    for tpl in time_list:
        if "T" in tpl:
            timstmp = TimeStamp(tpl[5:7], tpl[8:10], tpl[0:5], tpl[11:13], tpl[14:16], tpl[17:])
            tpl = timstmp
        else:
            date_time = tpl.split(" ")
            tstp = TimeStamp(date_time[0][1], date_time[0][2:4], date_time[0][5:], date_time[1][0:3], date_time[1][4:])
            tpl = tstp

class TimeStamp:
    def __init__(self, month, day, year, hour, minute, second="0"):
        self.month = month
        self.day = day
        if len(year) == 2:
            self.year = "20" + year
        else:
            self.year = year
        self.hour = hour
        self.minute = minute
        self.second = second

    def get_timestamp(self):
        return self.month + "/" + self.day + self.year + " " + self.hour + ":" + self.minute + ":" + self.second

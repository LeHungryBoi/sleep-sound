import re
from dataclasses import dataclass

@dataclass
class TimePeriod:
    time_begin: int
    time_peak: int
    time_over: int
    time_begin_sequential:
    time_peak_sequential:
    
period_1 = TimePeriod(2200, 300, 800)
period_2 = TimePeriod(1330, 1500, 1730)


def ConvertToSequentialTime(p_time_begin, p_time_over):
    if(p_time_over < p_time_begin):
        time_begin_sequential = p_time_begin
        time_over_sequential = p_time_over + 2400
    else:
        time_begin_sequential = p_time_begin
        time_over_sequential = p_time_over

def ConvertToMinute(p_time):
    t_hour = 0
    t_minute = 0
    
    if(p_time < 1000):
        t_hour = re.search(r"^(\d{1})", p_time)
        t_minute = re.search(r"(\d{2})$", p_time)
    else:
        t_hour = re.search(r"^(\d{2})", p_time)
        t_minute = re.search(r"(\d{2})$", p_time)
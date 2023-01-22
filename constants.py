from enum import Enum, auto
class Month(str, Enum):
    JAN = "January"
    FEB = "February"
    MAR = "March"
    APR = "April"
    MAY = "May"
    JUN = "June"
    JUL = "July"
    AUG = "August"
    SEP = "September"
    OCT = "October"
    NOV = "November"
    DEC = "December"
    def __str__(self) -> str:
        return str.__str__(self)
    def __int__(self) -> int:
        match self:
            case Month.JAN: return 1
            case Month.FEB: return 2
            case Month.MAR: return 3
            case Month.APR: return 4
            case Month.MAY: return 5
            case Month.JUN: return 6
            case Month.JUL: return 7
            case Month.AUG: return 8
            case Month.SEP: return 9
            case Month.OCT: return 10
            case Month.NOV: return 11
            case Month.DEC: return 12
    def days(self) -> int:
        if int(self) == 2: return 28
        if int(self) < 8 and int(self) % 2 == 1: return 31
        if int(self) >= 8 and int(self) % 2 == 0: return 31
        else: return 30

class Weekday(str, Enum):
    MON = "Monday"
    TUE = "Tuesday"
    WED = "Wednesday"
    THU = "Thursday"
    FRI = "Friday"
    SAT = "Saturday"
    SUN = "Sunday"
    def __str__(self) -> str:
        return str.__str__(self)
            
MONTHS = [Month.JAN, Month.FEB, Month.MAR, Month.APR, Month.MAY, Month.JUN, Month.JUL, Month.AUG, Month.SEP, Month.OCT, Month.NOV, Month.DEC]

import calendar


class MyCalendar(calendar.Calendar):
    def count_weekday_in_year(self, year: int, weekday: int):
        if not int.is_integer(year) and not (year >= 1 and year <= 9999):
            raise ValueError("The parameter 'year' has not a valid value!")
        if not int.is_integer(weekday) and not (weekday >= 0 and weekday <= 6):
            raise ValueError("The parameter 'weekday' has not a valid value!")

        count = 0
        for month in range(1, 13):
            for week in self.monthdays2calendar(year, month):
                for day, wd in week:
                    if day != 0 and wd == weekday:
                        count += 1

        return count


mc = MyCalendar()

print(mc.count_weekday_in_year(year=2019, weekday=0))
print(mc.count_weekday_in_year(year=2000, weekday=6))

import pandas as pd
import datetime
from datetime import datetime as datetime_2


class DateWrapper:
    def __init__(self):
        pass

    @staticmethod
    def get_date_range(start_date: str, end_date) -> list:
        dates = pd.date_range(start=start_date, end=end_date)

        dates_string = []
        for i in dates:
            dates_string.append(str(i.date()))

        return dates_string

    @staticmethod
    def get_date_range_datetime(start_date: str, end_date: str) -> list:
        dates = pd.date_range(start=start_date, end=end_date)

        dates_datetime = []
        for i in dates:
            dates_datetime.append(i.date())

        return dates_datetime

    @staticmethod
    def get_date_range_from_period(period: int = 28) -> list:
        dates = pd.date_range(end=datetime_2.today(), periods=period).to_pydatetime().tolist()

        dates_string = []
        for i in dates:
            dates_string.append(str(i.date()))

        return dates_string

    @staticmethod
    def get_hour_range(start_hour: int = 0, end_hour: int = 23) -> list:
        if start_hour > end_hour:
            raise ValueError("start should't grater than end")

        hour_range = list(range(start_hour, end_hour + 1, 1))

        return hour_range

    @staticmethod
    def get_bucket_date_path():
        today = datetime.datetime.today()
        return f"{today.year}/{today.month}/{today.day}"

    @staticmethod
    def get_date_from_string_with_slash(date_string: str) -> datetime:
        return datetime.datetime.strptime(date_string, "%m/%Y")

    @staticmethod
    def get_default_date_list() -> list:
        start_date = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        end_date = datetime.datetime.now().replace(hour=23, minute=59, second=59, microsecond=0)

        return DateWrapper.get_date_range(start_date, end_date)

    @staticmethod
    def get_default_date_list_date_object() -> list:
        start_date = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        end_date = datetime.datetime.now().replace(hour=23, minute=59, second=59, microsecond=0)

        return DateWrapper.get_date_range_datetime(start_date, end_date)

    @staticmethod
    def get_date_list(date_list) -> list:

        dates = []
        for date_object in date_list:
            start_date = date_object["start"]
            end_date = date_object["end"]
            date_range = DateWrapper.get_date_range(start_date, end_date)
            for date in date_range:
                if date not in dates:
                    dates.append(date)

        return dates

    @staticmethod
    def get_hour_list(hour_list) -> list:

        hours = []
        for hour_object in hour_list:
            start_hour = hour_object["from"]
            end_hour = hour_object["to"]
            start_hour = datetime.datetime.strptime(start_hour, '%I:%M %p').hour
            end_hour = datetime.datetime.strptime(end_hour, '%I:%M %p').hour
            hour_range = DateWrapper.get_hour_range(start_hour=start_hour, end_hour=end_hour)
            for hour in hour_range:
                if hour not in hours:
                    hours.append(hour)

        return hours

    @staticmethod
    def get_weekdays(date_list: list) -> list:

        weekdays = []
        for date in date_list:
            weekday = datetime.datetime.strptime(date, "%Y-%m-%d").weekday() + 1  # +1 for 1- 7 in datebase format
            if weekday not in weekdays:
                weekdays.append(weekday)

        return weekdays

    @staticmethod
    def get_weekdays_without_distirct(date_list: list) -> list:

        weekdays = []
        for date in date_list:
            weekday = datetime.datetime.strptime(date, "%Y-%m-%d").weekday() + 1  # +1 for 1- 7 in datebase format
            weekdays.append(weekday)

        return weekdays

    @staticmethod
    def get_weekday(date: str) -> int:

        return datetime.datetime.strptime(date, "%Y-%m-%d").weekday() + 1  # +1 for 1- 7 in datebase format

    @staticmethod
    def check_date_list(date_list: list) -> list:
        dates = []
        for date in date_list:
            try:
                if isinstance(date, datetime.date):
                    dates.append(date.strftime("%Y-%m-%d"))

                elif type(date) == str:
                    date_object = datetime.datetime.strptime(date, "%Y-%m-%d")
                    dates.append(date)

            except Exception as e:
                print("check_date_list", e)

        return dates

    @staticmethod
    def get_date_objects(date_list: list) -> list:

        dates = []
        for date in date_list:
            date = datetime.datetime.strptime(date, "%Y-%m-%d")
            if date not in dates:
                dates.append(date)

        return dates

    @staticmethod
    def date_to_datetime_list(date_list: list) -> list:

        dates = []
        for date in date_list:
            date = datetime_2.combine(date.today(), datetime_2.min.time())
            if date not in dates:
                dates.append(date)

        return dates

    @staticmethod
    def get_day_parting_hour(day_partition, week_day):
        for item in day_partition:
            if item.day == week_day:
                return item.hour

        return []

    @staticmethod
    def get_date_from_string(date_string):
        date_time_obj = datetime.datetime.strptime(date_string, '%Y-%m-%d')
        return date_time_obj.date()

    @staticmethod
    def get_today_object():
        return datetime.datetime.now().date()

    @staticmethod
    def date_object_to_str(date_object):
        return date_object.strftime('%Y-%m-%d')

    @staticmethod
    def get_date_string_from_date_object(date_object=datetime.datetime.now().date()):
        return date_object.strftime('%Y-%m-%d')

    @staticmethod
    def get_n_day_before_date_object(day: int = 2, date_object=datetime.datetime.now().date()):
        return date_object - datetime.timedelta(days=day)

    @staticmethod
    def date_to_datetime(date_object):
        date_object = datetime.datetime.combine(date_object, datetime.datetime.min.time()) # date to datetime
        return date_object


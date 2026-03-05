import datetime
import pytz

def convert_time(src_tz, dest_tz, hour, minute):
    try:
        source = pytz.timezone(src_tz)
        dest = pytz.timezone(dest_tz)
        
        now = datetime.datetime.now()
        local_time = source.localize(datetime.datetime(now.year, now.month, now.day, hour, minute))
        
        converted = local_time.astimezone(dest)
        
        print(f"\nsource ({src_tz}): {local_time.strftime('%h:%m %p')}")
        print(f"destination ({dest_tz}): {converted.strftime('%h:%m %p')}")
        print(f"date: {converted.strftime('%y-%m-%d')}")
        
    except pytz.exceptions.UnknownTimeZoneError:
        print("invalid time zone name. try 'america/new_york' or 'asia/kolkata'.")
    except ValueError:
        print("invalid time input. use 24-hour format.")

if __name__ == "__main__":
    print("common zones: utc, america/new_york, europe/london, asia/kolkata, australia/sydney")
    
    tz_from = input("enter source time zone: ")
    tz_to = input("enter target time zone: ")
    h = int(input("enter hour (0-23): "))
    m = int(input("enter minute (0-59): "))
    
    convert_time(tz_from, tz_to, h, m)
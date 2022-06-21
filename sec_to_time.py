def sec_to_time_format(dur, hours_per_day=24):
    days = dur // (3600*hours_per_day)
    dur = dur % (3600*hours_per_day)
    hours = dur // 3600
    dur = dur % 3600
    minutes = dur // 60
    seconds = dur % 60
    return f'{days} days {hours} hours {minutes} minutes {seconds} seconds'

def main():
    dur = 1975794
    duration = sec_to_time_durations(dur)
    print(duration)

if __name__ == '__main__':
    main()

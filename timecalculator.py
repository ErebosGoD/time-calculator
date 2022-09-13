def add_time():
    minutes = 0
    hours = 0
    hours_to_add = []
    minutes_to_add = []

    time_count_to_add = int(input("How many times do you want to add?"))
    while time_count_to_add > 0:
        hours_to_add.append(int(input("How many hours?: ")))
        minutes_to_add.append(int(input("How many minutes?: ")))
        time_count_to_add -= 1

    for hour in hours_to_add:
        hours += hour

    for minute in minutes_to_add:
        minutes += minute

    while minutes > 60:
        if minutes >= 60:
            hours += 1
            minutes -= 60
    print(f"Total time = {hours} hours and {minutes} minutes")


add_time()

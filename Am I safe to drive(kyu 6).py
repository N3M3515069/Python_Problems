from datetime import datetime


def drive(drinks, finished, drive_time):
    total_units = 0
    for i in drinks:

        units = (i[0] * i[1]) / 1000
        total_units += units

    time1 = finished
    time2 = drive_time
    t1 = datetime.strptime(time1, "%H:%M")
    t2 = datetime.strptime(time2, "%H:%M")

    delta = t2 - t1
    total_time = delta.seconds
    final_output = total_time/3600.0

    if final_output > total_units:

        return [float(format(total_units, ".2f")), True]
    else:
        return [float(format(total_units, ".2f")), False]


print(drive([[10.0, 100]], "20:00", "21:00"))

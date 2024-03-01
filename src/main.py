import datetime
from send_email import send_notification
from fng import calculate_average_fng, check_average

if __name__ == "__main__":
    url = "https://api.alternative.me/fng/"
    threshold_value = 20
    average = calculate_average_fng(url)

    if check_average(average, threshold_value):
        send_notification('IMPORTANT: FNG value below threshold', f"Average FNG value ({average}) is below ({threshold_value}).")

    if datetime.datetime.now().weekday() == 0:
          send_notification("Weekly FNG test", f"The current FNG value is {average}.")

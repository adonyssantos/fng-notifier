import datetime
from send_email import send_notification
from fng import calculate_average_fng, check_average

if __name__ == "__main__":
    url = "https://api.alternative.me/fng/"

    # If FNG avg in the last 60 days is 20 or less the bot will buy the 100%
    threshold_value = 20
    average = calculate_average_fng(url, 60)
    if check_average(average, threshold_value):
        send_notification(
            'IMPORTANT: FNG value below threshold',
            f"Average FNG value ({average}) is below ({threshold_value}). \n\nIt's a good time to buy the 100%."
        )
        exit()

    # If FNG avg in the last 30 days is 20 or less the bot will buy the 50%
    threshold_value = 20
    average = calculate_average_fng(url, 30)
    if check_average(average, threshold_value):
        send_notification(
            'IMPORTANT: FNG value below threshold',
            f"Average FNG value ({average}) is below ({threshold_value}). \n\nIt's a good time to buy the 50%."
        )
        exit()

    # If FNG avg in the last 60 days is 80 or more the bot will sell the 100%
    threshold_value = 80
    average = calculate_average_fng(url, 60)
    if check_average(threshold_value, average):
        send_notification(
            'IMPORTANT: FNG value above threshold',
            f"Average FNG value ({average}) is above ({threshold_value}). \n\nIt's a good time to sell the 100%."
        )
        exit()

    # If FNG avg in the last 30 days is 80 or more the bot will sell the 50%
    threshold_value = 80
    average = calculate_average_fng(url, 30)
    if check_average(threshold_value, average):
        send_notification(
            'IMPORTANT: FNG value above threshold',
            f"Average FNG value ({average}) is above ({threshold_value}). \n\nIt's a good time to sell the 50%."
        )
        exit()

    # If it's Monday, send a weekly test email
    if datetime.datetime.now().weekday() == 0:
        send_notification(
            "Weekly FNG test",
            f"The current FNG value is {average}."
        )
        exit()

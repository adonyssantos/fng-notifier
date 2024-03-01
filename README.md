# Fear and Greed Index Notifier

## Overview

Fear and Greed Index Notifier is a Python script that fetches data from the Fear and Greed Index API and calculates the average value over the last 30 days. If the average value is below 20, it sends a notification via email. Additionally, it sends periodic notifications to validate that the cron job is active.

## Features

- Fetches data from the Fear and Greed Index API.
- Calculates the average value over the last 30 days.
- Sends an email notification if the average value is below 20.
- Sends periodic notifications to validate the cron job status.

## Requirements

- Python 3.x
- `requests` library
- SMTP server for sending email notifications
- Cron job scheduler

## Environment Variables

Check the `.env.example` file to see the required environment variables.

## Scripts

### Dependencies Installation

To install the dependencies, run the following command:

```bash
pip install -r requirements.txt
```

### Run the Script

To run the script, execute the following command:

```bash
python src/main.py
```

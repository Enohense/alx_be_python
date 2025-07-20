# daily_reminder.py

task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task."
    case "medium":
        message = f"Note: '{task}' is a medium priority task."
    case "low":
        message = f"Note: '{task}' is a low priority task."
    case _:
        message = f"'{task}' has an unspecified priority"

if time_bound == "yes":
    message += " that requires immediate attention today!"
elif time_bound == "no":
    message += " Consider completing it when you have free time."
else:
    message += ". Enter a valid time bound."

print(f" {message}")

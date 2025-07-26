import warnings

warnings.filterwarnings('ignore')

def log_filter(logs: str, level: str):
    for line in logs.strip().split('\n'):
        if f' {level} ' in line:
            yield line

logs = (
    "2023-08-15 14:15:24 INFO Starting the system.\n"
    "2023-08-15 14:15:26 WARN System load is above 80%.\n"
    "2023-08-15 14:15:27 ERROR Failed to connect to database.\n"
    "2023-08-15 14:15:28 INFO Connection retry in 5 seconds.\n"
)

to_test = list(log_filter(logs, level="ERROR"))

print(to_test)

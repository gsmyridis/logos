from datetime import datetime
from logos.settings.globals import LOG_FILE


def log_action(action: str, action_type: str):
    """Logs an action and action type."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp}: {action_type} : {action}\n"
    with open(LOG_FILE, 'a') as file:
        file.write(log_entry)


def reset_log():
    """Resets the log by truncating the log file."""
    with open(LOG_FILE, 'w') as file:
        file.truncate(0)


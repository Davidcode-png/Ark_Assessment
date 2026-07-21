import pandas as pd

"""
The notification system is designed as an event-driven layer
that emits structured events during backtest execution.
Each notification includes a timestamp, event type, severity,
and human-readable message, allowing the same interface to be connected to
logging systems, Slack, or monitoring tools in a production environment.
"""


def emit_notification(notifications, event, severity, message, **details):
    notifications.append(
        {
            "timestamp": pd.Timestamp.now(),  # or the candle's close_time
            "event": event,
            "severity": severity,
            "message": message,
            **details,
        }
    )
    # We can also log this to a file or send it to an external system if needed like slack.


def store_notifications_to_csv(notifications, file_path):
    df = pd.DataFrame(notifications)
    df.to_csv(file_path, index=False, mode="w")

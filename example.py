from logger import EventLogger
import os

def main():
    # Replace with your actual MongoDB connection string
    # For local test: 'mongodb://localhost:27017/'
    MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017/")
    DB_NAME = "event_tracking"
    
    logger = EventLogger(MONGODB_URI, DB_NAME)

    print("Logging dummy events...")
    
    # Log some example events
    logger.log_event("app_start", {"version": "1.0.0"})
    logger.log_event("user_action", {"action": "click", "button": "login"})
    logger.log_event("data_processed", {"items": 50, "status": "success"})

    print("Retrieving the last 5 events:")
    recent_events = logger.get_recent_events(limit=5)
    for event in recent_events:
        print(f"[{event['timestamp']}] {event['event_type']}: {event['metadata']}")

    logger.close()

if __name__ == "__main__":
    main()

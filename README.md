# MongoDB Event Logger

A simple and efficient Python-based event logging system that stores events and timestamps in a MongoDB database.

## Features 
- **Easy Integration**: Simple class-based interface to log events.
- **Automated Timestamps**: Every event is automatically timestamped using UTC time.
- **Flexible Metadata**: Store any additional data as a dictionary along with the event.
- **Querying**: Basic functionality to retrieve recent events.

## Project Structure
- `logger.py`: Contains the `EventLogger` class which handles MongoDB connections and logging operations.
- `example.py`: A demonstration script showing how to initialize the logger and record events.
- `requirements.txt`: List of required Python packages (`pymongo`).

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/REPLACE_WITH_YOUR_USERNAME/mongo-event-logger.git
   cd mongo-event-logger
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

```python
from logger import EventLogger

# Initialize the logger
logger = EventLogger("mongodb://localhost:27017/", "my_database")

# Log an event
logger.log_event("user_signup", {"user_id": 123, "source": "web"})

# Retrieve recent events
events = logger.get_recent_events(limit=5)
for e in events:
    print(e)
```

## Configuration
It is recommended to use environment variables for your MongoDB URI:
```bash
export MONGODB_URI="mongodb+srv://user:pass@cluster.mongodb.net/test"
```
Or use a `.env` file (ensure it's added to `.gitignore`).

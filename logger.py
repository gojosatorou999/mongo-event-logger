import datetime
from pymongo import MongoClient
from typing import Any, Dict, Optional

class EventLogger:
    def __init__(self, connection_string: str, database_name: str, collection_name: str = "events"):
        """
        Initializes the MongoDB Event Logger.
        
        :param connection_string: MongoDB connection URI.
        :param database_name: Name of the database to use.
        :param collection_name: Name of the collection to store events (default: 'events').
        """
        self.client = MongoClient(connection_string)
        self.db = self.client[database_name]
        self.collection = self.db[collection_name]

    def log_event(self, event_type: str, metadata: Optional[Dict[str, Any]] = None):
        """
        Logs an event to MongoDB.
        
        :param event_type: The name/type of the event (e.g., 'user_login').
        :param metadata: Optional dictionary containing additional event data.
        """
        event_document = {
            "event_type": event_type,
            "timestamp": datetime.datetime.utcnow(),
            "metadata": metadata or {}
        }
        
        result = self.collection.insert_one(event_document)
        return result.inserted_id

    def get_recent_events(self, limit: int = 10):
        """
        Retrieves recent events from the database.
        
        :param limit: Number of events to retrieve (default: 10).
        """
        return list(self.collection.find().sort("timestamp", -1).limit(limit))

    def close(self):
        """Closes the MongoDB connection."""
        self.client.close()

import json
from datetime import datetime
from typing import Dict, Any
def load_flight_data(filename: str) -> Dict[str, Any] :
    """
    Load flight data from a JSON file.
    Args:
        Filename: Path to JSON file
        Returns:
            Dictionary containing flight data
    """
    try:
        with open(filename,"r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: {filename} not found!")
        raise
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in {filename}")
        raise
def parse_datetime(dt_string: str) -> datetime:
    """Parse ISO format datetime string"""
    return datetime.fromisoformat(dt_string)
def is_delayed(scheduled: str, actual: str,threshold_minutes: int=15) -> bool:
    """
    Check if flight is delayed.
    Args:
        scheduled: Scheduled time (ISO format)
        actual: Actual time (ISO format)
        threshold_minutes: Minutes before considered delayed
    Returns:
        True if delayed, False otherwise
    """
    sched_dt = parse_datetime(scheduled)
    actual_dt = parse_datetime(actual)
    delay_minutes = (actual_dt - sched_dt).total_seconds() / 60
    return delay_minutes > threshold_minutes
def format_flight_summary(flight: Dict[str, Any]) -> str:
    """Create a nice formatted summary of flight"""
    departure = flight["departure"]
    arrival = flight["arrival"]

    summary = f"""
Flight {flight['flight_number']}
{departure['airport']} → {arrival['airport']}

Departure:
  Scheduled: {departure['scheduled']}
  Actual:    {departure['actual']}
  Status:    {'DELAYED' if is_delayed(departure['scheduled'], departure['actual']) else 'ON TIME'}

Arrival:
  Scheduled: {arrival['scheduled']}
  Estimated: {arrival['estimated']}
"""
    return summary
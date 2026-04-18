from flight_parser import load_flight_data, format_flight_summary

def main():
    # Load sample flight
    flight = load_flight_data("data/sample_flights.json")
    
    # Print summary
    print(format_flight_summary(flight))

if __name__ == "__main__":
    main()
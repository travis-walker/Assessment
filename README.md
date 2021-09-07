# Problem 2

This is a program that takes in a csv file of station data and state code and outputs a JSON file containing statistics
about the stations in that state.

Run the program from the command line in the format
`python analyze_elevation_by_state.py <data_file_name> <state code>`

Output is saved to a file named elevation_report_*<state_code>*.json

You will need python 3.7+ with pandas installed to run the program.

## Sample output:

    {
        "state": "NV",
        "total_stations": 868,
        "median_elevation": 5130.5,
        "average_elevation": 5209.55,
        "max_elevation_station": {
            "name": "CAVE MOUNTAIN",
            "elevation": 10583.0,
            "latitude": "39.16",
            "longitude": "-114.61"
        },
        "min_elevation_station": {
            "name": "RENO 0.6 ENE",
            "elevation": 456.0,
            "latitude": "39.54374",
            "longitude": "-119.81306"
        },
        "stations_missing_elevation_data": 48,
        "stations_over_sea_level": 820,
        "stations_over_2000_feet": 782,
        "stations_over_4000_feet": 676,
        "stations_over_6000_feet": 246
    }
import json
import sys

import pandas as pd


def is_valid_state_code(code):
    return code in ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA",
                    "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM",
                    "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA",
                    "WV", "WI", "WY"]


def load_data_from_file(file_name):
    df = pd.DataFrame()
    try:
        df = pd.read_csv(file_name)
    except FileNotFoundError:
        print("File name is invalid. Please check and try again.")
    return df


def generate_elevation_statistics_report(df):
    min_elevation_index = df.elev.idxmin()
    max_elevation_index = df.elev.idxmax()
    min_row = df.loc[min_elevation_index].to_dict()
    max_row = df.loc[max_elevation_index].to_dict()
    report = {
        "state": df.state.iloc[0],
        "total_stations": df.shape[0],
        "median_elevation": round(df.elev.median(), 2),
        "average_elevation": round(df.elev.mean(), 2),
        "max_elevation_station": {
            "name": max_row['name'],
            "elevation": max_row['elev'],
            "lat/lon": max_row['ll'],
        },
        "min_elevation_station": {
            "name": min_row['name'],
            "elevation": min_row['elev'],
            "lat/lon": min_row['ll']
        }
    }
    return report


def output_to_file(report):
    output_file_name = f"elevation_report_{report['state']}.json"
    with open(output_file_name, "w") as f:
        json.dump(report, f, indent=4)
    print(f"Success. Output saved to {output_file_name}")


if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) == 2:
        data_file_name, state_code = args
        state_code = state_code.upper()
        if is_valid_state_code(state_code):
            df_all = load_data_from_file(data_file_name)
            if not df_all.empty:
                df_state = df_all[df_all.state == state_code]
                if df_state.size > 0:
                    elevation_report = generate_elevation_statistics_report(df_state)
                    output_to_file(elevation_report)
                else:
                    print("State code is valid, but no data exists for it in file.")
        else:
            print("State code is invalid. Please check and try again.")
    else:
        print("Args are <data file name> <state code>")

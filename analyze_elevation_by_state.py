import sys

import pandas as pd


def is_valid_state_code(code):
    return code in ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA",
                    "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM",
                    "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA",
                    "WV", "WI", "WY"]


def load_data_from_file(file_name):
    try:
        df = pd.read_csv(file_name)
        return df
    except FileNotFoundError:
        print("File name is invalid. Please check and try again.")


if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) == 2:
        data_file_name, state_code = args
        if is_valid_state_code(state_code):
            df_all = load_data_from_file(data_file_name)
        else:
            print("State code is invalid. Please check and try again")
    else:
        print("Args are <data file name> <state code>")

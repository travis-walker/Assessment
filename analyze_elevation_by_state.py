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


def calculate_statistics(df):
    print(df.tail())
    print(df.size)


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
                    calculate_statistics(df_state)
                else:
                    print("State code is valid, but no data exists for it in file.")
        else:
            print("State code is invalid. Please check and try again.")
    else:
        print("Args are <data file name> <state code>")

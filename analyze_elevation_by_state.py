import sys


def is_valid_state_code(code):
    return code in ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA",
                    "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM",
                    "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA",
                    "WV", "WI", "WY"]


if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) == 2:
        data_file_name, state_code = args
        print(data_file_name)
        print(state_code)
        print(is_valid_state_code(state_code))
    else:
        print("Args are <data file name> <state code>")

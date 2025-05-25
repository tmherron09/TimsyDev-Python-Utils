""" Csv File Service for CSV Comparison App """
import os
import csv
import argparse


""" Globals """
daily_folder_name = 'daily'
accepted_extensions = ['csv']
debug_mode = False

test_add_quotes_input_path = 'daily\\2-11\members_20240212.csv'
test_add_quotes_output_path = 'daily\\2-11\\test_add_quotes.csv'


def debug_print(*msg):
    if debug_mode:
        print(*msg)


class MissingDailyCsvFolderException(Exception):
    """Raise when the Hard Coded Daily CSV Folder is not found Locally."""

    def __init__(self):
        default_message = "Error: No 'daily' folder found. Please Create Local folder."
        super().__init__(default_message)


def check_for_daily_folder():
    local_folders_lambda = set(map(lambda x: x.lower(), os.listdir()))
    local_folders_lower = set([x.lower() for x in os.listdir()])

    if daily_folder_name in local_folders_lower:
        return True
    else:
        raise MissingDailyCsvFolderException()


def list_available_dates():
    """
    List available dates based on folders.
    """
    date_folders = set(os.listdir(daily_folder_name))
    folders_to_discard = []
    for folder in date_folders:
        contained_files = os.listdir(f'{daily_folder_name}/{folder}')
        debug_print(f'All Contained dates in Folder {folder}: ', contained_files)
        if any(file[-3:] not in accepted_extensions for file in contained_files):
            debug_print("There is a Non-Csv File. Removing from list.")
            for file in contained_files:
                if file[-3:] not in accepted_extensions:
                    contained_files.remove(file)
        if any(file[-3:] in accepted_extensions for file in contained_files[-3:]):
            debug_print(f'Available CSV Files in {folder}: ', contained_files)
        else:
            debug_print("No CSV Files.")
            folders_to_discard.append(folder)
    debug_print(f'Pre-Remove Date Folders: {date_folders}')
    [date_folders.discard(folder) for folder in folders_to_discard]
    debug_print(f'Post-Remove Date Folders: {date_folders}')
    if any(date_folders):
        return date_folders
    else:
        return None



def csv_add_quotes(input_file_path, output_file_path):
    """
    This helps add Quotes around an existing CSV file
    when there are no existing quotes.
    Good when mocked data comes from external source without quotes.
    Header will not be quoted.
    NULL or blanks will be quoted.
    """
    with open(input_file_path, newline='') as csvfile:
        # reader = csv.DictReader(csvfile)
        simple_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        with open(output_file_path, 'w+', newline='') as quoted_csv:
            quote_writer = csv.writer(quoted_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONE)
            for row in simple_reader:
                if simple_reader.line_num == 1:
                    quote_writer.writerow(row)
                    quote_writer = csv.writer(quoted_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
                    continue
                quote_writer.writerow(row)


def get_csv_data(input_file_path):
    csv_dict = []
    csv_columns = []
    with open(input_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        csv_columns = reader.fieldnames
        for row in reader:
            csv_dict.append(row)

    debug_print(f'Number of Items in CSV: {len(csv_dict)}')
    debug_print(f'First Item: {csv_dict[0]}')
    debug_print(f'Second Item: {csv_dict[1]}')
    debug_print(f'Third Item: {csv_dict[2]}')
    debug_print(f'Fourth Item: {csv_dict[3]}')
    debug_print(f'Fourth Item Reconciliation Status: {csv_dict[3]["USERNAME"]}')
    return csv_columns, csv_dict


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Csv Comparison App Csv File Service')
    parser.add_argument('-d', '--debug', action='store_true')
    debug_mode = parser.parse_args().debug
    debug_mode = True
    print(f'Debug Mode: {parser.parse_args().debug}')
    debug_print('Test For Local daily folder.')
    try:
        has_folder = check_for_daily_folder()
        debug_print("Daily Folder Present: ", has_folder)
        dates_available = list_available_dates()
        debug_print(f'Available dates: {dates_available}')
    except MissingDailyCsvFolderException as ex:
        raise
    get_csv_data(test_add_quotes_output_path)
    # csv_add_quotes(test_add_quotes_input_path, test_add_quotes_output_path)

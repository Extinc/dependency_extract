import yaml
import csv
from pathlib import Path
from datetime import datetime
# csv header
header = ['package', 'versions', 'project', 'project_version']
row =[]
date = datetime.today().strftime('%Y-%m-%d')
path = Path(__file__).parent / f'dependency-list-flutter-{date}.csv'

project = ''
project_version = ''

pubspec_path_input = input('Enter the full path to the pubspec yaml for flutter : ')


with open(pubspec_path_input, 'r') as yaml_file:
    print("Start reading yaml...")
    yaml_data = yaml.safe_load(yaml_file)
    count = 0

    for key in yaml_data:
 
        if key == 'name' and type(yaml_data[key]) == str:
            project = yaml_data[key]
        
        if key == 'version' and type(yaml_data[key]) == str:
            project_version = yaml_data[key]

        if key.endswith('dependencies') and type(yaml_data[key]) == dict:
            for sub_key in yaml_data[key]:
                if type(yaml_data[key][sub_key]) == str:
                    row.append({
                        'package': sub_key,
                        'versions': yaml_data[key][sub_key],
                        'project': project,
                        'project_version': project_version
                    })

    print("Finished reading yaml...")
    yaml_file.close()


with open(path, '+w', encoding='UTF8') as csv_file:
    print("Proceeding to writing the data to csv ...")

    writer = csv.DictWriter(csv_file, fieldnames=header)
    writer.writeheader()
    writer.writerows(row)

    print("CSV have been saved")

    csv_file.close()

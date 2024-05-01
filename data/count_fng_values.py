# This script reads the fng-all-data.csv file and counts the repetitions of each fng_value.
import csv

def count_fng_values(csv_file):
    fng_values_count = {}

    with open(csv_file, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            fng_value = row['fng_value']
            if fng_value in fng_values_count:
                fng_values_count[fng_value] += 1
            else:
                fng_values_count[fng_value] = 1

    return fng_values_count

def write_count_to_csv(count_dict, output_csv):
    with open(output_csv, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['fng_value', 'repeticiones'])
        for value, count in count_dict.items():
            writer.writerow([value, count])

input_csv = "C:\\Users\\Adonys\\My Drive\\0. HERMES\\Development_Labs\\fng-notifier\\data\\fng-all-data.csv"

output_csv = "fng_values_count.csv"

result = count_fng_values(input_csv)

write_count_to_csv(result, output_csv)

print("The CSV file with the repetitions count was created successful.")

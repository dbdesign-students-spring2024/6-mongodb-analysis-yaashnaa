import csv

def normalize_text(text):
    return text.lower()

def convert_percentage_to_decimal(percentage):
    if percentage.endswith('%'):
        return str(float(percentage.replace('%', '')) / 100)
    return percentage

def format_date(date_string):
   
    return date_string

def convert_to_boolean(text):

    if text == 't':
        return 'True'
    elif text == 'f':
        return 'False'
    return text

def validate_numeric(field):
    try:
        return str(float(field))
    except ValueError:
        return ''

def clean_field(field, header):

    if header in ['name', 'description', 'host_name', 'neighborhood_overview']:
        return normalize_text(field)
    elif header in ['host_response_rate', 'host_acceptance_rate']:
        return convert_percentage_to_decimal(field)
    elif header == 'host_is_superhost':
        return convert_to_boolean(field)
    elif header in ['latitude', 'longitude', 'price']:
        return validate_numeric(field)
    elif header in ['host_since', 'last_scraped']:
        return format_date(field)
    return field 

def clean_row(row, headers):
    return [clean_field(field, header) for field, header in zip(row, headers)]

def clean_csv(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as infile, \
         open(output_file_path, 'w', encoding='utf-8', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        headers = next(reader)  
        writer.writerow(headers)  
        
        for row in reader:
            cleaned_row = clean_row(row, headers)
            writer.writerow(cleaned_row)

input_file_path = 'data/listings.csv'
output_file_path = 'data/listing_clean.csv'

clean_csv(input_file_path, output_file_path)

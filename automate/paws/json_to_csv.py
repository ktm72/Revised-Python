import json
import csv

# Step 1: Read the JSON file
json_file_path = 'category_mapping.json'  # Replace with your JSON file path
csv_file_path = 'leftover_collection_title.csv'   # Replace with desired CSV output path

with open(json_file_path, 'r', encoding='utf-8') as json_file:
  data = json.load(json_file)

total_obj = len(data)
print(f"Loaded {total_obj} items from JSON file.")

# Step 2: Filter objects that have a 'title' key
filtered_data = [obj for obj in data if 'title' in obj]
title_count = len(filtered_data)
print(f"Filtered down to {title_count} items with 'title' key.")
print(f"Category mapped: {total_obj - title_count}")

# Step 3: Write to CSV with specified column mapping
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
  writer = csv.DictWriter(csv_file, fieldnames=['Shopify Id', 'Title'])
  writer.writeheader()
  
  for obj in filtered_data:
    writer.writerow({
      'Shopify Id': obj.get('id', ''),  # Uses empty string if 'id' is missing
      'Title': obj['title']             # We already filtered for 'title'
    })

print(f"Successfully wrote {len(filtered_data)} items to {csv_file_path}")
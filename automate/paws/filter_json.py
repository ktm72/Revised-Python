import json

# Step 1: Read the JSON file
json_file_path = 'category_mapping.json'  # Replace with your file path
output_file_path = 'output.json'  # Output path

with open(json_file_path, 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Step 2: Process the data
filtered_objects = []

for obj in data:
    if 'title' in obj:  # Filter out objects with 'title'
      continue
        
    # Create a copy without 'id'
    filtered_obj = {k: v for k, v in obj.items() if k != 'id'}
    filtered_objects.append(filtered_obj)

# Step 3: Merge into a single object
merged_object = {}
for obj in filtered_objects:
    merged_object.update(obj)  # Merge all key-value pairs

# Step 4: Save the result
with open(output_file_path, 'w', encoding='utf-8') as out_file:
    json.dump(merged_object, out_file, indent=2)

print(f"Filtered and merged data saved to {output_file_path}")
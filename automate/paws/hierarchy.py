import pandas as pd

def build_hierarchy(df):
  hierarchy = []
  level_paths = {0: ""}  # Tracks paths for each level (0 = top)
  
  for index, row in df.iterrows():
    category = row['Category'].strip()
    
    if '-->' not in category:
      # Top-level category (level 0)
      level_paths[0] = category
      # Clear deeper levels (since a new top-level resets hierarchy)
      for lvl in range(1, 10): # assuming max depth of 10
        level_paths.pop(lvl, None)
      hierarchy.append(category)
    else:
      # Split into prefix (dashes) and subcategory
      prefix, subcategory = category.split('-->', 1)
      subcategory = subcategory.strip()
      
      # Level = number of '--' before '-->' + 1
      level = prefix.count('--') + 1  # '-->' = level 1, '-- -->' = level 2, etc.
      
      # Parent is at (level - 1)
      parent_level = level - 1
      if parent_level not in level_paths:
        # Fallback: use the closest existing parent (if data is malformed)
        parent_level = max(lvl for lvl in level_paths if lvl < level)
      
      # Build the new path
      parent_path = level_paths[parent_level]
      new_path = f"{parent_path} - {subcategory}" if parent_path else subcategory
      
      # Update current level and clear deeper levels
      level_paths[level] = new_path
      for lvl in range(level + 1, 10):  # Clear deeper levels
        level_paths.pop(lvl, None)
      
      hierarchy.append(new_path)
  
  df['Hierarchy'] = hierarchy
  return df

#  To process CSV:
df = pd.read_csv('input.csv')
result = build_hierarchy(df)
result.to_csv('output.csv', index=False)
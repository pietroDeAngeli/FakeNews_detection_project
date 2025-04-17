import pandas as pd

# Load test
df = pd.read_csv('test.csv', names=['id', 'title', 'text', 'category', 'date', 'label'])

# Fill any missing values in title and text
df['title'] = df['title'].fillna('')
df['text'] = df['text'].fillna('')

# Just join title and text with a space
df['text'] = df['title'] + ' ' + df['text']

# Drop title column
df.drop(columns=['title'], inplace=True)

# Reorder columns
df = df[['id', 'text', 'category', 'date', 'label']]

# Save to new CSV
df.to_csv('test_joined.csv', index=False, header=False)


#************************************************
# Load train
df = pd.read_csv('train.csv', names=['id', 'title', 'text', 'category', 'date', 'label'])

# Fill any missing values in title and text
df['title'] = df['title'].fillna('')
df['text'] = df['text'].fillna('')

# Just join title and text with a space
df['text'] = df['title'] + ' ' + df['text']

# Drop title column
df.drop(columns=['title'], inplace=True)

# Reorder columns
df = df[['id', 'text', 'category', 'date', 'label']]

# Save to new CSV
df.to_csv('train_joined.csv', index=False, header=False)

#***********************************************
# Load validation
df = pd.read_csv('validation.csv', names=['id', 'title', 'text', 'category', 'date', 'label'])

# Fill any missing values in title and text
df['title'] = df['title'].fillna('')
df['text'] = df['text'].fillna('')

# Just join title and text with a space
df['text'] = df['title'] + ' ' + df['text']

# Drop title column
df.drop(columns=['title'], inplace=True)

# Reorder columns
df = df[['id', 'text', 'category', 'date', 'label']]

# Save to new CSV
df.to_csv('validation_joined.csv', index=False, header=False)


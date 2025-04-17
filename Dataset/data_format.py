import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')

def preprocess(text):
    text = text.lower()
    # Replace punctuation with space (preserve word boundaries)
    text = re.sub(r'[^\w\s]', ' ', text)
    # Replace multiple spaces with single space
    text = re.sub(r'\s+', ' ', text)
    words = word_tokenize(text)
    words = [word for word in words if word not in stop_words]
    return ' '.join(words)


#************************************************************
# Load TEST (no header row)
df = pd.read_csv('test.csv', names=['id', 'title', 'text', 'category', 'date', 'label'])

# Fill any missing values in title and text
df['title'] = df['title'].fillna('')
df['text'] = df['text'].fillna('')

# Define stopwords
stop_words = set(stopwords.words('english'))

# Combine and clean title + text
df['text'] = (df['title'] + ' ' + df['text']).apply(preprocess)

# Drop the title column
df.drop(columns=['title'], inplace=True)

# Reorder columns to match format: [id, text, category, date, label]
df = df[['id', 'text', 'category', 'date', 'label']]

# Save to new CSV (no header, no index)
df.to_csv('test_cleaned.csv', index=False, header=False)

#************************************************************
# Load TRAIN (no header row)
df = pd.read_csv('train.csv', names=['id', 'title', 'text', 'category', 'date', 'label'])

# Fill any missing values in title and text
df['title'] = df['title'].fillna('')
df['text'] = df['text'].fillna('')

# Define stopwords
stop_words = set(stopwords.words('english'))

# Combine and clean title + text
df['text'] = (df['title'] + ' ' + df['text']).apply(preprocess)

# Drop the title column
df.drop(columns=['title'], inplace=True)

# Reorder columns to match format: [id, text, category, date, label]
df = df[['id', 'text', 'category', 'date', 'label']]

# Save to new CSV (no header, no index)
df.to_csv('train_cleaned.csv', index=False, header=False)

#************************************************************
# Load VALIDATION (no header row)
df = pd.read_csv('validation.csv', names=['id', 'title', 'text', 'category', 'date', 'label'])

# Fill any missing values in title and text
df['title'] = df['title'].fillna('')
df['text'] = df['text'].fillna('')

# Define stopwords
stop_words = set(stopwords.words('english'))

# Combine and clean title + text
df['text'] = (df['title'] + ' ' + df['text']).apply(preprocess)

# Drop the title column
df.drop(columns=['title'], inplace=True)

# Reorder columns to match format: [id, text, category, date, label]
df = df[['id', 'text', 'category', 'date', 'label']]

# Save to new CSV (no header, no index)
df.to_csv('validation_cleaned.csv', index=False, header=False)
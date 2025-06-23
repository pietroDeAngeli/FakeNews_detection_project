import pandas as pd
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

# Download stopwords and tokenizer if not already done
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')

# Load your CSV
df = pd.read_csv("RAW_Dataset/validation.csv")

# Define stopwords and punctuation
stop_words = set(stopwords.words('english'))
punct_table = str.maketrans('', '', string.punctuation)

# Function to clean text
def clean_text(text):
    if not isinstance(text, str):
        return text
    text = text.lower()  # Lowercase
    text = text.translate(punct_table)  # Remove punctuation
    words = word_tokenize(text)
    words = [word for word in words if word not in stop_words]  # Remove stopwords
    return ' '.join(words)

# Apply to the first 3 columns
for col in df.columns[:3]:
    df[col] = df[col].apply(clean_text)

# Save cleaned CSV
df.to_csv("Dataset/validation.csv", index=False)

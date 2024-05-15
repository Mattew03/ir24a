import os

# Define the path to the directory containing the text files
CORPUS_DIR = 'D:\U\7. Septimo\Rec. Info\ir24a\week01\data'
documents = {}
for filename in os.listdir(CORPUS_DIR):
    if filename.endswith('.txt'):
        file_path = os.path.join(CORPUS_DIR, filename)
        with open(file_path, 'r', encoding='utf-8') as file:
            documents[filename] = file.read().lower()  # Read and convert to lowercase

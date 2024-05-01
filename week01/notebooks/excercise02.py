import os
import re
from collections import defaultdict
from tqdm import tqdm

# Directorio donde están los documentos
directory = r'D:\U\7. Septimo\Rec. Info\ir24a\week01\data'

# Crear un índice invertido para almacenar la ubicación de las palabras en los documentos
inverted_index = defaultdict(set)

# Recopilar todos los documentos del directorio
document_files = [f for f in os.listdir(directory) if f.endswith(".txt")]

# Leer cada documento y construir el índice invertido
for doc_file in tqdm(document_files, desc="Cargando documentos"):
    doc_path = os.path.join(directory, doc_file)
    with open(doc_path, 'r', encoding='utf-8') as file:
        content = file.read().lower()  # Normalizar a minúsculas
        
        # Extraer palabras, ignorando puntuaciones
        words = re.findall(r'\b\w+\b', content)
        
        # Agregar cada palabra al índice invertido con el documento correspondiente
        for word in words:
            inverted_index[word].add(doc_file)  # Usamos un set para evitar duplicados

# Encontrar palabras que aparecen en más de un documento
repeated_words = {word: list(docs) for word, docs in inverted_index.items() if len(docs) > 1}

# Mostrar las palabras y los documentos donde se repiten
if repeated_words:
    print("Palabras que se repiten en más de un documento:")
    for word, docs in repeated_words.items():
        print(f"- '{word}' aparece en los documentos: {', '.join(docs)}")
else:
    print("No hay palabras que se repitan en más de un documento.")

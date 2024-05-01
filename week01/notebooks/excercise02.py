import os
import re
import nltk
from collections import defaultdict
from tqdm import tqdm
from typing import Set, List

# Descargar datos de tokenización de NLTK (si es necesario)
nltk.download("punkt")

# Directorio donde están los documentos
directory = r'D:\U\7. Septimo\Rec. Info\ir24a\week01\data'

# Crear un índice invertido para almacenar la ubicación de las palabras en los documentos
inverted_index = defaultdict(set)

# Cargar documentos y construir el índice invertido
document_files = [f for f in os.listdir(directory) if f.endswith(".txt")]

# Leer y tokenizar cada documento para crear el índice invertido
for doc_file in tqdm(document_files, desc="Cargando documentos"):
    doc_path = os.path.join(directory, doc_file)
    with open(doc_path, 'r', encoding='utf-8') as file:
        content = file.read().lower()  # Normalizar a minúsculas
        
        # Extraer palabras con tokenización de NLTK
        words = nltk.word_tokenize(content)
        
        # Agregar cada palabra al índice invertido con el documento correspondiente
        unique_words = set(words)
        for word in unique_words:
            inverted_index[word].add(doc_file)  # Usamos un set para evitar duplicados

# Función para procesar consultas booleanas
def parse_boolean_query(query: str) -> List[str]:
    """
    Divide una consulta booleana en sus partes constituyentes: términos y operadores.
    """
    tokens = query.split()
    terms = []
    operators = []

    for token in tokens:
        if token.upper() in {"AND", "OR", "NOT"}:
            operators.append(token.upper())
        else:
            terms.append(token.lower())

    return terms, operators

# Función para ejecutar una consulta booleana
def execute_boolean_query(terms: List[str], operators: List[str]) -> Set[str]:
    """
    Ejecuta una consulta booleana utilizando el índice invertido.
    """
    if not terms:
        return set()  # No hay términos para buscar

    # Conjuntos de resultados para cada término
    term_results = [inverted_index.get(term, set()) for term in terms]

    # Resultado inicial para la consulta
    if "NOT" in operators:
        not_index = operators.index("NOT")
        not_set = term_results.pop(not_index)
        operators.pop(not_index)

    # Comenzar con el primer conjunto de resultados
    result_set = term_results[0]

    # Aplicar operadores
    for i, operator in enumerate(operators):
        if operator == "AND":
            result_set = result_set.intersection(term_results[i + 1])
        elif operator == "OR":
            result_set = result_set.union(term_results[i + 1])

    if "NOT" in operators:
        result_set = result_set.difference(not_set)

    return result_set

# Consulta del usuario
query = input("Ingrese la consulta booleana (AND, OR, NOT): ")

# Analizar la consulta y ejecutar la búsqueda
terms, operators = parse_boolean_query(query)
results = execute_boolean_query(terms, operators)

# Mostrar los resultados
if results:
    print("Documentos que coinciden con la consulta:")
    for doc in results:
        print(f"- {doc}")
else:
    print("No se encontraron documentos que coincidan con la consulta.")

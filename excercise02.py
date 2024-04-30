import os
from collections import defaultdict

# Paso 1: Crear un Índice Invertido
def create_inverted_index(documents):
    inverted_index = defaultdict(set)
    for doc_id, (filename, content) in enumerate(documents):
        words = content.lower().split()  # Dividir contenido en palabras
        for word in set(words):  # Usar set para evitar duplicados
            inverted_index[word].add(doc_id)  # Asociar palabra con el documento
    return inverted_index

# Paso 2: Procesar la Consulta
def parse_query(query):
    # Separar la consulta en términos y operadores
    tokens = query.split()
    return tokens

# Paso 3: Buscar Documentos Basados en la Consulta
def search_documents(inverted_index, query_tokens):
    # Para procesar la consulta con operadores booleanos
    if 'AND' in query_tokens:
        terms = query_tokens[:query_tokens.index('AND')]
        and_terms = query_tokens[query_tokens.index('AND') + 1:]
        
        # Intersección para 'AND'
        results = inverted_index[terms[0]].intersection(*[inverted_index[term] for term in and_terms])
    
    elif 'OR' in query_tokens:
        terms = query_tokens[:query_tokens.index('OR')]
        or_terms = query_tokens[query_tokens.index('OR') + 1:]
        
        # Unión para 'OR'
        results = inverted_index[terms[0]].union(*[inverted_index[term] for term in or_terms])
    
    elif 'NOT' in query_tokens:
        term = query_tokens[query_tokens.index('NOT') + 1]
        
        # Complemento para 'NOT'
        all_docs = set(range(len(inverted_index)))
        results = all_docs.difference(inverted_index[term])
    
    else:
        # Buscar documentos con el término sin operadores booleanos
        term = query_tokens[0]
        results = inverted_index[term]

    return results

# Paso 4: Mostrar Resultados
def display_results(documents, results):
    if results:
        print("Documentos que coinciden con la consulta:")
        for doc_id in results:
            print(f"- {documents[doc_id][0]}")
    else:
        print("No se encontraron documentos que coincidan con la consulta.")

# Ejecutar el Algoritmo
def main():
    directory = r'D:\U\7. Septimo Semestre\Rec. Info\ir24a\week01\data'
    documents = load_documents(directory)  # Cargar documentos
    
    inverted_index = create_inverted_index(documents)  # Crear índice invertido
    
    query = input("Ingrese la consulta con operadores booleanos (AND, OR, NOT): ")
    query_tokens = parse_query(query)  # Analizar la consulta
    
    results = search_documents(inverted_index, query_tokens)  # Buscar documentos según la consulta
    
    display_results(documents, results)  # Mostrar resultados

# Ejecutar el script principal
if __name__ == '__main__':
    main()

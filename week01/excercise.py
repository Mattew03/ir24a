import os

def load_documents(directory):
    # Cargar documentos .txt desde la carpeta especificada
    documents = []
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            path = os.path.join(directory, filename)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()  # Leer todo el contenido del archivo
                documents.append((filename, content))  # Agregar a la lista
    return documents


def search_in_documents(documents, term):
    # Buscar la palabra clave (term) en todos los documentos
    results = []
    for name, content in documents:
        if term.lower() in content.lower():  # Convertir a minúsculas para búsqueda insensible a mayúsculas
            results.append(name)  # Agregar el nombre del archivo a los resultados
    return results


def main():
    # Directorio donde están tus archivos de texto
    directory = r'D:\U\7. Septimo Semestre\Rec. Info\ir24a\week01\data'
    
    # Cargar documentos
    documents = load_documents(directory)

    # Mostrar cuántos documentos se cargaron
    print("Se cargaron {} documentos.".format(len(documents)))

    # Pedir al usuario que ingrese la palabra a buscar
    search_term = input("Ingrese la palabra que desea buscar: ")

    # Buscar la palabra en los documentos
    search_results = search_in_documents(documents, search_term)

    # Mostrar resultados de la búsqueda
    if search_results:
        print("La palabra '{}' se encontró en los siguientes documentos:".format(search_term))
        for result in search_results:
            print("- {}".format(result))
    else:
        print("La palabra '{}' no se encontró en ningún documento.".format(search_term))


# Ejecutar el script
if __name__ == '__main__':
    main()

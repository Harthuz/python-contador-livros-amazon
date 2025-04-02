def count_books(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    # Contando as linhas que representam títulos de livros
    book_count = sum(1 for line in lines if line.strip() and not line.startswith(('Título', 'Comentários', 'Preço', 'Quantidade', 'Possui')))
    
    return book_count // 2  # Cada livro parece ter duas linhas de informação

# Exemplo de uso
file_path = "livros.txt"  # Substitua pelo caminho real do seu arquivo
print("Número de livros:", count_books(file_path))
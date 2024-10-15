# Sites para consulta de preço e quantidade: https://hortifruti.com.br/catalogsearch/result/?q=Laranja
produtos = {
    'frutas': {
        'Laranja Seleta': {'preco': 2.97, 'peso': '270g'},
        'Laranja Pera': {'preco': 2.12, 'peso': '250g'},
        'Laranja Lima': {'preco': 2.64, 'peso': '220g'},
        'Limão Tahiti': {'preco': 10.99, 'peso': '500g'},
        'Limão Siciliano': {'preco': 2.20, 'peso': '150g'},
        'Melão': {'preco': 5.00, 'peso': '1un'},
        'Banana Prata': {'preco': 2.60, 'peso': '200g'},
        'Banana Nanica': {'preco': 1.24, 'peso': '155g'},
        'Manga Tommy': {'preco': 5.50, 'peso': '500g'},
        'Manga Palmer': {'preco': 6.50, 'peso': '500g'},
        'Manga Espada': {'preco': 3.70, 'peso': '185g'},
        'Uva Verde': {'preco': 15.99, 'peso': '500g'},
        'Uva Preta': {'preco': 12.99, 'peso': '500g'},
        'Uva Vermelha': {'preco': 12.99, 'peso': '500g'},
        'Abacaxi': {'preco': 4.00, 'peso': '1un'},
        'Morango': {'preco': 5.50, 'peso': '500g'},
    },
    'verduras': {
        'Abóbora': {'preco': 3.00, 'peso': '1kg'},
        'Abóbora Itália': {'preco': 3.20, 'peso': '1kg'},
        'Abóbora Japonesa': {'preco': 3.50, 'peso': '1kg'},
        'Batata doce': {'preco': 2.50, 'peso': '1kg'},
        'Batata Baroa': {'preco': 3.00, 'peso': '1kg'},
        'Batata Inglesa': {'preco': 2.20, 'peso': '1kg'},
        'Beringela': {'preco': 4.50, 'peso': '300g'},
        'Beterraba': {'preco': 1.47, 'peso': '210g'},
        'Cebola': {'preco': 1.00, 'peso': '250g'},
        'Cebola Roxa': {'preco': 2.10, 'peso': '140g'},
        'Cenoura': {'preco': 1.12, 'peso': '160g'},
        'Chuchu': {'preco': 11.99, 'peso': '500g'},
        'Mandioca Embalada': {'preco': 7.79, 'peso': '400g'}, #Verificar este produto com o Scrum Master
        'Pepino': {'preco': 1.75, 'peso': '250g'},
        'Pepino Japonês': {'preco': 4.80, 'peso': '300g'},
        'Pimentão Amarelo': {'preco': 3.00, 'peso': '100g'},
        'Pimentão Verde': {'preco': 5.00, 'peso': '200g'},
        'Pimentão Vermelho': {'preco': 4.99, 'peso': '200g'},
        'Tomate Carmem': {'preco': 1.40, 'peso': '200g'},
        'Tomate Italiano' : {'preco': 0.98, 'peso': '115g'}
    },
    'folhagens': {
        'Alface Americana': {'preco': 4.79, 'peso': '1un'},
        'Alface Crespa': {'preco': 3.99, 'peso': '1un'},
        'Alface Roxa': {'preco': 8.29, 'peso': '1un'},
        'Alho Nacional': {'preco': 2.40, 'peso': '60g'},
        'Alho Poró': {'preco': 4.95, 'peso': '150g'},
        'Agrião': {'preco': 4.99, 'peso': '1un'},
        'Alecrim': {'preco': 4.99 , 'peso': '1un'},
        'Brócolis Comum': {'preco': 12.99, 'peso': '1un'},
        'Brócolis Japonês': {'preco': 14.99, 'peso': '1un'},
        'Cebolinha': {'preco': 6.99, 'peso': '1un'},
        'Coentro': {'preco': 5.99, 'peso': '1un'},
        'Couve Manteiga': {'preco': 9.99, 'peso': '1un'},
        'Espinafre': {'preco': 8.99, 'peso': '1un'},
        'Milho Verde': {'preco': 10.99, 'peso': '500g'},
        'Rabanete': {'preco': 0.60, 'peso': '60g'},
        'Rúcula': {'preco': 13.99, 'peso': '500g'}
    }
}


def get_produtos(categoria=None):
    if categoria:
        return produtos.get(categoria, {})
    return produtos    
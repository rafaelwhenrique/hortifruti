# Sites para consulta de preço e quantidade: https://hortifruti.com.br/catalogsearch/result/?q=Laranja
produtos = {
    'frutas': {
        'Laranja Seleta': {'preco': 2.97, 'quantidade': '270g'},
        'Laranja Pera': {'preco': 2.12, 'quantidade': '250g'},
        'Laranja Lima': {'preco': 2.64, 'quantidade': '220g'},
        'Limão Tahiti': {'preco': 10.99, 'quantidade': '500g'},
        'Limão Siciliano': {'preco': 2.20, 'quantidade': '150g'},
        'Melão': {'preco': 5.00, 'quantidade': '1un'},
        'Banana Prata': {'preco': 2.60, 'quantidade': '200g'},
        'Banana Nanica': {'preco': 1.24, 'quantidade': '155g'},
        'Manga Tommy': {'preco': 5.50, 'quantidade': '500g'},
        'Manga Palmer': {'preco': 6.50, 'quantidade': '500g'},
        'Manga Espada': {'preco': 3.70, 'quantidade': '185g'},
        'Uva Verde': {'preco': 15.99, 'quantidade': '500g'},
        'Uva Preta': {'preco': 12.99, 'quantidade': '500g'},
        'Uva Vermelha': {'preco': 12.99, 'quantidade': '500g'},
        'Abacaxi': {'preco': 4.00, 'quantidade': '1un'},
        'Morango': {'preco': 5.50, 'quantidade': '500g'},
    },
    'verduras': {
        'Abóbora': {'preco': 3.00, 'quantidade': '1kg'},
        'Abóbora Itália': {'preco': 3.20, 'quantidade': '1kg'},
        'Abóbora Japonesa': {'preco': 3.50, 'quantidade': '1kg'},
        'Batata doce': {'preco': 2.50, 'quantidade': '1kg'},
        'Batata Baroa': {'preco': 3.00, 'quantidade': '1kg'},
        'Batata Inglesa': {'preco': 2.20, 'quantidade': '1kg'},
        'Beringela': {'preco': 4.50, 'quantidade': '300g'},
        'Beterraba': {'preco': 1.47, 'quantidade': '210g'},
        'Cebola': {'preco': 1.00, 'quantidade': '250g'},
        'Cebola Roxa': {'preco': 2.10, 'quantidade': '140g'},
        'Cenoura': {'preco': 1.12, 'quantidade': '160g'},
        'Chuchu': {'preco': 11.99, 'quantidade': '500g'},
        'Mandioca Embalada': {'preco': 7.79, 'quantidade': '400g'}, #Verificar este produto com o Scrum Master
        'Pepino': {'preco': 1.75, 'quantidade': '250g'},
        'Pepino Japonês': {'preco': 4.80, 'quantidade': '300g'},
        'Pimentão Amarelo': {'preco': 3.00, 'quantidade': '100g'},
        'Pimentão Verde': {'preco': 5.00, 'quantidade': '200g'},
        'Pimentão Vermelho': {'preco': 4.99, 'quantidade': '200g'},
        'Tomate Carmem': {'preco': 1.40, 'quantidade': '200g'},
        'Tomate Italiano' : {'preco': 0.98, 'quantidade': '115g'}
    },
    'folhagens': {
        'Alface Americana': {'preco': 4.79, 'quantidade': '1un'},
        'Alface Crespa': {'preco': 3.99, 'quantidade': '1un'},
        'Alface Roxa': {'preco': 8.29, 'quantidade': '1un'},
        'Alho Nacional': {'preco': 2.40, 'quantidade': '60g'},
        'Alho Poró': {'preco': 4.95, 'quantidade': '150g'},
        'Agrião': {'preco': 4.99, 'quantidade': '1un'},
        'Alecrim': {'preco': 4.99 , 'quantidade': '1un'},
        'Brócolis Comum': {'preco': 12.99, 'quantidade': '1un'},
        'Brócolis Japonês': {'preco': 14.99, 'quantidade': '1un'},
        'Cebolinha': {'preco': 6.99, 'quantidade': '1un'},
        'Coentro': {'preco': 5.99, 'quantidade': '1un'},
        'Couve Manteiga': {'preco': 9.99, 'quantidade': '1un'},
        'Espinafre': {'preco': 8.99, 'quantidade': '1un'},
        'Milho Verde': {'preco': 10.99, 'quantidade': '500g'},
        'Rabanete': {'preco': 0.60, 'quantidade': '60g'},
        'Rúcula': {'preco': 13.99, 'quantidade': '500g'}
    }
}


def get_produtos(categoria=None):
    if categoria:
        return produtos.get(categoria, {})
    return produtos    
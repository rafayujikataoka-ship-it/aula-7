estoque= {
    1: ['nome:','notebook', 'preço: 5000', 'quantidade: 10'],
    2: ['nome:','mouse', 'preço: 200', 'quantidade: 50'],
    3: ['nome:','teclado', 'preço: 300', 'quantidade: 30']
}

cod = 1
quant = 10
if cod in estoque:
    estoque[cod][1] += quant 

for cod,produto in estoque.items():
    print(f'{cod} - {produto['nome']} - {produto['qtd']}')

    

Funcionalidade: Adicionar novo endereço

    @Endereco_test
    Cenário: Adicionar um novo endereço com sucesso
        Dado que o usuário esteja logado
        Quando clicar no menu de usuário
        E clicar em "My Account"
        E clicar em "Address Book"
        E clicar em "Adicionar novo endereço"
        E preencher os dados obrigatórios
        E clicar em "Salvar endereço"
        Então aparecer a mensagem "Você salvou o endereço."
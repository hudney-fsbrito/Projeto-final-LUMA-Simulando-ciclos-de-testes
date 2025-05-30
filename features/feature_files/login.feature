Funcionalidade: Login

    @Smoke
    Cenário: Cadastrar uma conta com login e senha
        Dado que a página de LUMA seja acessada e clicado em Create an Account
        Quando o formulário Create New Customer Account for preechido
        Então a conta deve ser criada com sucesso

    @Smoke @Login
    Cenário: Efetuar login com email e senha cadastrados
        Dado que o usuário tenha cadastro
        Quando os dados de login forem preechidos
        Então o nome do usuário deve aparecer no topo da tela

   
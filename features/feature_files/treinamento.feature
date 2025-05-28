Funcionalidade: Treinamento Automação

    @Smoke
    Cenário: Verificar se o botão click-me muda o texto quando clicado
        Dado que a página de treinamento seja acessada
        Quando o botão click me for pressionado
        Então o seu valor deverá mudar para "Obrigado!!"

    @Smoke @test
    Cenário: Inserir o um valor no campo nome
        Dado que a página de treinamento seja acessada
        Quando o valor "David" for inserido no campo nome
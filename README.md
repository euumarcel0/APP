# APP

## Objetivos

Rodar a APP para:
- Converter PDF para português
- Converter PDF traduzido para Excel
- Converter Excel para Forms

## Tarefa 1: Converter PDF para português

1. No Explorador de Arquivos, abra `Documentos`.
2. Clique com o botão direito do mouse, selecione `Mostrar mais opções` e escolha `Open Git Bash here`.
3. Com o terminal do Git aberto, digite o seguinte comando e pressione `Enter`:

    ```sh
    git clone https://github.com/euumarcel0/APP.git
    ```



4. Será criada uma pasta chamada `APP`. Acesse essa pasta.
5. Clique com o botão direito em qualquer lugar vazio da pasta, selecione `Mostrar mais opções` e clique em `Abrir com o Code`.
6. Abra o arquivo `apiPDF.py`.

    - Na linha 48, você pode definir o nome que deseja para o PDF de saída.


7. Abra o terminal.
8. Rode o programa com o comando:

    ```sh
    python.exe .\apiPDF.py
    ```

9. Quando abrir a tela de tradução, defina o caminho do PDF desejado juntamente com o nome.

## Tarefa 2: Converter PDF traduzido para Excel

1. Assim que abrir o VSCode na pasta, abra o arquivo `appExcel.py`.
2. Altere as linhas 63 e 64:

    - Linha 63: Define o arquivo que será convertido.
    - Linha 64: Define o nome do arquivo Excel de saída.

3. No terminal, rode o programa com o comando:

    ```sh
    python.exe .\appExcel.py
    ```

4. O app vai salvar o arquivo Excel na pasta atual.

## Tarefa 3: Converter Excel para Forms

1. Abra o link no navegador: [Google Cloud Console](https://console.cloud.google.com/welcome?hl=en-au&project=subtle-torus-421513).
2. Crie um novo projeto:
    - Clique em `Novo projeto`.
    - Defina o nome do seu projeto.
    - Aguarde a notificação.

3. Após a notificação, clique em `Select a Project` e selecione o projeto criado.
4. Clique no menu de navegação no canto superior esquerdo, sobreponha o nome `API e serviços` e clique em `Biblioteca`.
5. Procure por `Google Forms API` e clique nele.
6. Clique em `Enable`.
7. Clique novamente no menu de navegação, sobreponha o nome `API e serviços` e clique em `Credenciais`.
8. Clique em `Criar credenciais`.
9. Selecione `ID do cliente OAuth`.
10. Clique em `Configurar Tela de Consentimento`.
11. Selecione `Externo` e clique em `Criar`.
12. Nomeie o APP e defina o e-mail de suporte.
13. Defina o e-mail e clique em `Salvar e Continuar`.
14. Na página seguinte, clique em `Salvar e Continuar`.
15. Clique novamente no menu de navegação, sobreponha o nome `API e serviços` e clique em `Credenciais`.
16. Clique em `Criar credenciais`.
17. Selecione `ID do cliente OAuth`.
18. Defina como `Aplicativo Desktop`.
19. Deixe o resto padrão e clique em `Criar`. Após isso, vai abrir a tela de credenciais.
20. Clique em `Baixar JSON` e em `OK`.
21. Volte ao menu de navegação, sobreponha o nome `API e serviços` e clique em `Tela de consentimento do OAuth`.
22. Clique em `Publicar Aplicativo` e confirme.
23. Abra o Explorador de Arquivos e mova o JSON para a mesma pasta onde o código está salvo.
24. Abra o VSCode nessa pasta.
25. Na linha 10 do código `appForms.py`, altere o nome do JSON para o nome do seu arquivo JSON.

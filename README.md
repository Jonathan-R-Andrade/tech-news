# Tech News

Projeto desenvolvido por [Jonathan R. Andrade](https://www.linkedin.com/in/jonathan-r-andrade/) na [Trybe](https://www.betrybe.com/).

## Sobre

Projeto de uma ferramenta escrita em Python capaz de coletar noticias sobre tecnologia. As notícias são obtidas por meio de raspagem do [blog da Trybe](https://blog.betrybe.com/) e são salvas no banco de dados MongoDB para serem consultadas posteriormente.

## Habilidades desenvolvidas

* Utilizar o terminal interativo do Python;
* Escrever meus próprios módulos e importá-los em outros códigos;
* Aplicar técnicas de raspagem de dados;
* Extrair dados de conteúdo HTML;
* Armazenar os dados obtidos no banco de dados MongoDB.

## Como executar

Siga os passos abaixo executando os comandos no terminal.

1. Clone o repositório.

    * Exemplo com Git + HTTPS
      ```bash
      git clone https://github.com/Jonathan-R-Andrade/tech-news.git
      ```
    * Exemplo com Git + SSH
      ```bash
      git clone git@github.com:Jonathan-R-Andrade/tech-news.git
      ```
    * Usando GitHub CLI
      ```bash
      gh repo clone Jonathan-R-Andrade/tech-news
      ```

    > Entre na pasta do repositório clonado.

2. Crie um arquivo `.env` na raiz do projeto com as variáveis de ambiente necessárias para o banco de dados.
    * No Windows, execute o comando abaixo no terminal.
      ```bash
      copy .env.example .env
      ```
    * No Unix/Linux, execute o comando abaixo no terminal.
      ```bash
      cp .env.example .env
      ```

3. Prepare o ambiente usando Docker Compose ou o Python e o MongoDB instalados localmente.

   * <details>
       <summary>Usando Docker Compose.</summary>

       > Para rodar esse projeto usando Docker Compose eu utilizei o Docker na versão 23.0.1 e o Docker Compose na versão 2.16.0.

       1. Inicie a aplicação.
       ```bash
       docker compose up -d --build
       ```

       2. Entre no container da aplicação.
       ```bash
       docker exec -it tech_news bash
       ```
     </details>

   * <details>
       <summary>Usando Python e MongoDB instalados localmente.</summary>

       > Para rodar esse projeto localmente eu utilizei o Python na versão 3.8.16 e o MongoDB na versão 5.0.14.

       3. Crie o ambiente virtual.
       ```bash
       python3 -m venv .venv
       ```

       4. Ative o ambiente virtual.
       ```bash
       source .venv/bin/activate
       ```

       5. Instale as dependências.
       ```bash
       python3 -m pip install -r dev-requirements.txt
       ```

       > Verifique se o MongoDB está rodando e as variáveis de ambiente estão corretas no arquivo `.env`.
     </details>

4. Execute o script.
  ```bash
  tech-news-analyzer
  ```

---

Além do que foi solicitado no projeto, eu adicionei a possibilidade de executar o script com os seguintes argumentos:

* `--option` ou `-o`: Executa o script com a opção desejada sem exibir o menu.
  ```bash
  tech-news-analyzer --option 5
  ```

* `--width` ou `-w`: Define a largura máxima das colunas da tabela (padrão: 100).
  ```bash
  tech-news-analyzer --width 50
  ```

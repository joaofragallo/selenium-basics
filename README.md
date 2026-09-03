# Scripts de Automação Web com Selenium e Python

Este repositório contém pequenos projetos e scripts criados para estudo de automação web, web scraping e integração de dados usando Python e Selenium. O navegador alvo utilizado nestes testes foi o Mozilla Firefox.

## Tecnologias Utilizadas

* **Python 3**
* **Selenium WebDriver** (Automação de navegador)
* **Pandas & Openpyxl** (Manipulação e leitura de planilhas Excel)
* **Mozilla Firefox** (Navegador utilizado)

##  O que tem neste repositório?

1. **Navegação Básica e Elementos:** 
   * Acesso a páginas da web.
   * Localização de elementos por `ID`, `NAME`, `LINK_TEXT` e `XPATH`.
   * Simulação de cliques e digitação em campos de texto (`send_keys`).

2. **Manipulação Avançada de Navegador:**
   * Alternância entre abas (`window_handles`).
   * Simulação de teclas do teclado (ex: `Keys.ENTER`).
   * Captura de tela (`save_screenshot`).

3. **Web Scraping (Wikipedia):**
   * Script que acessa a página principal, pesquisa por uma cidade (ex: Curitiba), aguarda o carregamento e extrai parágrafos específicos do artigo de forma dinâmica.

4. **Preenchimento de Formulários em Massa (Integração com Excel):**
   * Leitura de uma base de clientes em uma planilha `.xlsx`.
   * Laço de repetição (`for`) para acessar um formulário e preencher dados sequenciais (Nome, Email, Telefone) de forma 100% automatizada.
   * Utilização de um formulário HTML local para ambiente de testes seguro.

##  Como instalar e rodar

### 1. Pré-requisitos
Certifique-se de ter o Python e o Mozilla Firefox instalados na sua máquina.

### 2. Instalação das bibliotecas
Abra o terminal na pasta do projeto e instale as dependências executando:

```bash
pip install selenium pandas openpyxl

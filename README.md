# 🎬 Sistema de Gestão - Rede de Cinemas


Este projeto foi desenvolvido como parte de uma atividade prática de **Engenharia de Software**. O objetivo é gerenciar as operações principais de uma rede de cinemas, integrando modelagem UML, arquitetura em camadas e persistência de dados.

---

## 📌 Contextualização
A empresa enfrentava desafios no controle de filmes em exibição, organização de sessões (respeitando intervalos) e registro diário de público. Este sistema centraliza essas informações para garantir confiabilidade e facilidade de evolução.

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3.x
* **Banco de Dados:** SQLite (Persistência local)
* **Modelagem:** UML 2.0 (Casos de Uso, Classes, Atividades e Sequência)
* **Arquitetura:** MVC (Model-View-Controller) + Service + Repository

---

## 📂 Estrutura do Projeto
O projeto está organizado seguindo padrões de arquitetura limpa:

- `docs/`: Documentação de requisitos e diagramas UML.
- `src/`: Código-fonte da aplicação.
    - `controller/`: Intermédio entre a View e a lógica de negócio.
    - `service/`: Regras de negócio e validações.
    - `repository/`: Camada de acesso ao banco de dados (SQLite).
    - `main.py`: Ponto de entrada do sistema.

---

## 📊 Modelagem UML

### 1. Diagrama de Classes (Domínio)
Representa as principais entidades do negócio: **Cinema**, **Filme** e **Sessão**.
<img width="308" height="365" alt="Diagrama_de_Classes_do_Domínio" src="https://github.com/user-attachments/assets/fe35a892-df0b-4054-8d49-82d343f8080f" />


### 2. Diagrama de Sequência
Demonstra a interação entre as camadas para o cadastro de um filme.
<img width="1005" height="514" alt="Diagrama_de_Sequência" src="https://github.com/user-attachments/assets/cbd025cb-9e00-4ee6-8457-4c140c3f697b" />


## ⚙️ Regras de Negócio Implementadas
1.  **Conflito de Horário:** Não permite sessões simultâneas no mesmo cinema sem intervalo mínimo.
2.  **Limite de Público:** O registro de público não pode exceder a capacidade da sala.


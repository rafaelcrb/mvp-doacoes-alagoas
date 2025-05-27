# Sistema de Doações para Municípios de Alagoas

## 📖 Descrição
Este projeto é um MVP (Produto Mínimo Viável) desenvolvido para organizar e facilitar doações a pontos de apoio nos municípios de Alagoas afetados por enchentes e inundações.  

A aplicação permite cadastrar Pontos de Apoio, registrar doações e listar campanhas ativas, tudo com uma interface moderna e responsiva.  

---

## 🚀 Funcionalidades
✅ Cadastro de Pontos de Apoio com Chave Pix  
✅ Listagem de Pontos de Apoio com botão para copiar Chave Pix  
✅ Cadastro e listagem de Doadores  
✅ Listagem de Campanhas em andamento  
✅ Relatório de Doações  
✅ Layout responsivo com Bootstrap e ícones com FontAwesome  
✅ Mensagens de sucesso via `flash` e modais para cadastros  

---

## 🛠️ Tecnologias
- Python 3.x  
- Flask  
- SQLite  
- Bootstrap 4  
- FontAwesome  

---

## 📂 Estrutura do Projeto

mvp-doacoes-alagoas/
├── app.py
├── templates/
│ ├── base.html
│ ├── index.html
│ ├── instituicoes.html
│ ├── doar.html
│ ├── campanhas.html
│ ├── sobre.html
│ └── relatorio.html
├── static/
│ └── style.css
├── database.db (ignorado no .gitignore)
├── requirements.txt
└── .gitignore


## ⚙️ Como executar

1. Clone o repositório:  
   ```bash
   git clone https://github.com/rafaelcrb/mvp-doacoes-alagoas.git
   cd mvp-doacoes-alagoas

   Instale as dependências:
   pip install -r requirements.txt


Execute a aplicação:
python app.py
Acesse no navegador:
http://127.0.0.1:5000

✅ Requisitos
Python 3.x

Pip

Git

📋 Futuras melhorias
Integração com API de pagamento via Pix

Exportação de relatórios em PDF/CSV

Sistema de autenticação para administradores

Dashboard com gráficos de doações
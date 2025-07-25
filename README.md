# 🚀 API Flask para Gestão de Usuários

Uma API RESTful desenvolvida com **Python + Flask**, voltada para o gerenciamento de usuários. Ideal para sistemas de autenticação, cadastros, microserviços e como base sólida para novos projetos de back-end.

## 🔥 Destaques

- ✅ Cadastro, leitura, atualização e exclusão de usuários (CRUD)
- 🔐 Autenticação segura com JWT (JSON Web Tokens)
- 🧱 Estrutura de código modular e fácil de escalar
- 🧪 Pronta para receber testes automatizados com `pytest`
- 🐳 Arquivo `requirements.txt` pronto para deploy (Docker-friendly)
- 🧠 Código limpo, comentado e pensado para iniciantes e profissionais

---

## 📸 Demonstração

### ▶️ Requisição com Postman
![API rodando com sucesso](./assets/api_postman_demo.png)

---

## ⚙️ Tecnologias utilizadas

- [Python 3.x](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/)
- [SQLite](https://www.sqlite.org/) (ou PostgreSQL)
- [Werkzeug](https://werkzeug.palletsprojects.com/) para segurança de senhas

---

## 📦 Como rodar localmente

```bash
# 1. Clone o repositório
git clone https://github.com/Fabiano-Ramos/api_flask_users.git
cd api_flask_users

# 2. (Opcional) Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Rode a aplicação
flask run
🔁 Endpoints
Método	Rota	Descrição
POST	/register	Cria um novo usuário
POST	/login	Autentica e gera token
GET	/users	Lista todos os usuários
PUT	/user/<id>	Atualiza usuário
DELETE	/user/<id>	Deleta usuário

Todos os endpoints (exceto /register e /login) exigem token JWT.

📄 Licença
Este projeto está sob a licença MIT — fique à vontade para usar, modificar e compartilhar.

💼 Contato
Desenvolvido com 💻 e café por Bow-Z 😎
🔗 https://www.linkedin.com/in/fabiano-ramos-do-nascimento-707941315
📫 fabiano.ramos@live.com

⭐ Dê uma estrela!
Se esse projeto te ajudou ou te inspirou, deixe uma ⭐ no repositório pra apoiar o trabalho!



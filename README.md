# Sistema de mercado

Interface: PyQt

Banco de dados: sqlite3

Envio de emails: smtp + emails
## Instalação

Instale o PyQt5 por meio do pip:

```bash
pip install PyQt5
```

## Usabilidade

```python
Ao rodar o arquivo Login.py você verá uma tela de login.

Pra testar o sistema como administrador: admin/admin
E como operador: operador/operador
```

## Conteúdo

```
Como administrador você trabalha com três tabelas: funcionários, produtos e fornecedores (CRUD)
Como operador de caixa você retorna o valor das compras digitando o código do produto e a quantidade
Caso o estoque do produto seja menor que 10 um email é disparado para o email cadastrado do fornecedor

```

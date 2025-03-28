## **Descrição do Projeto**

O objetivo do Teste 4 é desenvolver uma API em Python utilizando **FastAPI** e uma interface web em **Vue.js**. A API realiza buscas textuais em uma lista de operadoras de saúde, enquanto o frontend exibe os resultados de forma interativa. Este teste demonstra habilidades em desenvolvimento de APIs, integração com frontend e uso de ferramentas modernas como Docker.

---

## 🛠️ **Execução**

### **Subindo o Backend e o Frontend**

Para subir o backend e o frontend, basta executar o seguinte comando na raiz do projeto:

```bash
docker-compose up --build
```

O que acontece ao executar o comando:
O Docker Compose irá construir as imagens do backend e do frontend.
Todas as dependências do projeto serão instaladas automaticamente.
O backend será iniciado na porta 8000 e o frontend na porta 8080.
🌐 Acessando a Interface Web
Após executar o Docker Compose, a interface web estará acessível em:

http://localhost:8080

📂 Coleção do Postman
`/postman/IntuitiveCare.postman_collection.json`
A coleção do Postman, que contém as rotas da API para testes e validação, está disponível na pasta:

Você pode importar essa coleção no Postman para realizar testes diretamente na API. 
# Intensivo de Docker

## Sobre

Pequeno bloco de notas sobre Docker escrito durante intensivo de Docker do Fabrício Veronez (KubeDev.io).

## 1 Docker

### 1.1 Comandos

- `docker container ls` ou `docker ps` - listar os containers rodando;
- `docker container ls -a` ou `docker ps -a` - listar todos os containers (rodando e parados);

- `docker container run --name meu_container hello-world` - nomeia o container

- `docker container run -it ubuntu /bin/bash` - executa o container em modo interativo.

- `docker container rm nome_ou_id` - remove o container.

- `docker container run -d` - `-d` executa o modo deamon, executa em segundo plano e libera o console.

- `docker container run -e ENV=1` - seta variáveis de ambiente.

- `docker container run -p 27017:27017` - port binding do container para a máquina.

- `docker build -t nome` - cria a imagem da aplicação `Dockerfile`

- `docker image ls` - lista as imagens disponíveis

- `docker image prune` - remove imagens intermediárias.

- `docker network create nome` - cria uma network para que containers possam se comunicar.

- `docker network ls` - lista as networks

- `docker container run --network-nome` - rodar na network

- `docker volume create mongo-vol` - cria um volume para o mongo

- `docker volume ls` - lista os volumes

- `docker container run -v mongo-vol:/data/db` - mapeia o volume mongo-vol para a pasta /data/db do container.


### 1.2 - Passo a passo

1 - Criar uma network
2 - Criar volume do mongodb
3 - Criar o container com o MongoDB (na network criada)
4 - Criar o container com a API (na network criada)

```bash
docker network create api-env
docker volume create mongo-vol
docker container run -d -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=mongouser -e MONGO_INITDB_ROOT_PASSWORD=mongopwd --name mongo --network=api-env -v mongo-vol:/data/db mongo
docker container run -d -p 8080:8080 -e MONGODB_URI=mongodb://mongouser:mongopwd@mongo:27017/admin --network api-env --name api  api-produto
```

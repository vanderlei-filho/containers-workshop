# Containers & REST APIs Workshop

## Containers vs Virtual Machines

![contvsvms](./docs/images/containers-vs-virtual-machines.jpg)

## Ferramentas

- Podman: https://podman.io/
- Docker: https://www.docker.com/
- IBM CLI: https://github.com/IBM-Cloud/ibm-cloud-cli-release/releases/


## API REST em Python Flask

```bash
.
└── python-api
    ├── app
    │   ├── __init__.py
    │   └── main
    │       ├── __init__.py
    │       └── routes.py
    ├── boot.sh
    ├── config.py
    ├── Dockerfile
    ├── flask_server.py
    └── requirements.txt
```

Arquivos importantes:

- `/app/main/routes.py` contém a lógica de negócio
- `/config.py` e `/.env` é onde configuramos as variáveis de ambiente na aplicação
- `requirements.txt` é onde listamos os pacotes Python necessários
- `Dockerfile` é a "receita de bolo" para construir o ambiente onde a aplicação irá ser executada (desde nível de SISTEMA OPERACIONAL)

## Onde posso realizar deploy desse código na IBM Cloud?

    - IBM Code Engine
    - Kubernetes (IKS: IBM Kubernetes Service)
    - OpenShift (ROKS: Red Hat OpenShift Kubernetes Service)
    - IBM Cloud Functions

## Como construir a imagem?

```bash
podman build . -t <repo>/<namespace>/<image_name>:<version_tag>
```

ou 

```bash
docker build . -t <repo>/<namespace>/<image_name>:<version_tag>
```

## Como executá-lo?

```bash
podman run -p 5000:5000 <repo>/<namespace>/<image_name>:<version_tag>
```

```bash
docker run -p 5000:5000 <repo>/<namespace>/<image_name>:<version_tag>
```


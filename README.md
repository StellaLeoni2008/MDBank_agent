<h1 align="center"> 🏦 MDBank AI </h1>

<img width="1100" height="580" alt="ChatGPT Image 4 de jun  de 2026, 14_58_19" src="https://github.com/user-attachments/assets/69fd6095-1584-4a85-b758-90ba297becc3" />

---

## 💻 Tecnologias utilizadas no projeto

<img loading="lazy" src="https://img.shields.io/badge/Python-darkblue"/>      <img loading="lazy" src="https://img.shields.io/badge/FastAPI-purple"/>      <img loading="lazy" src="https://img.shields.io/badge/FastMCP-pink"/>      <img loading="lazy" src="https://img.shields.io/badge/React-darkgreen"/>      <img loading="lazy" src="https://img.shields.io/badge/Streamlit-red"/>      <img loading="lazy" src="https://img.shields.io/badge/Docker_Compose-blue"/>      <img loading="lazy" src="https://img.shields.io/badge/JavaScript-yellow"/>      <img loading="lazy" src="https://img.shields.io/badge/JSON--RPC-grey"/>      <img loading="lazy" src="https://img.shields.io/badge/A2A-green"/>     

---

## 📌 Sobre
O **MDBank AI** foi desenvolvido durante o curso **Alura - Protocolos e arquitetura para construção de agentes: MCP, A2A, AG-UI e Backend for Agents (BFA)**.

O objetivo do projeto foi construir uma arquitetura multiagente aplicada a um cenário bancário, explorando protocolos modernos de comunicação entre agentes, ferramentas, front-end e backend.

A aplicação simula um assistente bancário inteligente capaz de compreender a intenção do usuário, rotear a solicitação para o agente correto e executar ações relacionadas a serviços do MDBank, como abertura de conta e consulta/solicitação de cartão de crédito.

---

## 🧠 Objetivos do projeto

Este projeto teve como foco praticar a construção de arquiteturas reais para agentes de IA, indo além de um chatbot simples.

Os principais objetivos foram:

- Projetar uma arquitetura multiagente distribuída
- Utilizar protocolos como **MCP**, **A2A** e **AG-UI**
- Implementar uma camada **Backend for Agents (BFA)**
- Separar regras de negócio da camada de agentes
- Criar agentes especializados para diferentes intenções bancárias
- Integrar front-end, backend, agentes e ferramentas externas
- Executar múltiplos serviços isolados com Docker Compose

---

## 🏗️ Arquitetura do sistema

A arquitetura do MDBank AI é composta por diferentes camadas responsáveis por comunicação, roteamento, regras de negócio e execução dos agentes.

<p align="center">
<img width="900" alt="Arquitetura MDBank AI" src="(https://img.shields.io/badge/AG--UI-ora[AgentMDBank.drawio.pdf])" />
<img loading="lazy" src="https://img.shields.io/badge/AG--UI-ora[AgentMDBank.drawio.pdf](https://github.com/user-attachments/files/28840943/AgentMDBank.drawio.pdf)
nge"/>
</p>

---

## 🤖 Agentes do sistema
O projeto utiliza agentes especializados para lidar com diferentes tipos de solicitação do usuário.

### 🏦 Agente de Abertura de Conta
Responsável por conduzir o fluxo de abertura de conta bancária.

Esse agente pode:
- solicitar dados necessários do usuário
- validar informações recebidas
- criar ou buscar uma conta existente
- retornar mensagens personalizadas ao usuário

### 💳 Agente de Cartão de Crédito
Responsável por lidar com solicitações relacionadas a cartões.

Esse agente pode:
- consultar dados de cartão
- solicitar cartão de crédito
- exibir número, tipo e limite do cartão
- formatar respostas com informações destacadas

### 🧭 Supervisor

Responsável por identificar a intenção do usuário e encaminhar a solicitação para o agente adequado.
Exemplos de intenções:

- “Quero abrir uma conta”
- “Quero um cartão de crédito”
- “Quando exibir o número do meu cartão...”

---

## 🔌 Protocolos explorados

### MCP - Model Context Protocol
O **MCP** foi utilizado para expor recursos e ferramentas que podem ser acessados pelos agentes.
Exemplos de recursos e ferramentas do projeto:
- `consultar_conta`
- `consultar_cartao`
- `criar_ou_buscar_conta`
- `solicitar_cartao`
- `gerar_prompt_abertura`
- `abrir_conta_prompt`
- `solicitar_cartao_prompt`
- `obter_conta`
- `obter_cartao`

---

### A2A - Agent to Agent
O protocolo **A2A** foi utilizado para representar a comunicação entre agentes especializados.
No projeto, ele permite que o roteador encaminhe solicitações para agentes como:
- agente de abertura de conta
- agente de cartão de crédito
- agente de suporte ao cliente

---

### AG-UI
O **AG-UI** foi explorado para criar uma interface interativa conectada aos agentes.
A interface permite:
- enviar mensagens ao assistente
- visualizar o histórico de respostas
- acompanhar o estado compartilhado
- exibir respostas estruturadas dos agentes
- renderizar informações como cartões, tabelas e destaques visuais

---

### BFA - Backend for Agents
A camada **Backend for Agents (BFA)** foi utilizada para organizar a lógica de negócio e desacoplar os agentes das regras internas da aplicação.
Essa camada é responsável por:
- centralizar regras de negócio
- organizar fluxos complexos
- expor serviços reutilizáveis
- permitir integração entre agentes, ferramentas e dados

---

## ✨ Funcionalidades

- Chat com assistente bancário inteligente
- Roteamento automático de intenções
- Abertura de conta bancária
- Solicitação de cartão de crédito
- Consulta de informações de cartão
- Exibição de respostas estruturadas
- Histórico de respostas
- Estado compartilhado da conversa
- Integração entre agentes especializados
- Comunicação entre serviços via APIs
- Execução com Docker Compose

---

## 🖼️ Demonstração do projeto

### Chat com abertura de conta

<p align="center">
<img width="500" alt="Abertura de conta MDBank" src="https://github.com/user-attachments/assets/9ff7eba6-71a7-4fbd-bb28-f88a059fa3ae" />
</p>


---

### Consulta e exibição de cartão de crédito

<p align="center">
<img width="500" alt="Cartão de crédito MDBank" src="https://github.com/user-attachments/assets/ee06b663-ee38-47cd-a035-dc0fdab09699" />
</p>

---

### Histórico de respostas e estado compartilhado

<p align="center">
<img width="500" alt="Histórico MDBank" src="https://github.com/user-attachments/assets/9ddfd458-88dd-4ae5-a328-e40b3ccf0d46" />
</p>

---

## 📂 Estrutura do projeto
```text
MDBank_agent/
├── MDBank/
│   └── Supervisor / roteador principal
│
├── agents/
│   ├── abrir_conta/
│   └── cartao_credito/
│
├── bfa/
│   └── Camada Backend for Agents
│
├── frontend/
│   └── Interface Streamlit
│
├── frontend2/
│   └── Interface React / AG-UI
│
├── recursos/
│   └── Recursos e tools utilizados pelos agentes
│
├── docker-compose.yml
└── README.md
```

---

## ▶️ Como executar o projeto
### 1. Clone este repositório

```bash
git clone https://github.com/StellaLeoni2008/MDBank_agent.git
```

### 2. Acesse a pasta do projeto

```bash
cd MDBank_agent
```

### 3. Execute os serviços com Docker Compose

```bash
docker compose up --build
```

### 4. Acesse a aplicação

Após subir os containers, acesse a interface pelo navegador:

```text
http://localhost:9090
```
---

## 🧠 Conceitos praticados

Durante o desenvolvimento deste projeto, foram praticados conceitos avançados de arquitetura para agentes de IA, incluindo:

- Sistemas multiagente
- Roteamento de intenções
- Comunicação entre agentes
- Protocolos MCP, A2A e AG-UI
- Backend for Agents
- Separação entre agentes e regras de negócio
- Catálogo de agentes e ferramentas
- APIs HTTP com FastAPI
- Comunicação distribuída com JSON-RPC
- Serviços MCP com FastMCP
- Interfaces interativas com React e Streamlit
- Estado compartilhado entre usuário e agentes
- Docker Compose para orquestração de serviços
- Modularização de sistemas com múltiplos containers

---

<br>
## 👩🏻‍💻 Autora

| [<img loading="lazy" src="https://avatars.githubusercontent.com/u/237313711?v=4" width=115><br><sub>Stella Leoni</sub>](https://github.com/StellaLeoni2008) |
| :---: |

---

<p align="right">
2026
</p>

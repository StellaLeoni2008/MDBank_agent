from a2a.server.apps import A2AStarletteApplication
from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.tasks import InMemoryTaskStore
from a2a.types import AgentCapabilities, AgentCard, AgentSkill
from executor import AbrirContaExecutor

#Definiçao do skill/habilidades
skill = AgentSkill(
    id="abrir_conta",
    name="Abertura de Conta MDBank", 
    description="Ajuda clientes a abrirem uma conta bancária e explica os tipos de contas disponíveis.",
    tags=[
        "conta",
        "abrir_conta",
        "abrir conta no banco",
        "conta corrente",
        "conta poupança",
        "abrir conta digital",
        "cadastro bancário"
    ],
    examples=[
        "quero abrir uma conta",
        "como faço para abrir uma conta?",
        "quais tipos de conta vocês oferecem?",
        "quero criar uma conta corrente",
        "posso abrir uma conta digital?"
    ],
)

#Agent Card
agent_card = AgentCard(
    name="Agente de Abertura de Conta MDBank",
    description="Especialista em abertura de contas bancárias do MDBank.",
    url="http://abrir_conta_agent:8000/",
    defaultInputModes=["text"],
    defaultOutputModes=["text"],
    skills=[skill],
    version="1.0.0",
    capabilities=AgentCapabilities(),
)

#Request Handler
handler = DefaultRequestHandler(
    agent_executor=AbrirContaExecutor(),
    task_store=InMemoryTaskStore(),
)

#A2A Application
server = A2AStarletteApplication(
    http_handler=handler, 
    agent_card=agent_card,
)

#Exposição do app para o uvicorn 
app = server.build()
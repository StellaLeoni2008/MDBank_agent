from a2a.server.apps import A2AStarletteApplication
from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.tasks import InMemoryTaskStore
from a2a.types import AgentCapabilities, AgentCard, AgentSkill
from executor import CartaoDeCreditoExecutor

#Definiçao do skill/habilidades
skill = AgentSkill(
    id="carta_credito",
    name="Cartões de Crédito MDBank", 
    description="Ajuda clientes com dúvidas, solicitações e limites de cartões de crédito.",
    tags=[
        "cartão",
        "crédito",
        "limite",
        "platinum",
        "gold", 
        "silver",
        "black",
        "md_card"
    ],
    examples=[
        "quais cartões vocês tem?",
        "quero solicitar um cartão platinum",
        "qual é o limite do meu cartão?",
        "posso aumentar meu limite?",
        "quero um cartão md_card."
    ],
)

#Agent Card
agent_card = AgentCard(
    name="Agente de Cartões MDBank",
    description="Especialista em cartões de crédito do MDBank.",
    url="http://cartao_credito_agent:8000/",
    defaultInputModes=["text"],
    defaultOutputModes=["text"],
    skills=[skill],
    version="1.0.0",
    capabilities=AgentCapabilities(),
)

#Request Handler
handler = DefaultRequestHandler(
    agent_executor=CartaoDeCreditoExecutor(),
    task_store=InMemoryTaskStore(),
)

#A2A Application
server = A2AStarletteApplication(
    http_handler=handler, 
    agent_card=agent_card,
)

#Exposição do app para o uvicorn 
app = server.build()
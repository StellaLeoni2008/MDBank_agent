import asyncio
import httpx
from a2a.client import A2ACardResolver

AGENT_ENDPOINTS = [
    "http://cartao_credito_agent:8000",
    "http://abrir_conta_agent:8000"
]


def normalize(text):
    if not text:
        return ""
    return text.lower().strip()


async def discover_agents():
    registry = {}

    async with httpx.AsyncClient(timeout=5) as client:
        for url in AGENT_ENDPOINTS:

            for attempt in range(3):
                try:
                    response = await client.get(f"{url}/.well-known/agent.json")
                    response.raise_for_status()
                    card_data = response.json()

                    for skill in card_data.get("skills", []):
                        registry[skill["id"]] = {
                            "agent_url": url,
                            "name": skill.get("name"),
                            "description": skill.get("description"),
                            "tags": skill.get("tags", []),
                            "examples": skill.get("examples", []),
                            "type": "agent",
                            "search_text": " ".join([
                                skill.get("name", ""),
                                skill.get("description", ""),
                                " ".join(skill.get("tags", [])),
                                " ".join(skill.get("examples", [])),
                            ]).lower()
                        }

                    break

                except Exception as e:
                    print(f"Tentativa {attempt+1} falhou para {url}: {e}")
                    await asyncio.sleep(2)

    return registry
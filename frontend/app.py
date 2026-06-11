import streamlit as st
import requests

API_URL = "http://supervisor:8000/chat"

st.set_page_config(
    page_title="MDBank Assistente",
    page_icon="🏦",
    layout="centered"
)

# ===== ESTILO =====

st.markdown("""
<style>

.main {
    background-color: #f8fafc;
}

h1 {
    color: #0f172a;
    text-align: center;
}

.stChatMessage {
    border-radius: 12px;
}

[data-testid="stChatInput"] {
    margin-top: 15px;
}

</style>
""", unsafe_allow_html=True)

# ===== CABEÇALHO =====

st.title("🏦 MDBank Assistente")
st.caption("Seu assistente virtual para produtos e serviços bancários")

# ===== HISTÓRICO =====

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ===== INPUT =====

user_input = st.chat_input(
    "Digite sua pergunta..."
)

if user_input:

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    payLoad = {
        "message": user_input,
        "session_id": "123",
        "client_id": "123"
    }

    with st.chat_message("assistant"):

        with st.spinner("Pensando..."):

            try:

                response = requests.post(
                    API_URL,
                    json=payLoad,
                    timeout=60
                )

                if response.status_code == 200:

                    data = response.json()

                    resposta = (
                        data.get("resposta")
                        or data.get("response")
                        or data.get("message")
                        or "Nenhuma resposta recebida."
                    )

                else:

                    resposta = (
                        f"Erro {response.status_code}: "
                        f"{response.text}"
                    )

            except Exception as e:

                resposta = f"Erro ao conectar com a API: {str(e)}"

        st.markdown(resposta)

    st.session_state.messages.append({
        "role": "assistant",
        "content": resposta
    })
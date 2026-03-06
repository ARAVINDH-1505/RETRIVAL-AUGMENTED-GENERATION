from langchain_community.llms.ollama import Ollama
def load_llm():

    llm = Ollama(
        model="mistral",
        num_predict=200
    )

    return llm
# app/services/rag_pipeline.py

# CORRECT IMPORTS FOR LANGCHAIN 0.2.x / 0.3.x
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

def build_rag_pipeline(llm, retriever):
    prompt = ChatPromptTemplate.from_template(
        """
        You are an assistant for answering questions.
        Use the following context to answer the question.
        
        Context:
        {context}
        
        Question:
        {input}
        """
    )

    question_answer_chain = create_stuff_documents_chain(
        llm,
        prompt
    )

    rag_chain = create_retrieval_chain(
        retriever,
        question_answer_chain
    )

    return rag_chain
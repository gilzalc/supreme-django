import os
from langchain.llms import HuggingFaceHub
from langchain.chains import LLMChain, SimpleSequentialChain
from langchain.prompts import PromptTemplate

if __name__ == '__main__':
    hugging_face_token = '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'
    llm = HuggingFaceHub(repo_id='HuggingFaceH4/zephyr-7b-beta',
                         model_kwargs={"temperature": 0.1, "max_new_tokens": 200},
                         huggingfacehub_api_token=hugging_face_token)
    # First chain:
    prompt1 = PromptTemplate(template=""" Question: {question}""", input_variables=["question"])
    chain = LLMChain(prompt=prompt1, llm=llm, verbose=False)
    # Second chain:
    translation_model = HuggingFaceHub(repo_id='Helsinki-NLP/opus-mt-en-de',
                                       huggingfacehub_api_token=hugging_face_token)
    prompt2 = PromptTemplate(input_variables=["answer"], template="Übersetzung: {answer}")
    translation_chain = LLMChain(prompt=prompt2, llm=translation_model)
    overall_chain = SimpleSequentialChain(chains=[chain, translation_chain], verbose=True)
    res = overall_chain.run('when to use BytesIO in python?')
    print(res)

    # text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=0)
    # texts = text_splitter.create_documents([res])
    # print(texts)
    # embeddings = ElasticsearchEmbeddings(model_name="ada")
    # query_res= embeddings.embed_query(texts[0].page_content)
    # print(query_res)
    # print(res)

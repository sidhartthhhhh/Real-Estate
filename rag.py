from uuid import uuid4
from dotenv import load_dotenv
from pathlib import Path
from langchain.chains import RetrievalQAWithSourcesChain
from langchain_community.document_loaders import UnstructuredURLLoader, SeleniumURLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain_huggingface.embeddings import HuggingFaceEmbeddings


load_dotenv()

CHUNK_SIZE = 1000
EMBEDDING_MODEL = "Alibaba-NLP/gte-base-en-v1.5"
VECTORSTORE_DIR = Path(__file__).parent / "resources/vectorstore"
COLLECTION_NAME = 'real_estate'

llm = None
vector_store = None


def initialize_components():
    global llm, vector_store
    if llm is None:
        llm = ChatGroq(model="llama-3.3-70b-versatile",
                    temperature=0.9, max_tokens=500)
    if vector_store is None:
        ef = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL, model_kwargs={
                                "trust_remote_code": True})
        vector_store = Chroma(collection_name=COLLECTION_NAME, embedding_function=ef,
                            persist_directory=str(VECTORSTORE_DIR))


def process_urls(urls):
    yield 'Initialize components'
    initialize_components()

    yield "Resetting vector store..✅"
    vector_store.reset_collection()

    yield "Loading data..✅"
    loader = SeleniumURLLoader(urls=urls)
    data = loader.load()

    yield "Splitting text into chunks..✅"
    splitter = RecursiveCharacterTextSplitter(
        separators=['\n\n', '\n', '.', ' '], chunk_size=CHUNK_SIZE)
    docs = splitter.split_documents(data)

    yield "Add chunks to vector database..✅"
    uuids = [str(uuid4()) for _ in range(len(docs))]
    vector_store.add_documents(docs, ids=uuids)

    yield "Docs added to vector database..✅"


def generate_answer(query):
    if not vector_store:
        raise RuntimeError('Vector db is not initialized')
    chain = RetrievalQAWithSourcesChain.from_llm(
        llm=llm, retriever=vector_store.as_retriever())
    result = chain.invoke({"question": query}, return_only_outputs=True)
    sources = result.get("sources", "")
    return result['answer'], sources


if __name__ == "__main__":
    urls = ["https://www.cnbc.com/2024/12/21/how-the-federal-reserves-rate-policy-affects-mortgages.html",
            "https://www.cnbc.com/2024/12/20/why-mortgage-rates-jumped-despite-fed-interest-rate-cut.html"
            ]

    process_urls(urls)

    results = vector_store.similarity_search(
        "30 year mortage rate",
        k=2
    )

    print(results)
    answer, sources = generate_answer(
        "Tell me what was the 30 year fixed mortagate rate along with the date?")
    print(f"Answer: {answer}")
    print(f"Sources: {sources}")

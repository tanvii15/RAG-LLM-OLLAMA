import argparse
from langchain_chroma import Chroma
from langchain_ollama import OllamaLLM
from get_embedding_function import get_embedding_function

CHROMA_PATH = "chroma"

# 🔐 USER PERMISSIONS
USER_PERMISSIONS = {
    "alice": ["HR"],
    "bob": ["Finance"],
    "charlie": ["Shares"],
    "david": ["Marketing"],
    "admin": ["HR", "Finance", "Shares", "Marketing"]
}

PROMPT_TEMPLATE = """
Answer the question using ONLY the context below.

Context:
{context}

---

Question: {question}
"""

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("query_text", type=str)
    parser.add_argument("--user", type=str, default="alice")

    args = parser.parse_args()

    query_text = args.query_text
    user = args.user

    embedding_function = get_embedding_function()

    db = Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=embedding_function
    )

    # 🔐 Get allowed departments
    allowed_departments = USER_PERMISSIONS.get(user, [])

    print(f"\nUser: {user}")
    print(f"Allowed Departments: {allowed_departments}\n")

    # 🔐 Filter retrieval by department
    results = db.similarity_search(
        query_text,
        k=5,
        filter={"department": {"$in": allowed_departments}}
    )

    if len(results) == 0:
        print("⚠ No documents found for this department.")
        return

    context = "\n\n---\n\n".join([doc.page_content for doc in results])

    prompt = PROMPT_TEMPLATE.format(
        context=context,
        question=query_text
    )

    # ✅ Stable lightweight model
    model = OllamaLLM(model="mistral")

    response = model.invoke(prompt)

    print("\nResponse:\n")
    print(response)


if __name__ == "__main__":
    main()
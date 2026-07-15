from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=700,
        chunk_overlap=120,
        separators=[
            "\n# ",
            "\n## ",
            "\n### ",
            "\n\n",
            "\n",
            ". ",
            "? ",
            "! ",
            "; ",
            ", ",
            " ",
            "",
        ],
        keep_separator=True,
    )

    chunks = splitter.split_documents(documents)

    cleaned = []

    for chunk in chunks:

        text = chunk.page_content.strip()

        if len(text) < 80:
            continue

        chunk.page_content = text

        cleaned.append(chunk)

    return cleaned
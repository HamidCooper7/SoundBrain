from brain.text import TextPipeline

pipeline = TextPipeline()

pipeline.index(
    text="dark emotional piano",
    text_id="text_001",
    metadata={
        "type": "query",
    },
    document="Dark Emotional Piano",
)

result = pipeline.search(
    text="sad cinematic piano",
    top_k=5,
)

print(result)
from brain.audio.search import AudioSearchService

service = AudioSearchService()

result = service.search(
    text="dark emotional piano",
    top_k=5,
)

print(result)
from brain.memory.vector import VectorManager, VectorRecord

db = VectorManager()

record = VectorRecord(
    id="audio_1",
    embedding=[0.1] * 1024,
    metadata={
        "type": "audio",
        "title": "Test Audio",
    },
    document="First audio embedding",
)

db.add(record)

print(db.count())

result = db.search([0.1] * 1024)

print(result)
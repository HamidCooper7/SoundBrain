from sentence_transformers import SentenceTransformer

print("Loading Qwen Embedding...")

model = SentenceTransformer(
    r"E:\SoundBrain\models\Qwen3-Embedding-0.6B",
    trust_remote_code=True
)

print("✅ Model Loaded!")

text = [
    "سلام من یک مهندس صدا هستم.",
    "What is psychoacoustics?"
]

embeddings = model.encode(text)

print(embeddings.shape)
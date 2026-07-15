from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

MODEL_PATH = r"E:\SoundBrain\models\lmstudio-community\Qwen2.5-7B-Instruct"

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

print(f"LLM Device: {DEVICE}")

tokenizer = AutoTokenizer.from_pretrained(
    MODEL_PATH,
    trust_remote_code=True
)

model = AutoModelForCausalLM.from_pretrained(
    MODEL_PATH,
    torch_dtype=torch.float16 if DEVICE == "cuda" else torch.float32,
    device_map="auto",
    trust_remote_code=True
)


def generate(
    prompt: str,
    max_tokens: int = 1024,
    temperature: float = 0.2,
):
    messages = [
        {
            "role": "system",
            "content":
            "You are SoundBrain, an expert audio engineer and music production assistant."
        },
        {
            "role": "user",
            "content": prompt
        }
    ]

    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )

    inputs = tokenizer(
        text,
        return_tensors="pt"
    ).to(model.device)

    outputs = model.generate(
        **inputs,
        max_new_tokens=max_tokens,
        temperature=temperature,
        do_sample=True,
        pad_token_id=tokenizer.eos_token_id,
    )

    answer = tokenizer.decode(
        outputs[0][inputs.input_ids.shape[-1]:],
        skip_special_tokens=True,
    )

    return answer.strip()
from transformers import AutoTokenizer, AutoModelForCausalLM

from brain.runtime import ModelRuntime


MODEL_NAME = "lmstudio-community/Qwen2.5-7B-Instruct"


def _assets():
    runtime = ModelRuntime.shared()
    return runtime.load(
        model_name=MODEL_NAME,
        model_cls=AutoModelForCausalLM,
        tokenizer_cls=AutoTokenizer,
        trust_remote_code=True,
        model_options={
            "device_map": "auto",
            "torch_dtype": runtime.dtype,
        },
    )


def generate(
    prompt: str,
    max_tokens: int = 1024,
    temperature: float = 0.2,
):
    assets = _assets()
    model = assets.model
    tokenizer = assets.tokenizer
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

# ai_providers.py
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load local GPT-2 model and tokenizer
model_name = "gpt2"  # you can also try "gpt2-medium" for better responses
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

def ask_watson(query: str) -> str:
    """
    Generate a response to the user query using GPT-2 locally.
    """
    # Prepare prompt
    prompt = f"User: {query}\nAssistant (friendly financial coach):"
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    
    # Generate output
    outputs = model.generate(
        inputs,
        max_length=200,
        num_return_sequences=1,
        no_repeat_ngram_size=2,
        do_sample=True,
        temperature=0.7,
        top_p=0.9,
    )
    
    # Decode and return text
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # Remove the prompt from the output
    return response.replace(prompt, "").strip()

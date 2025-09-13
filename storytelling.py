# storytelling.py
def story_from_data(user_id: str, summary: str) -> str:
    """
    Converts summary into a friendly story.
    Later you can replace with HuggingFace/Granite text generation.
    """
    if "Food" in summary:
        return f"{user_id}, your wallet’s story is about balance — you managed your food expenses well!"
    return f"{user_id}, this month’s money story is simple: {summary}"

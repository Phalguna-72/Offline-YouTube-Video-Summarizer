from transformers import pipeline
from utils.chunker import chunk_text


def summarize_text(text, model_name="facebook/bart-large-cnn"):
    summarizer = pipeline(
        "summarization",
        model=model_name,
        device=-1  # CPU
    )

    # ---- First pass: chunk-level summaries ----
    chunks = chunk_text(text, max_words=400)
    chunk_summaries = []

    for chunk in chunks:
        summary = summarizer(
            chunk,
            max_length=120,
            min_length=40,
            do_sample=False
        )
        chunk_summaries.append(summary[0]["summary_text"])

    # ---- Second pass: abstract the summaries ----
    combined_summary = " ".join(chunk_summaries)

    final_summary = summarizer(
        combined_summary,
        max_length=100,
        min_length=40,
        do_sample=False
    )

    return final_summary[0]["summary_text"]

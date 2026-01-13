
# backend/services/text_summarizer.py

from transformers import pipeline

# Global summarizer instance
summarizer = None

def summarize_text(text):
    """
    Summarizes the given text using HuggingFace pipeline.
    """
    if not text:
        return ""
    
    if len(text.split()) < 30: # If too short, return as is
        return text

    if summarizer:
        try:
            # Check length to avoid index errors
            max_len =  min(120, len(text.split())) 
            min_len =  min(30, max_len - 10)
            
            summary = summarizer(text, max_length=max_len, min_length=min_len, do_sample=False)
            return summary[0]['summary_text']
        except Exception as e:
            print(f"Summarization error: {e}")
            return text # Fallback to original text
    else:
        return text # Fallback if unchecked model load failed

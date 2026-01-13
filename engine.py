import nltk
nltk.download('averaged_perceptron_tagger_eng', quiet=True)

from g2p_en import G2p
import Levenshtein
import difflib

g2p = G2p()

def get_phonemes(text):
    """Convert words into ARPAbet Phonemes"""
    return [p for p in g2p(text) if p.strip()]

def calculate_pronunciation_score(target_word, user_transcript):
    target_p = get_phonemes(target_word)
    user_p = get_phonemes(user_transcript)
    
    # Calculate Levenshtein Distance
    dist = Levenshtein.distance(target_p, user_p)
    max_len = max(len(target_p), len(user_p))
    
    if max_len == 0: return 0, target_p, user_p, ""
    
    score = ((max_len - dist) / max_len) * 100
    
    # Generate Feedback string
    diff = difflib.ndiff(target_p, user_p)
    feedback = []
    for d in diff:
        if d.startswith('  '): feedback.append(f"{d[2:]}") # Correct
        elif d.startswith('- '): feedback.append(f"({d[2:]} missed)") # Missing
        elif d.startswith('+ '): feedback.append(f"[{d[2:]} extra]") # Extra
        
    return round(score, 2), target_p, user_p, " ".join(feedback)
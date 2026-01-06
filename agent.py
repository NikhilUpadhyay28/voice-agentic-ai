# agent.py

from tools import retrieve_schemes, check_eligibility

conversation_memory = []

def run_agent(user_text, lang):
    conversation_memory.append(user_text)

    # HARD SAFETY: never return empty
    if not user_text or len(user_text.strip()) < 2:
        return fallback_message(lang)

    text = user_text.lower()

    if "नमस्ते" in text or "hello" in text:
        return greeting(lang)

    if any(word in text for word in ["योजना", "scheme", "প্রকল্প", "ଯୋଜନା"]):
        scheme = retrieve_schemes("housing")
        eligibility = check_eligibility(25, 400000)
        return f"{scheme}. {eligibility}"

    # Memory-based response
    if len(conversation_memory) > 1:
        return followup(lang)

    return fallback_message(lang)


def greeting(lang):
    return {
        "hi-IN": "नमस्ते! मैं आपकी कैसे मदद कर सकता हूँ?",
        "bn-IN": "নমস্কার! আমি কীভাবে আপনাকে সাহায্য করতে পারি?",
        "or-IN": "ନମସ୍କାର! ମୁଁ କିପରି ସହଯୋଗ କରିପାରିବି?"
    }.get(lang, "नमस्ते!")


def followup(lang):
    return {
        "hi-IN": "क्या आप किसी सरकारी योजना के बारे में जानना चाहते हैं?",
        "bn-IN": "আপনি কি কোনো সরকারি প্রকল্প সম্পর্কে জানতে চান?",
        "or-IN": "ଆପଣ କୌଣସି ସରକାରୀ ଯୋଜନା ବିଷୟରେ ଜାଣିବାକୁ ଚାହାନ୍ତି କି?"
    }.get(lang, "क्या आप और जानकारी चाहते हैं?")


def fallback_message(lang):
    return {
        "hi-IN": "कृपया अपनी समस्या बताइए।",
        "bn-IN": "অনুগ্রহ করে আপনার সমস্যাটি বলুন।",
        "or-IN": "ଦୟାକରି ଆପଣଙ୍କ ସମସ୍ୟା କହନ୍ତୁ।"
    }.get(lang, "कृपया बताइए।")

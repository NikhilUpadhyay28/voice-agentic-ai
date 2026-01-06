from tools import retrieve_schemes, check_eligibility

def execute(plan_text, user_text, lang):
    result = []

    if "scheme" in plan_text.lower():
        scheme = retrieve_schemes("housing")
        result.append(scheme)

    if "eligibility" in plan_text.lower():
        eligibility = check_eligibility(25, 400000)
        result.append(eligibility)

    if not result:
        result.append("मैं आपकी सहायता करने के लिए यहाँ हूँ")

    return " ".join(result)

def retrieve_schemes(category):
    schemes = {
        "housing": "प्रधानमंत्री आवास योजना – गरीब नागरिकों के लिए घर",
        "loan": "प्रधानमंत्री मुद्रा योजना – बिना गारंटी ऋण",
        "education": "सुकन्या समृद्धि योजना – बालिकाओं की शिक्षा"
    }
    return schemes.get(category.lower(), "कोई योजना नहीं मिली")


def check_eligibility(age, income):
    if age >= 18 and income < 500000:
        return "आप इस योजना के लिए पात्र हैं"
    return "आप इस योजना के लिए पात्र नहीं हैं"

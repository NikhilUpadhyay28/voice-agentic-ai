def evaluate(response_text):
    if "पात्र" not in response_text:
        return response_text + " कृपया अपनी आय और उम्र बताएं।"
    return response_text

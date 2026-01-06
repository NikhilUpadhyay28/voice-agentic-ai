from planner import plan
from executor import execute
from evaluator import evaluate

# memory
conversation_memory = []

def run_agent(user_text, lang):
    conversation_memory.append(user_text)

    # 1️⃣ PLAN
    steps = plan(user_text)

    # 2️⃣ EXECUTE
    raw_response = execute(steps, user_text, lang)

    # 3️⃣ EVALUATE
    final_response = evaluate(raw_response)

    return final_response

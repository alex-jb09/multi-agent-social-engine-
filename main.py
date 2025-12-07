from agents.agent import Agent
from agents.persona_builder import load_mbti_sample, generate_persona
from orchestrator.dialogue_manager import DialogueManager

def fake_llm(prompt):
    return "This is a placeholder response until LLM is added."

def main():
    df = load_mbti_sample()
    persona1 = generate_persona(df)
    persona2 = generate_persona(df)

    agent1 = Agent("Alice", persona1, fake_llm)
    agent2 = Agent("Bob", persona2, fake_llm)

    dm = DialogueManager(agent1, agent2)
    print("=== Multi-Agent Conversation ===")
    print(dm.run())

if __name__ == "__main__":
    main()

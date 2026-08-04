from app.agents.scenario_interpreter_agent import scenario_interpreter_agent

query = "Suppose salary is my highest priority and I want Bangalore."

result = scenario_interpreter_agent(query)

print("\n===== Scenario =====\n")

print(result)
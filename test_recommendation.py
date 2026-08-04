from app.graph.builder import graph
from app.models.sample_data import sample_state

result = graph.invoke(sample_state)

print("\n========== FINAL RECOMMENDATION ==========\n")

print(result["recommendation"])
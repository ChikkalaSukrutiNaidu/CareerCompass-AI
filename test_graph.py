from app.graph.builder import graph

from app.models.sample_data import sample_state


result = graph.invoke(sample_state)

print("\n==============================")
print("CareerCompass Completed")
print("==============================\n")

print(result)
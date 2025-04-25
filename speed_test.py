import time
import random
import matplotlib.pyplot as plt
import pandas as pd

def benchmark_search(file_path: str, queries: list, reread_on_query: bool):
    """

    Args:
      file_path: str: 
      queries: list: 
      reread_on_query: bool: 

    Returns:

    """
    with open(file_path, "r") as f:
        lines = set(f.read().splitlines())

    times = []
    for query in queries:
        start_time = time.time()
        if reread_on_query:
            with open(file_path, "r") as f:
                found = query in f.read().splitlines()
        else:
            found = query in lines
        times.append(time.time() - start_time)
    return times

def generate_report():
    """ """
    FILE_PATH = "200k.txt"
    QUERIES = [random.choice(open(FILE_PATH).read().splitlines()) for _ in range(100)]

    # Benchmark with REREAD_ON_QUERY=True
    times_true = benchmark_search(FILE_PATH, QUERIES, True)

    # Benchmark with REREAD_ON_QUERY=False
    times_false = benchmark_search(FILE_PATH, QUERIES, False)

    avg_time_true = sum(times_true) / len(times_true) * 1000
    avg_time_false = sum(times_false) / len(times_false) * 1000

    print(f"Average time (REREAD_ON_QUERY=True): {avg_time_true:.2f}ms")
    print(f"Average time (REREAD_ON_QUERY=False): {avg_time_false:.2f}ms")

    # Create DataFrame for table
    data = {
        "Algorithm": ["File Re-read", "Preloaded File"],
        "Average Time (ms)": [avg_time_true, avg_time_false],
    }
    df = pd.DataFrame(data)

    # Save table as CSV
    df.to_csv("speed_test_results.csv", index=False)

    # Plot graph
    plt.figure(figsize=(10, 6))
    plt.bar(df["Algorithm"], df["Average Time (ms)"], color=["blue", "green"])
    plt.title("Search Algorithm Performance Comparison")
    plt.ylabel("Average Time (ms)")
    plt.xlabel("Algorithm")
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    # Save graph as PNG
    plt.savefig("speed_test_graph.png")
    plt.show()

if __name__ == "__main__":
    generate_report()
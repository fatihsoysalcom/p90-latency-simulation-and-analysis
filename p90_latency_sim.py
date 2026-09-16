import random
import statistics

def simulate_session_wait_times(num_connections):
    """Simulates session wait times for a given number of MCP connections."""
    wait_times = []
    # Simulate a distribution where most connections are fast, but a few are very slow.
    # This mimics the scenario where P90 latency is high.
    for _ in range(num_connections):
        if random.random() < 0.95:  # 95% of connections are relatively fast
            wait_time = random.uniform(0.1, 5.0)  # Fast wait times between 0.1 and 5 seconds
        else:  # 5% of connections are significantly slower
            wait_time = random.uniform(20.0, 60.0) # Slow wait times between 20 and 60 seconds
        wait_times.append(wait_time)
    return wait_times

def calculate_p90_latency(wait_times):
    """Calculates the P90 latency from a list of wait times."""
    # Sort the wait times to easily find percentiles
    sorted_wait_times = sorted(wait_times)
    
    # Calculate the index for the 90th percentile
    # P90 means 90% of data is below this value.
    p90_index = int(len(sorted_wait_times) * 0.90)
    
    # Ensure the index is within bounds
    if p90_index >= len(sorted_wait_times):
        p90_index = len(sorted_wait_times) - 1
        
    return sorted_wait_times[p90_index]

if __name__ == "__main__":
    # Number of MCP connections as mentioned in the article
    num_connections = 27257
    
    print(f"Simulating {num_connections} MCP connections...")
    session_wait_times = simulate_session_wait_times(num_connections)
    
    # Calculate and print the P90 latency
    p90_latency = calculate_p90_latency(session_wait_times)
    
    print(f"\n--- Analysis Results ---")
    print(f"Total connections analyzed: {num_connections}")
    # The article mentions P90 reaching 35 seconds. Our simulation aims to demonstrate this possibility.
    print(f"Calculated P90 session wait time: {p90_latency:.2f} seconds")
    
    # For comparison, let's also show the average
    average_latency = statistics.mean(session_wait_times)
    print(f"Average session wait time: {average_latency:.2f} seconds")
    
    print("\nThis simulation illustrates how a small percentage of very long wait times can significantly increase the P90 latency, even if the average is much lower.")

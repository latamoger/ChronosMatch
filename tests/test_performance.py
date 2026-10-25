import csv
import time
from pathlib import Path
from matching_engine import MatchingEngine


def performance_test(number_of_orders):
    engine = MatchingEngine()

    start = time.perf_counter()

    for i in range(number_of_orders):
        if i % 2 == 0:
            engine.submit_order("BUY", 100, 10)
        else:
            engine.submit_order("SELL", 100, 10)

    end = time.perf_counter()

    total_time = end - start
    throughput = number_of_orders / total_time
    average_latency = (total_time / number_of_orders) * 1000

    print(f"\nOrders: {number_of_orders}")
    print(f"Total Time: {total_time:.6f} seconds")
    print(f"Throughput: {throughput:.2f} orders/sec")
    print(f"Average Time: {average_latency:.6f} ms")

    return [
        number_of_orders,
        total_time,
        throughput,
        average_latency
    ]


def main():
    results = []

    for count in [100, 1000, 5000, 10000]:
        results.append(performance_test(count))

    report_folder = Path(__file__).resolve().parents[1] / "reports"
    report_folder.mkdir(exist_ok=True)

    file_path = report_folder / "performance_results.csv"

    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "Orders",
            "Total_Time_Seconds",
            "Throughput_Orders_Per_Second",
            "Average_Time_Milliseconds"
        ])

        writer.writerows(results)

    print("\nPerformance report saved successfully!")


if __name__ == "__main__":
    main()
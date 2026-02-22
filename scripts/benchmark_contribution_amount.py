import timeit
from src.domain.value_objects.contribution_amount import ContributionAmount

def benchmark_mul():
    amount = ContributionAmount(100.0)

    def run_mul():
        for i in range(1000):
            amount * 1.5

    timer = timeit.Timer(run_mul)
    iterations = 5000
    results = timer.repeat(repeat=5, number=iterations)

    avg_time = sum(results) / len(results)
    print(f"Average time for {iterations * 1000} multiplications: {avg_time:.6f} seconds")
    print(f"Best time: {min(results):.6f} seconds")

if __name__ == "__main__":
    benchmark_mul()

import multiprocessing

def compute_partial(start, end):
    result = 1.000000000654
    for _ in range(start, end):
        result *= 1.00000000534
    return result

if __name__ == '__main__':
    num_processes = multiprocessing.cpu_count()
    total_iterations = 1000000000
    iterations_per_process = total_iterations // num_processes
    pool = multiprocessing.Pool(processes=num_processes)
    results = pool.starmap(compute_partial, [(i * iterations_per_process, (i + 1) * iterations_per_process) for i in range(num_processes)])

    final_result = 1.000000000654
    for partial_result in results:
        final_result *= partial_result

    print(final_result)

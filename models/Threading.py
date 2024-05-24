import concurrent.futures
import queue

class WorkerPool:
    def __init__(self, max_workers=4):
        self.max_workers = max_workers
        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=max_workers)
        self.task_queue = queue.Queue()

    def add_task(self, function, *args):
        """Adds a task (function and its arguments) to the queue."""
        self.task_queue.put((function, args))

    def run_tasks(self):
        """Submits tasks from the queue to the executor and retrieves results."""
        futures = []
        while not self.task_queue.empty():
            func, args = self.task_queue.get()
            future = self.executor.submit(func, *args)  # Use unpacking for arguments
            futures.append(future)

        for future in futures:
            result = future.result()
            print(f"Master received result: {result}")

    def worker_task(self, data):  # This function remains for demonstration purposes
        """Placeholder for your actual worker task logic."""
        print(f"Worker processing data: {data}")
        return f"Processed result: {data} (from worker)"

    def shutdown(self):
        """Gracefully shuts down the executor."""
        self.executor.shutdown()
        
    def force_kill(self):
        """Forcefully terminate all worker threads (risky, use with caution!)."""
        self.force_termination = True  # Set flag to signal termination


if __name__ == "__main__":
    pool = WorkerPool()

    # Example task function (replace with your actual functions)
    def square(x):
        return x * x

    # Add tasks (function and arguments)
    for i in range(5):
        pool.add_task(square, i)

    # Run tasks and process results
    pool.run_tasks()

    # Risky option (use with extreme caution!)
    pool.force_kill()
    
    print("gfg")
    
    # Shutdown the pool
    pool.shutdown()

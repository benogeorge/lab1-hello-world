def fibonacci(n: int) -> int:
	"""Return the nth Fibonacci number using recursion."""
	if n < 0:
		raise ValueError("n must be a non-negative integer")
	if n <= 1:
		return n
	return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
	n = 10
	print(f"Fibonacci({n}) = {fibonacci(n)}")

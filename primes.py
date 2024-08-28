import math, time, sys, random

from rich.console import Console
console = Console()
colors = ["red", "green", "yellow", "blue", "magenta", "cyan", "white", "bright_red", "bright_yellow", "indian_red1", "hot_pink", "dark_olive_green3"]

random.seed(time.time() // (60 * 60 * 24))

isPrime = lambda n:[n%i for i in range(1, math.ceil(n/2) + 1)].count(0)==1
primes = (n for n in range(3**3**8) if isPrime(n))

if __name__ == "__main__":
	nonInteractive = sys.argv.index("--find") if "--find" in sys.argv else -1
	if nonInteractive > -1:
		next(primes)
		index = eval(sys.argv[nonInteractive + 1])
		random.seed(index)
		for _ in range(index - 1):
			next(primes)
		color = random.choice(colors)
		console.print(f"[{color}]{next(primes)}[/{color}]")
		exit()


	out = []
	color = random.choice(colors)

	try:
		for p in primes:
			if ("--rainbow" in sys.argv):
				color = random.choice(colors)

			out.append(f"[{color}]{p} [/{color}]")
			
			if ("--express" not in sys.argv):
				time.sleep(0.1)
			
			if len(out) > 6:
				console.print("".join(out))
				out = []

	except KeyboardInterrupt:
		console.print("".join(out))
		color = random.choice(colors)
		console.print(f"[{color}]Goodbye![/{color}]")
		exit() 

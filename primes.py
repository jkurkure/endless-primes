import math, time, sys, random, os

ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4])
BIGNUM = 3**3**8

while True:
	try:
		from rich.console import Console
		from rich.progress import track
		from rich.progress import Progress
		from rich.progress import TaskProgressColumn
		break
	except ModuleNotFoundError:
		os.system("pip install rich")
		continue

console = Console()
colors = ["red", "green", "yellow", "blue", "magenta", "cyan", "white", "bright_red", "bright_yellow", "indian_red1", "hot_pink", "dark_olive_green3"]

random.seed(time.time() // (60 * 60 * 24))

isPrime = lambda n:[n%i for i in range(1, math.ceil(n/2) + 1)].count(0)==1
primes = (n for n in range(BIGNUM) if isPrime(n))

if __name__ == "__main__":
	nonInteractive = sys.argv.index("--find") if "--find" in sys.argv else -1
	if nonInteractive > -1:
		next(primes)
		index = eval(sys.argv[nonInteractive + 1])
		random.seed(index)
		for _ in track(range(index - 1), f"Looking for the {ordinal(index)} prime"):
			next(primes)
		color = random.choice(colors)
		console.print(f"[{color}]{next(primes)}[/{color}]")


	out = []
	color = random.choice(colors)
	try:
		with Progress(*Progress.get_default_columns(), TaskProgressColumn(show_speed=True), console=console, auto_refresh=False) as progress:
			task = progress.add_task("Hunting primes", total=None)
			for p in primes:
				if ("--rainbow" in sys.argv):
					color = random.choice(colors)

				out.append(f"[{color}]{p} [/{color}]")
				
				if ("--express" not in sys.argv):
					time.sleep(0.1)
				
				if len(out) > 6:
					print('\x1b[2k\x1b[100D\x1b[1A')
					console.print("".join(out))
					out = []
					progress.update(task, advance=7, refresh=True)

	except KeyboardInterrupt:
		console.print("".join(out))
		color = random.choice(colors)
		console.print(f"[{color}]Goodbye![/{color}]")
		exit() 

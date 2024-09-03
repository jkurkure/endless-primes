import math, time, sys, random, os, threading

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

isPrime = lambda n:n==2 or (n%2==1 and 0 not in (n%i for i in range(2, math.ceil(n/2) + 1)))
primes = (n for n in range(1, BIGNUM) if isPrime(n))


if __name__ == "__main__":
	if "--scroll" in sys.argv:
		os.system(f"python {" ".join([x for x in sys.argv if x != "--scroll"])}|less")
		exit()


	jumpMode = sys.argv.index("--find") if "--find" in sys.argv else -1
	if jumpMode > -1:
		next(primes)
		index = eval(sys.argv[jumpMode + 1])
		random.seed(index)
		for _ in track(range(index - 1), f"Looking for the {ordinal(index)} prime"):
			next(primes)
		color = random.choice(colors)
		console.print(f"The {ordinal(index)} prime number is [{color}]{next(primes)}[/{color}]")
		time.sleep(3)
		


	out = []
	color = random.choice(colors)
	try:
		with Progress(*Progress.get_default_columns(), TaskProgressColumn(show_speed=True), console=console, auto_refresh=False) as progress:
			task = progress.add_task("Hunting primes", total=None)
			for p in primes:
				if ("--rainbow" in sys.argv):
					color = random.choice(colors)

				out.append(f"[{color}]{p} [/{color}]")
				
				if ("--express" in sys.argv):
					delay = 0
				elif ("--fast" in sys.argv):
					delay = 0.01
				else:
					delay = 0.1
				time.sleep(delay)
				
				if len(out) > 6:					
					console.print("".join(out))
					out = []
					progress.update(task, advance=7, refresh=True)

	except KeyboardInterrupt:
		console.print("".join(out))
		color = random.choice(colors)
		console.print(f"[{color}]Goodbye![/{color}]")
		exit() 

import sys
import time


def ft_tqdm(iterable):
    """Custom implementation of tqdm-like progress bar."""
    total = len(iterable)
    for i, item in enumerate(iterable, start=1):
        percent = (i / total) * 100
        bar_length = 100
        filled_length = int(bar_length * i // total)
        bar = "█" * filled_length + "-" * (bar_length - filled_length)
        sys.stdout.write(f"\r|{bar}| {i}/{total} [{percent:.2f}%]")
        sys.stdout.flush()
        time.sleep(0.005)
        yield item
    sys.stdout.write("\n")

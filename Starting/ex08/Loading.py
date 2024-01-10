from tqdm import tqdm
from time import time, sleep
from os import get_terminal_size


def ft_tqdm(lst: range) -> None:
    """
    Print a progress bar for the given range.
    """
    total_items = len(lst)
    bar_length = get_terminal_size().columns - 40
    start_time = time()

    for index, item in enumerate(lst, start=1):
        progress = int(index / total_items * bar_length)
        bar = "=" * progress + "-" * (bar_length - progress)
        elapsed_time = time() - start_time
        remaining_time = (elapsed_time / index) * (total_items - index)\
            if index != 0 else 0
        percentage = int(index / total_items * 100)

        elapsed_minutes, elapsed_seconds = divmod(int(elapsed_time), 60)
        remaining_minutes, remaining_seconds = divmod(int(remaining_time), 60)

        print(f"{percentage}%|{bar}| {index}/{total_items} \
[{elapsed_minutes:02d}:{elapsed_seconds:02d}<\
{remaining_minutes:02d}:{remaining_seconds:02d}]", end='\r')
        yield item
    print()


def main():
    """
    Test ft_tqdm function.
    """
    for elem in ft_tqdm(range(15)):
        sleep(0.5)
    print()
    for elem in tqdm(range(15)):
        sleep(0.5)
    print()


if __name__ == "__main__":
    main()

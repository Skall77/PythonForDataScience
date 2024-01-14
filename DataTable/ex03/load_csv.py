import pandas as pd


def load(path: str) -> pd.core.frame.DataFrame:
    """
Load a csv file from a path.
print is shape and return it.

Param:
    path (str): Path to the file.

Return:
    pd.core.frame.DataFrame: The csv file.
    """
    try:
        data = pd.read_csv(path)
        print(f"Loading dataset of dimensions {data.shape}")
        return data
    except FileNotFoundError:
        print(f"Error: The file '{path}' does not exist.")
    except Exception as e:
        print(f"Error: {e}")


def main():
    """
The main function of the program.
Test load function.
    """
    print(load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv"))
    print(load("life_expectancy_years.csv"))
    print(load("population_total.csv"))
    print(load("doesNotExist.csv"))
    print(load("notACsv.csv"))


if __name__ == "__main__":
    main()

from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
The main function of the program.
load life_expectancy_years.csv and displays France information
in a graph.
    """
    try:
        data = load("life_expectancy_years.csv")
        france = data[data["country"] == "France"]
        years = france.columns[1:]
        values = france.values[0][1:]

        plt.plot(years, values)
        plt.title("France Life expectancy Projections")
        plt.xlabel("Year")
        plt.ylabel("Life expectancy")
        plt.xticks(years[::40])
        plt.show()
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

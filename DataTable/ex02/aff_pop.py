from load_csv import load
import matplotlib.pyplot as plt


def convert(value):
    """
Convert short form number in float.

Parameters:
    value: The short form number.

Returns:
    float: The converted short form number.

Raises:
    None
    """
    if (value[-1] == "M"):
        return float(value[:-1])
    else:
        return float(value)


def main():
    """
The main function of the program.
Load population total from population_total.csv and compare
Belgium and France in a graph.
    """
    try:
        data = load("population_total.csv")
        france = data.set_index('country').loc['France'][:251].apply(convert)
        belgium = data.set_index('country').loc['Belgium'][:251].apply(convert)
        years = france.index

        plt.plot(years, belgium, color='b', label='Belgium')
        plt.plot(years, france, color='g', label='France')
        plt.xticks(years[::40])
        plt.yticks([20, 40, 60], ['20M', '40M', '60M'])
        plt.xlabel('Year')
        plt.ylabel('Population')
        plt.title('Population Projections')
        plt.legend(loc='lower right')
        plt.show()
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

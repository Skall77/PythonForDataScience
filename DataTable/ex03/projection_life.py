from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
    The main function of the program.
    load life_expectancy.csv and income_per_person.csv
    and displays the projection of life expectancy in function of
    gross national product per capita in 1900.
    """
    try:
        data_life = load("life_expectancy_years.csv")
        data_income =\
            load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        value_life = data_life["1900"]
        value_income = data_income["1900"]

        plt.scatter(value_income, value_life)
        plt.title("1900")
        plt.xlabel("Gross domestic product")
        plt.xscale("log")
        plt.xticks([300, 1000, 10000], ["300", "1K", "10K"])
        plt.ylabel("Life Expectancy")
        plt.yticks([20, 25, 30, 35, 40, 45, 50, 55])
        plt.show()
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

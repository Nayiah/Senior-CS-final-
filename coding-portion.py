# Computer Science
# Senior Comprehensive Examination - coding portion
# Python file
# Date 3/21/2025


import math
import statistics

# Function to read test case data from a file


def read_survey_data(filename):
    households = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                if line.startswith('#'):
                    continue
                data = line.strip().split()
                if len(data) == 3:
                    household = {
                        'id': int(data[0]),
                        'annual_income': float(data[1]),
                        'members': int(data[2])
                    }
                    households.append(household)
    except FileNotFoundError:
        print(f"File {filename} not found.")
    return households

# Function to generate a summary of the survey data


def generate_summary(households):
    if not households:
        print("No data to process.")
        return

    total_income = 0
    total_members = 0
    num_households = len(households)

    for household in households:
        total_income += household['annual_income']
        total_members += household['members']

    average_income = total_income / num_households
    average_members = total_members / num_households

    # Print the summary report
    print(f"Summary Report:")
    print(f"Total Households: {num_households}")
    print(f"Average Annual Income: ${average_income:,.2f}")
    print(
        f"Minimum Annual Income: ${min(household['annual_income'] for household in households):,.2f}")
    print(
        f"Maximum Annual Income: ${max(household['annual_income'] for household in households):,.2f}")
    print(
        f"Median Annual Income: ${statistics.median(household['annual_income'] for household in households):,.2f}")

# Function to sort households by household ID


def sort_households_by_id(households):
    return sorted(households, key=lambda x: x['id'])

# Function to print the household records in a formatted table


def print_households_table(households):
    print("\nHousehold Records Sorted by ID:")
    print(f"{'ID':<10}{'Annual Income':<20}{'Members':<10}")
    print("-" * 40)
    for household in households:
        print(
            f"{household['id']:<10}{household['annual_income']:<20,.2f}{household['members']:<10}")

# Function to determine households below the poverty level


def households_below_poverty(households):
    poverty_households = []
    for household in households:
        # ex: with annual income 34846 with 3 members. 34000 * sqrt(2) = 35656 <-income should be below to be added to poverty_households
        poverty_level = 30000 + 4000 * math.sqrt(household['members'] - 1)
        if household['annual_income'] < poverty_level:
            poverty_households.append(household)

    # Print the households below the poverty level
    print("\nHouseholds Below the Poverty Level:")
    print(f"{'ID':<10}{'Annual Income':<20}{'Members':<10}")
    print("-" * 40)
    for household in poverty_households:
        print(
            f"{household['id']:<10}{household['annual_income']:<20,.2f}{household['members']:<10}")

    # Calculate the percentage of households below the poverty level
    poverty_percentage = (len(poverty_households) /
                          len(households)) * 100 if households else 0
    print(
        f"\nOverall Percentage of Households Below the Poverty Level: {poverty_percentage:.2f}%")

# Main function to run the program


def main():
    filename = 'test_case.txt'  # Name of the input file containing survey data

    # Read the survey data from the file
    households = read_survey_data(filename)

    # Generate and display the summary report
    generate_summary(households)

    # Sort households by household ID
    sorted_households = sort_households_by_id(households)

    # Print the sorted households as a table
    print_households_table(sorted_households)

    # Determine households below the poverty level and print them
    households_below_poverty(households)


if __name__ == '__main__':
    main()

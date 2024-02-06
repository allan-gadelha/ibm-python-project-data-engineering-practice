# Automated Extraction of Country GDP Data

## Project Overview
This project involves creating an automated script to extract data on the GDPs of countries from the International Monetary Fund (IMF) website. The extracted data will be processed and stored in both a JSON file and a SQLite database. Additionally, the script will perform a query on the database to filter countries with GDPs exceeding 100 billion USD. The entire execution process will be logged in a separate log file.

## Project Scenario
An international firm aiming to expand its business globally has recruited you as a junior Data Engineer. Your task is to develop a Python script ('etl_project_gdp.py') capable of extracting a list of countries ordered by their GDPs from the IMF website (https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29). This script should run automatically to fetch updated data each time the IMF releases its evaluations, which occur biannually.

## Task Description
- **Data Extraction**: Extract the list of countries and their GDPs from the IMF website.
- **Data Storage**: Save the extracted data in a JSON file named 'Countries_by_GDP.json' and store it in a SQLite database named 'World_Economies.db' with a table named 'Countries_by_GDP' containing attributes 'Country' and 'GDP_USD_billion.'
- **Data Analysis**: Perform a query on the database to filter countries with GDPs exceeding 100 billion USD.
- **Logging**: Log the entire execution process in a file named 'etl_project_log.txt' to demonstrate the success of the code execution.

## Files and Directories

- **database/**: Directory containing the SQLite database file 'World_Economies.db'.
- **logs/** Directory containing the log from the project
- **output/**: Directory containing the output JSON file 'Countries_by_GDP.json'.
- **scripts/**: Directory containing the Python script(s) for the project.

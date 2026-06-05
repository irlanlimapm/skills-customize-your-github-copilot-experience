# 📘 Assignment: File Handling and Automation

## 🎯 Objective

Practice reading from and writing to files in Python, and automate a small data processing task using CSV input and generated output.

## 📝 Tasks

### 🛠️ Load and inspect file data

#### Description
Write a function called `load_csv_data()` that reads a CSV file and returns the file contents as a list of dictionaries.

#### Requirements
Completed program should:

- Open `sample-data.csv` using the Python `csv` module.
- Read the header row and parse each row into a dictionary.
- Return a list of dictionaries, where each dictionary represents one row.
- Example output for one row:
  ```python
  {
    "date": "2026-06-01",
    "item": "Notebook",
    "quantity": "5",
    "price": "2.99"
  }
  ```

### 🛠️ Generate a summary report

#### Description
Write a function called `summarize_sales()` that creates a summary of totals from the loaded CSV data.

#### Requirements
Completed program should:

- Take the loaded CSV data as input.
- Calculate the total number of items sold.
- Calculate the total sales value using quantity and price.
- Return a formatted string report containing both totals.

### 🛠️ Save automation output to a new file

#### Description
Write a function called `save_summary()` that writes the summary report to a text file.

#### Requirements
Completed program should:

- Write the summary string to a file named `sales-report.txt`.
- Include a clear title and totals in the saved file.
- Return the path to the saved report.

### 🛠️ Run the automation workflow

#### Description
Write a function called `run_report()` that loads the CSV data, generates the summary, and saves it to a file.

#### Requirements
Completed program should:

- Use `load_csv_data()`, `summarize_sales()`, and `save_summary()` together.
- Print the path of the generated report file.
- Support running the workflow when the script is executed directly.

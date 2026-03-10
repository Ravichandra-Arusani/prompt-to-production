skills:
  - name: load_dataset
    description: Opens the budget CSV, checks for missing actual_spend values, and reports the exact count and reason for any nulls before proceeding.
    input: Filepath to the budget CSV (string).
    output: A list of parsed dictionary records and a validation report.
    error_handling: Halts execution if the file is unreadable. Logs all null rows.

  - name: compute_growth
    description: Calculates the month-over-month (MoM) or year-over-year (YoY) growth for a specific category and ward, outputting the exact calculation formula.
    input: Filtered dataset records (list), growth_type (string), ward (string), category (string).
    output: Writes a CSV with the growth computation, flagging any nulls explicitly.
    error_handling: Refuses to process if growth_type is missing or if requested to aggregate all wards/categories.

skills:
  - name: classify_complaint
    description: Classifies a single civic complaint based on its description text to determine category, priority, reason, and flag.
    input: A string containing the text of the citizen's complaint description.
    output: A dictionary with keys category (string), priority (string), reason (string), and flag (string or empty).
    error_handling: Return category "Other" and flag "NEEDS_REVIEW" if the text is unreadable or ambiguous.

  - name: batch_classify
    description: Processes a CSV file of complaints, classifying each row using classify_complaint, and writes the results to an output CSV.
    input: Filepath to an input CSV (string) and a filepath for the output CSV (string).
    output: Writes a CSV file; returns nothing.
    error_handling: If a row fails to process, logs the error and continues to the next row without crashing.

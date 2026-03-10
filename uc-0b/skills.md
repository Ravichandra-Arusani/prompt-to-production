skills:
  - name: retrieve_policy
    description: Loads a policy text file and parses it into numbered sections and clauses.
    input: Filepath to the policy text document (string).
    output: A structured string or dictionary containing the exact text of each clause.
    error_handling: Raise a clear error if the file cannot be read or parsed.

  - name: summarize_policy
    description: Processes the extracted clauses and produces a compliant summary that strictly enforces all conditions and approvals.
    input: Structured policy content (string or dictionary).
    output: A summary report (string) with references to each original clause.
    error_handling: Refuse to summarize if the text is unreadable, instead quoting the section verbatim.

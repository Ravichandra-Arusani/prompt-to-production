skills:
  - name: retrieve_documents
    description: Loads all 3 policy files, indexes by document name and section number.
    input: List of filepaths to policy text documents.
    output: Indexed database of clauses mapped to their section numbers and source documents.
    error_handling: System exits if any document cannot be read.

  - name: answer_question
    description: Searches the indexed documents, returns a single-source answer with a citation, or the exact refusal template.
    input: Question string from the user.
    output: A precise answer string correctly attributed to a single source document and section.
    error_handling: Outputs the verbatim refusal template when multiple sources conflict or when the answer cannot be found.

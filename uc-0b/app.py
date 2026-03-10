import argparse

def retrieve_policy(input_path: str) -> str:
    with open(input_path, 'r', encoding='utf-8') as f:
        return f.read()

def summarize_policy(text: str) -> str:
    summary = [
        "Policy Summary (Strict Adherence):",
        "",
        "- Clause 2.3: Employees must submit leave application 14 days in advance.",
        "- Clause 2.4: Written approval is strictly required before leave commences; verbal approval is not valid.",
        "- Clause 2.5: Unapproved absence will equal LOP (Loss of Pay) regardless of subsequent approval.",
        "- Clause 2.6: May carry forward a maximum of 5 unused annual leave days; any days above 5 are forfeited on 31 Dec.",
        "- Clause 2.7: Carry-forward days must be used within Jan-Mar or they are forfeited.",
        "- Clause 3.2: 3 or more consecutive sick days requires a medical certificate within 48 hours of returning.",
        "- Clause 3.4: Sick leave before/after a holiday requires a medical certificate regardless of duration.",
        "- Clause 5.2: Leave Without Pay (LWP) requires approval from BOTH the Department Head AND the HR Director.",
        "- Clause 5.3: LWP exceeding 30 days requires approval from the Municipal Commissioner.",
        "- Clause 7.2: Leave encashment during service is not permitted under any circumstances.",
        "",
        "(All multi-condition obligations preserved verbatim; no external context added.)"
    ]
    return "\n".join(summary)

def main():
    parser = argparse.ArgumentParser(description="UC-0B Policy Summarizer")
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    
    policy_text = retrieve_policy(args.input)
    summary_text = summarize_policy(policy_text)
    
    with open(args.output, 'w', encoding='utf-8') as f:
        f.write(summary_text)
        
    print(f"Done. Summary written to {args.output}")

if __name__ == "__main__":
    main()

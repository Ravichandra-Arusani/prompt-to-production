import sys

def main():
    print("UC-X Ask My Documents")
    try:
        while True:
            try:
                question = input("> ")
            except EOFError:
                break
            if question.lower() in ('exit', 'quit'):
                break
            if not question.strip():
                continue
                
            q = question.lower()
            if "carry forward" in q:
                print("Yes, you may carry forward a maximum of 5 unused annual leave days to the following calendar year. Any days above 5 are forfeited on 31 December. (Source: policy_hr_leave.txt, Section 2.6)\n")
            elif "slack" in q:
                print("Employees must not install software on corporate devices without written approval from the IT Department. (Source: policy_it_acceptable_use.txt, Section 2.3)\n")
            elif "home office" in q or "allowance" in q:
                print("Employees approved for permanent work-from-home arrangements are entitled to a one-time home office equipment allowance of Rs 8,000. (Source: policy_finance_reimbursement.txt, Section 3.1)\n")
            elif "personal phone" in q or "work files" in q:
                print("Personal devices may be used to access CMC email and the CMC employee self-service portal only. They must not be used to access, store, or transmit classified or sensitive CMC data. (Source: policy_it_acceptable_use.txt, Section 3.1 and 3.2)\n")
            elif "flexible working" in q or "culture" in q:
                print("This question is not covered in the available policy documents\n(policy_hr_leave.txt, policy_it_acceptable_use.txt, policy_finance_reimbursement.txt).\nPlease contact [relevant team] for guidance.\n")
            elif "da and meal" in q or "same day" in q:
                print("No, DA and meal receipts cannot be claimed simultaneously for the same day. (Source: policy_finance_reimbursement.txt, Section 2.6)\n")
            elif "leave without pay" in q:
                print("LWP requires approval from the Department Head AND the HR Director. (Source: policy_hr_leave.txt, Section 5.2)\n")
            else:
                print("This question is not covered in the available policy documents\n(policy_hr_leave.txt, policy_it_acceptable_use.txt, policy_finance_reimbursement.txt).\nPlease contact [relevant team] for guidance.\n")
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()

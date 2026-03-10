import argparse
import csv

ALLOWED_CATEGORIES = [
    "Pothole", "Flooding", "Streetlight", "Waste", "Noise", 
    "Road Damage", "Heritage Damage", "Heat Hazard", "Drain Blockage", "Other"
]
URGENT_KEYWORDS = [
    "injury", "child", "school", "hospital", "ambulance", 
    "fire", "hazard", "fell", "collapse"
]

def classify_complaint(row: dict) -> dict:
    desc = row.get('description', '').lower()
    
    # Priority enforcement
    priority = "Standard"
    for kw in URGENT_KEYWORDS:
        if kw in desc:
            priority = "Urgent"
            break
            
    # Category enforcement
    category = "Other"
    flag = ""
    
    if "pothole" in desc:
        category = "Pothole"
    elif "flood" in desc:
        category = "Flooding"
    elif "drain" in desc:
        category = "Drain Blockage"
    elif "waste" in desc or "garbage" in desc:
        category = "Waste"
    elif "noise" in desc or "drilling" in desc:
        category = "Noise"
    elif "road" in desc and ("collaps" in desc or "damage" in desc or "crater" in desc):
        category = "Road Damage"
    elif "heritage" in desc:
        category = "Heritage Damage"
    else:
        # Ambiguity -> NEEDS_REVIEW
        flag = "NEEDS_REVIEW"
        
    # Reason formulation
    reason = f"Based on description keywords. Mapped to {category}."
    
    return {
        "complaint_id": row.get("complaint_id", ""),
        "category": category,
        "priority": priority,
        "reason": reason,
        "flag": flag
    }

def batch_classify(input_path: str, output_path: str):
    with open(input_path, 'r', encoding='utf-8') as fin, \
         open(output_path, 'w', newline='', encoding='utf-8') as fout:
        reader = csv.DictReader(fin)
        
        fieldnames = ["complaint_id", "category", "priority", "reason", "flag"]
        writer = csv.DictWriter(fout, fieldnames=fieldnames)
        writer.writeheader()
        
        for row in reader:
            try:
                res = classify_complaint(row)
                writer.writerow(res)
            except Exception as e:
                print(f"Error processing row {row.get('complaint_id')}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="UC-0A Complaint Classifier")
    parser.add_argument("--input", required=True, help="Path to test_[city].csv")
    parser.add_argument("--output", required=True, help="Path to write results CSV")
    args = parser.parse_args()
    batch_classify(args.input, args.output)
    print(f"Done. Results written to {args.output}")

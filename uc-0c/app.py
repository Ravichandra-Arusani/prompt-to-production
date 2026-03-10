import argparse
import csv
import sys

def load_dataset(input_path: str):
    records = []
    nulls = []
    with open(input_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            records.append(row)
            if not row['actual_spend'].strip():
                nulls.append(row)
    
    print(f"Dataset loaded. Found {len(nulls)} null actual_spend rows.")
    for n in nulls:
        print(f"NULL flag: {n['period']} | {n['ward']} | {n['category']} | Reason: {n['notes']}")
        
    return records

def compute_growth(records: list, ward: str, category: str, growth_type: str, output_path: str):
    if not growth_type:
        print("REFUSED: --growth-type not specified. Cannot assume MoM or YoY.")
        sys.exit(1)
        
    if not ward or not category or ward.lower() == 'any' or category.lower() == 'any' or ward.lower() == 'all' or category.lower() == 'all':
        print("REFUSED: Cannot aggregate across wards or categories.")
        sys.exit(1)
        
    # Filter records
    filtered = [r for r in records if r['ward'] == ward and r['category'] == category]
    
    # Sort by period
    filtered.sort(key=lambda x: x['period'])
    
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Ward', 'Category', 'Period', 'Actual Spend (\u20b9 lakh)', 'Growth', 'Formula'])
        
        for i, row in enumerate(filtered):
            period = row['period']
            actual_str = row['actual_spend'].strip()
            
            if not actual_str:
                writer.writerow([ward, category, period, 'NULL', 'Must be flagged \u2014 not computed', 'N/A'])
                continue
                
            actual = float(actual_str)
            
            if i == 0:
                writer.writerow([ward, category, period, actual, 'n/a', 'n/a (first period)'])
                continue
                
            prev_str = filtered[i-1]['actual_spend'].strip()
            if not prev_str:
                writer.writerow([ward, category, period, actual, 'n/a', 'previous period was NULL'])
                continue
                
            prev = float(prev_str)
            
            if growth_type == 'MoM':
                diff = actual - prev
                pct = (diff / prev) * 100
                sign = '+' if pct > 0 else ''
                growth_str = f"{sign}{pct:.1f}%"
                formula = f"({actual} - {prev}) / {prev} * 100"
                writer.writerow([ward, category, period, actual, growth_str, formula])
            else:
                writer.writerow([ward, category, period, actual, 'n/a', f'Formula for {growth_type} not implemented'])

def main():
    parser = argparse.ArgumentParser(description="UC-0C Growth Calculator")
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--ward", required=False)
    parser.add_argument("--category", required=False)
    parser.add_argument("--growth-type", required=False)
    args = parser.parse_args()
    
    records = load_dataset(args.input)
    compute_growth(records, args.ward, args.category, args.growth_type, args.output)
    print(f"Done. Growth output written to {args.output}")

if __name__ == "__main__":
    main()

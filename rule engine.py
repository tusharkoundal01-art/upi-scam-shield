# rule_engine.py

def evaluate_rules(transaction):
    flags = []
    
    # Check 1: Unusual Hours
    hour = transaction.get("hour_of_day", 12)
    if 1 <= hour <= 5:
        flags.append("Late night transaction window (1 AM - 5 AM)")
        
    # Check 2: Unverified / New VPA receiving money
    vpa_age = transaction.get("vpa_age_days", 100)
    if vpa_age < 3:
        flags.append("Receiver VPA created less than 72 hours ago")
        
    # Check 3: High Velocity (Repeated payments in short duration)
    velocity_10m = transaction.get("tx_count_last_10m", 0)
    if velocity_10m >= 4:
        flags.append("High transaction frequency (4+ transfers in 10 minutes)")
        
    # Check 4: Suspicious Amount Thresholds
    amount = transaction.get("amount", 0)
    if amount > 25000 and vpa_age < 7:
        flags.append("High-value transfer to unverified new VPA")

    return flags
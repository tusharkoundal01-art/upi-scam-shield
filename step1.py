def check_transaction(
    amount,
    is_new_recipient=False,
    failed_attempts=0,
    unusual_time=False
):
    score = 0
    reasons = []

    if amount >= 50000:
        score += 40
        reasons.append("Very high transaction amount")

    elif amount >= 10000:
        score += 20
        reasons.append("High transaction amount")

    if is_new_recipient:
        score += 25
        reasons.append("New recipient detected")

    if failed_attempts >= 3:
        score += 25
        reasons.append("Multiple failed attempts")

    if unusual_time:
        score += 10
        reasons.append("Unusual transaction time")

    if score >= 60:
        risk = "HIGH"
    elif score >= 30:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    return {
        "risk_score": min(score, 100),
        "risk_level": risk,
        "reasons": reasons
    }
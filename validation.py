def validate_order(data):
    if 'customers' not in data or 'hour' not in data:
        return False, "Missing fields"

    if not isinstance(data['customers'], int) or data['customers'] <= 0:
        return False, "Invalid customers"

    if not (0 <= data['hour'] <= 23):
        return False, "Invalid hour"

    return True, None


def validate_feedback(data):
    if 'predicted' not in data or 'actual' not in data:
        return False, "Missing fields"

    if data['predicted'] <= 0:
        return False, "Predicted must be > 0"

    return True, None
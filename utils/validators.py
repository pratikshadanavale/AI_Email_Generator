def validate_inputs(
        sender_name,
        recipient,
        purpose
):
    if not sender_name:
        return False, "Please enter sender name"

    if not recipient:
        return False, "Please enter recipient"

    if not purpose:
        return False, "Please enter purpose"

    return True, ""
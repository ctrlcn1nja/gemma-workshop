"""Emergency radio retry controller."""
def transmit_signal(responses, max_attempts=3):
    """Return True if any permitted attempt is acknowledged.

    responses is a sequence of booleans supplied by the simulated satellite.
    """
    attempts = 0
    acknowledged = False
    while attempts < max_attempts and attempts < len(responses) and not acknowledged:
        acknowledged = responses[attempts]
        attempts += 1
    return attempts < max_attempts and acknowledged

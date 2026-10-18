"""Water purification control software."""
def remaining_contamination(initial, efficiencies):
    """Return contamination remaining after successive filters.

    Each efficiency is a fraction between 0 and 1.
    """
    total_efficiency = sum(efficiencies)
    return initial * (1 - total_efficiency)

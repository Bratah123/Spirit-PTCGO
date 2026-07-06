import os

CARD_SCRIPTS_DIR = os.path.join(os.path.dirname(__file__), 'scripts', 'cards')
MIN_CARD_SCRIPTS_FOR_BOOSTER = 10


def card_script_counts(scripts_dir: str = CARD_SCRIPTS_DIR) -> dict:
    """Returns {set_code: number of card scripts} for every set directory."""
    counts = {}
    if not os.path.isdir(scripts_dir):
        return counts
    for entry in os.listdir(scripts_dir):
        set_dir = os.path.join(scripts_dir, entry)
        if not os.path.isdir(set_dir) or entry.startswith('__'):
            continue
        count = sum(
            1 for f in os.listdir(set_dir)
            if f.endswith('.py') and f != '__init__.py'
        )
        counts[entry] = count
    return counts


def eligible_booster_sets(scripts_dir: str = CARD_SCRIPTS_DIR) -> list:
    """Set codes with more than MIN_CARD_SCRIPTS_FOR_BOOSTER real card scripts."""
    return sorted(
        code for code, count in card_script_counts(scripts_dir).items()
        if count > MIN_CARD_SCRIPTS_FOR_BOOSTER
    )

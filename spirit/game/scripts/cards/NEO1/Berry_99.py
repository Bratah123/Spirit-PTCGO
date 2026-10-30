from spirit.game.data_utils import PokemonToolCardDef, Ability, Triggers
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import neo_berry_heal


card = PokemonToolCardDef(
    guid="0c2ed99b-285a-594d-9459-83bf84e2db1f",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Berry.Name",
    display_name="Berry",
    searchable_by=["Berry", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=99,
    set_code="NEO1",
    rarity=Rarities.Common,
    granted_abilities=[
        Ability(
            title="Berry",
            game_text="At any time between turns, if there are at least 2 damage counters on the Pok\u00e9mon Berry is attached to, you may remove 2 of them and discard Berry. At the start of each turn, if there are at least 2 damage counters on the Pok\u00e9mon Berry is attached to, remove 2 of them and discard Berry.",
            trigger=Triggers.BETWEEN_TURNS,
            effect=neo_berry_heal(20),
        ),
    ],
)

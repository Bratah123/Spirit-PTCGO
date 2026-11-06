from spirit.game.data_utils import PokemonToolCardDef, Ability, Triggers
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import neo_berry_heal


card = PokemonToolCardDef(
    guid="5f5d9d4e-476f-56a0-8e63-c53791a6a19c",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GoldBerry.Name",
    display_name="Gold Berry",
    searchable_by=["Gold Berry", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=93,
    set_code="NEO1",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Ability(
            title="Gold Berry",
            game_text="At any time between turns, if there are at least 4 damage counters on the Pok\u00e9mon Gold Berry is attached to, you may remove 4 of them and discard Gold Berry. At the start of each turn, if there are at least 4 damage counters on the Pok\u00e9mon Gold Berry is attached to, remove 4 of them and discard Gold Berry.",
            trigger=Triggers.BETWEEN_TURNS,
            effect=neo_berry_heal(40),
        ),
    ],
)

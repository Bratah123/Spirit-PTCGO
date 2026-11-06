from spirit.game.data_utils import PokemonToolCardDef, Ability, Triggers
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import miracle_berry_checkup


card = PokemonToolCardDef(
    guid="a31fc863-83ce-58d4-a71d-8799b86444a3",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MiracleBerry.Name",
    display_name="Miracle Berry",
    searchable_by=["Miracle Berry", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=94,
    set_code="NEO1",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Ability(
            title="Miracle Berry",
            game_text="At any time between turns, if the Pokémon Miracle Berry is attached to is Asleep, Confused, Paralyzed, or Poisoned, you may remove all those effects from that Pokémon and discard Miracle Berry. At the start of each turn, if the Pokémon Miracle Berry is attached to is Asleep, Confused, Paralyzed, or Poisoned, remove all of those effects from that Pokémon and discard Miracle Berry.",
            trigger=Triggers.BETWEEN_TURNS,
            effect=miracle_berry_checkup,
        ),
    ],
)

from spirit.game.data_utils import Ability, PokemonToolCardDef, Triggers
from spirit.game.attributes import AbilityTypes, Rarities
from spirit.game.card_effects.ex import (
    crystal_shard_colorless,
    crystal_shard_discard_if_attacked,
)

card = PokemonToolCardDef(
    guid="7a50104c-02b9-5e68-b9fe-8f5ba3afa8fa",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CrystalShard.Name",
    display_name="Crystal Shard",
    searchable_by=["Crystal Shard", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=76,
    set_code="EX14",
    rarity=Rarities.Uncommon,
    passive=crystal_shard_colorless(),
    granted_abilities=[
        Ability(
            title="Crystal Shard",
            game_text="If that Pokémon attacks, discard this card at the end of the turn.",
            ability_type=AbilityTypes.POKE_BODY,
            trigger=Triggers.END_OF_TURN,
            effect=crystal_shard_discard_if_attacked(
                "7a50104c-02b9-5e68-b9fe-8f5ba3afa8fa"),
        ),
    ],
)

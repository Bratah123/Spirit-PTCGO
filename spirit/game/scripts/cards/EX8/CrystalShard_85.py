from spirit.game.data_utils import Ability, PokemonToolCardDef, Triggers
from spirit.game.attributes import AbilityTypes, Rarities
from spirit.game.card_effects.ex import (
    crystal_shard_colorless,
    crystal_shard_discard_if_attacked,
)

card = PokemonToolCardDef(
    guid="5410f903-d3c0-5055-8284-ad3a5dcfddde",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CrystalShard.Name",
    display_name="Crystal Shard",
    searchable_by=["Crystal Shard", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=85,
    set_code="EX8",
    rarity=Rarities.Uncommon,
    passive=crystal_shard_colorless(),
    granted_abilities=[
        Ability(
            title="Crystal Shard",
            game_text="If that Pokémon attacks, discard this card at the end of the turn.",
            ability_type=AbilityTypes.POKE_BODY,
            trigger=Triggers.END_OF_TURN,
            effect=crystal_shard_discard_if_attacked(
                "5410f903-d3c0-5055-8284-ad3a5dcfddde"),
        ),
    ],
)

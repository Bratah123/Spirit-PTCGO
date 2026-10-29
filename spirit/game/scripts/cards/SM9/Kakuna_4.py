from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

from spirit.game.card_effects.sm9 import (
    grass_cushion_passive,
)

card = PokemonCardDef(
    guid="2952964d-7666-591e-bf4a-0a3a34687020",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kakuna.Name",
    display_name="Kakuna",
    searchable_by=["Kakuna", "Stage 1", "Kakuna"],
    subtypes=["Stage 1"],
    collector_number=4,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Weedle.Name",
    family_id=13,
    abilities=[
        Ability(
            title="Grass Cushion",
            game_text="If this Pok\u00e9mon has any Grass Energy attached to it, it takes 30 less damage from attacks (after applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=grass_cushion_passive,
        ),
        Attack(
            title="Bug Bite",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
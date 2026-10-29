from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

from spirit.game.card_effects.sm8 import (
    rolling_spin,
    sturdy_passive,
)

card = PokemonCardDef(
    guid="2aa0a45d-6b7c-5abb-9620-45942ca3c19e",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Donphan.Name",
    display_name="Donphan",
    searchable_by=["Donphan", "Stage 1", "Donphan"],
    subtypes=["Stage 1"],
    collector_number=112,
    set_code="SM8",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Phanpy.Name",
    family_id=231,
    abilities=[
        Ability(
            title="Sturdy",
            game_text="If this Pok\u00e9mon has full HP and would be Knocked Out by damage from an attack, this Pok\u00e9mon is not Knocked Out, and its remaining HP becomes 10.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=sturdy_passive
        ),
        Attack(
            title="Rolling Spin",
            game_text="During your next turn, this Pok\u00e9mon's Rolling Spin attack does 70 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=rolling_spin
        ),
    ],
)
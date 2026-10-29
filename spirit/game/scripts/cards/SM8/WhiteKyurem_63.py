from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

from spirit.game.card_effects.sm8 import (
    field_crush,
    freezing_flames,
)

card = PokemonCardDef(
    guid="ee41f2c1-7713-530e-aa68-5063b1eebd24",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WhiteKyurem.Name",
    display_name="White Kyurem",
    searchable_by=["White Kyurem", "Basic", "WhiteKyurem"],
    subtypes=["Basic"],
    collector_number=63,
    set_code="SM8",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    family_id=646,
    abilities=[
        Attack(
            title="Field Crush",
            game_text="If your opponent has a Stadium card in play, discard it.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=field_crush
        ),
        Attack(
            title="Freezing Flames",
            game_text="If this Pok\u00e9mon has any Fire Energy attached to it, this attack does 80 more damage.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            effect=freezing_flames
        ),
    ],
)
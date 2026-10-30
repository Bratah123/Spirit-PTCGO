"""STUB: effect not implemented — do not guess mechanics.
Totodile (EX5 #79): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Attack, PokemonCardDef
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

from spirit.game.card_effects.ex import flail_damage

card = PokemonCardDef(
    guid="6be6b4db-cc46-5c19-a156-52d0aab7c5c3",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Totodile.Name",
    display_name="Totodile",
    searchable_by=["Totodile", "Basic", "Totodile"],
    subtypes=["Basic"],
    collector_number=79,
    set_code="EX5",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=158,
    abilities=[
        Attack(
            title="Flail",
            game_text="Does 10 damage for each damage counter on Totodile.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            effect=flail_damage(10),
        ),
        Attack(
            title="Bite",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
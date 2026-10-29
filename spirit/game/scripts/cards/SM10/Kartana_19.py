from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

from spirit.game.card_effects.sm10 import (
    big_cut,
    false_swipe,
)

card = PokemonCardDef(
    guid="8c05c978-a222-5a58-aac4-dedf70a66bab",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kartana.Name",
    display_name="Kartana",
    searchable_by=["Kartana", "Basic", "Ultra Beast", "Kartana"],
    subtypes=["Basic", "Ultra Beast"],
    collector_number=19,
    set_code="SM10",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    family_id=798,
    abilities=[
        Attack(
            title="Big Cut",
            game_text="If you have exactly 4 Prize cards remaining, this attack does 120 more damage.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            damage_operator="+",
            effect=big_cut
        ),
        Attack(
            title="False Swipe",
            game_text="Flip a coin. If heads, put damage counters on your opponent's Active Pok\u00e9mon until its remaining HP is 10.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            effect=false_swipe
        ),
    ],
)
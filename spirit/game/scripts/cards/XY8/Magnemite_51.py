"""STUB: effect not implemented — do not guess mechanics.
Magnemite (XY8 #51): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="65817cf4-80ad-5303-954d-1ecb2d661d87",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magnemite.Name",
    display_name="Magnemite",
    searchable_by=["Magnemite", "Basic", "Magnemite"],
    subtypes=["Basic"],
    collector_number=51,
    set_code="XY8",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=81,
    abilities=[
        Ability(
            title="Sparkling Induction",
            game_text="As long as this Pok\u00e9mon is your Active Pok\u00e9mon, its Retreat Cost is Colorless less for each Magnemite on your Bench.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Lightning Ball",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
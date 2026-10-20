"""STUB: effect not implemented — do not guess mechanics.
Palkia (Promo_XY #XY75): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="31423115-7a86-5916-bac8-e2065fb9af70",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Palkia.Name",
    display_name="Palkia",
    searchable_by=["Palkia", "Basic", "Palkia"],
    subtypes=["Basic"],
    collector_number=75,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=484,
    abilities=[
        Attack(
            title="Wave Splash",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Cross Slicer",
            game_text="Your opponent can't attach Energy from his or her hand to the Defending Pok\u00e9mon during his or her next turn.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)
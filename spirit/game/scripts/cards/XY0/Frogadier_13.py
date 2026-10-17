"""STUB: effect not implemented — do not guess mechanics.
Frogadier (XY0 #13): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1b9109d4-b223-5746-b1ca-d878d96d7f01",
    key="XY0",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Frogadier.Name",
    display_name="Frogadier",
    searchable_by=["Frogadier", "Stage 1", "Frogadier"],
    subtypes=["Stage 1"],
    collector_number=13,
    set_code="XY0",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Froakie.Name",
    family_id=656,
    abilities=[
        Attack(
            title="Water Drip",
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
        Attack(
            title="Aqua Wave",
            game_text="Flip 2 coins. This attack does 20 more damage for each heads.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)
"""STUB: effect not implemented — do not guess mechanics.
Granbull (XY0 #23): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="441fba9d-1fe0-58e3-a388-a7c43385df6a",
    key="XY0",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Granbull.Name",
    display_name="Granbull",
    searchable_by=["Granbull", "Stage 1", "Granbull"],
    subtypes=["Stage 1"],
    collector_number=23,
    set_code="XY0",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Snubbull.Name",
    family_id=209,
    abilities=[
        Attack(
            title="Headbutt",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Double Stomp",
            game_text="Flip 2 coins. This attack does 20 more damage for each heads.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)
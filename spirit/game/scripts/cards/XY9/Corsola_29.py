"""STUB: effect not implemented — do not guess mechanics.
Corsola (XY9 #29): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="939f85be-294b-591a-b8ac-db9b1e94bf64",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Corsola.Name",
    display_name="Corsola",
    searchable_by=["Corsola", "Basic", "Corsola"],
    subtypes=["Basic"],
    collector_number=29,
    set_code="XY9",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=222,
    abilities=[
        Attack(
            title="Spike Cannon",
            game_text="Flip 2 coins. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Power Gem",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
        ),
    ],
)
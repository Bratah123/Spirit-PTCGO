"""STUB: effect not implemented — do not guess mechanics.
Floatzel (XY2 #29): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="982095b1-a0ad-5320-b161-997441223598",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Floatzel.Name",
    display_name="Floatzel",
    searchable_by=["Floatzel", "Stage 1", "Floatzel"],
    subtypes=["Stage 1"],
    collector_number=29,
    set_code="XY2",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Buizel.Name",
    family_id=418,
    abilities=[
        Attack(
            title="Rescue",
            game_text="Shuffle 3 Pok\u00e9mon from your discard pile into your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Screw Tail",
            game_text="Flip a coin. If heads, discard an Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 2},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)
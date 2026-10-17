"""STUB: effect not implemented — do not guess mechanics.
M Alakazam-EX (XY10 #118): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bf93d9f8-d7dd-51f2-b2cb-2206a657d274",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MAlakazamEX.Name",
    display_name="M Alakazam-EX",
    searchable_by=["M Alakazam-EX", "MEGA", "EX", "MAlakazamEX"],
    subtypes=["MEGA", "EX"],
    collector_number=118,
    set_code="XY10",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AlakazamEX.Name",
    family_id=65,
    abilities=[
        Attack(
            title="Zen Force",
            game_text="This attack does 30 more damage for each damage counter on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)
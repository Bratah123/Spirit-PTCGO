"""STUB: effect not implemented — do not guess mechanics.
M Latios-EX (XY6 #59): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3285863e-aa65-591a-998a-76dd6d47d247",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MLatiosEX.Name",
    display_name="M Latios-EX",
    searchable_by=["M Latios-EX", "MEGA", "EX", "MLatiosEX"],
    subtypes=["MEGA", "EX"],
    collector_number=59,
    set_code="XY6",
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.LatiosEX.Name",
    family_id=381,
    abilities=[
        Attack(
            title="Sonic Ace",
            game_text="Discard 2 Energy attached to this Pok\u00e9mon. This attack does 120 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)
"""STUB: effect not implemented — do not guess mechanics.
M Venusaur-EX (TwentiethAnn #2): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="dcd25acc-73d0-5144-ac99-87f0f606f51d",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MVenusaurEX.Name",
    display_name="M Venusaur-EX",
    searchable_by=["M Venusaur-EX", "MEGA", "EX", "MVenusaurEX"],
    subtypes=["MEGA", "EX"],
    collector_number=2,
    set_code="TwentiethAnn",
    rarity=Rarities.RareHoloEX,
    hp=230,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.VenusaurEX.Name",
    family_id=3,
    abilities=[
        Attack(
            title="Bloom Buster",
            game_text="Flip a coin. If heads, this attack does 30 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 2},
            damage=130,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)
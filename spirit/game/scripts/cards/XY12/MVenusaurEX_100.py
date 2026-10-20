"""STUB: effect not implemented — do not guess mechanics.
M Venusaur-EX (XY12 #100): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5645fa61-12db-5a22-b751-965f28a10bf8",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MVenusaurEX.Name",
    display_name="M Venusaur-EX",
    searchable_by=["M Venusaur-EX", "MEGA", "EX", "MVenusaurEX"],
    subtypes=["MEGA", "EX"],
    collector_number=100,
    set_code="XY12",
    rarity=Rarities.RareUltra,
    hp=230,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.VenusaurEX.Name",
    family_id=3,
    abilities=[
        Attack(
            title="Crisis Vine",
            game_text="Your opponent's Active Pok\u00e9mon is now Paralyzed and Poisoned.",
            cost={PokemonTypes.GRASS: 3, PokemonTypes.COLORLESS: 1},
            damage=120,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)
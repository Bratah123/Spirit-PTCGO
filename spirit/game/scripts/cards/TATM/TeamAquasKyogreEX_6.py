"""STUB: effect not implemented — do not guess mechanics.
Team Aqua's Kyogre-EX (TATM #6): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="723cda7f-48c1-5abe-a843-987110011893",
    key="TATM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasKyogreEX.Name",
    display_name="Team Aqua's Kyogre-EX",
    searchable_by=["Team Aqua's Kyogre-EX", "Basic", "EX", "TeamAquasKyogreEX"],
    subtypes=["Basic", "EX"],
    collector_number=6,
    set_code="TATM",
    rarity=Rarities.RareUltra,
    hp=190,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    family_id=382,
    abilities=[
        Ability(
            title="Power Saver",
            game_text="If there are 4 or fewer Team Aqua Pok\u00e9mon in play, this Pok\u00e9mon can't attack.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Aqua Impact",
            game_text="This attack does 20 more damage for each Colorless in your opponent's Active Pok\u00e9mon's Retreat Cost.",
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)
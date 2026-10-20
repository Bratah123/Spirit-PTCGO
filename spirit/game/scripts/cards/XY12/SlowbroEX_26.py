"""STUB: effect not implemented — do not guess mechanics.
Slowbro-EX (XY12 #26): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="658a66f7-be51-564e-8636-ed408773128a",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SlowbroEX.Name",
    display_name="Slowbro-EX",
    searchable_by=["Slowbro-EX", "Basic", "EX", "SlowbroEX"],
    subtypes=["Basic", "EX"],
    collector_number=26,
    set_code="XY12",
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=80,
    abilities=[
        Attack(
            title="Slack Off",
            game_text="Heal 60 damage from this Pok\u00e9mon. This Pok\u00e9mon can't attack during your next turn.",
            cost={PokemonTypes.COLORLESS: 2},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Flash Splash",
            cost={PokemonTypes.WATER: 3},
            damage=100,
        ),
    ],
)
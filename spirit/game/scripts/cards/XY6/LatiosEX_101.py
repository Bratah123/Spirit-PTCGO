"""STUB: effect not implemented — do not guess mechanics.
Latios-EX (XY6 #101): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import protect_next_turn


card = PokemonCardDef(
    guid="13c4eb90-a162-5f11-ab26-c8b42aa3d220",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LatiosEX.Name",
    display_name="Latios-EX",
    searchable_by=["Latios-EX", "Basic", "EX", "LatiosEX"],
    subtypes=["Basic", "EX"],
    collector_number=101,
    set_code="XY6",
    rarity=Rarities.RareUltra,
    hp=170,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    family_id=381,
    abilities=[
        Attack(
            title="Fast Raid",
            game_text="If you go first, you can use this attack on your first turn.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=40,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Light Pulse",
            game_text="Prevent all effects of your opponent's attacks, except damage, done to this Pok\u00e9mon during your opponent's next turn.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=110,
            # STUB: attack effect not implemented
            effect=protect_next_turn(effects_too=True),
        ),
    ],
)
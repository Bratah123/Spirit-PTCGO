"""STUB: effect not implemented — do not guess mechanics.
Latios-EX (XY6 #58): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5d0cde4e-e7fa-5d95-bf1e-29e6c18ed9a7",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LatiosEX.Name",
    display_name="Latios-EX",
    searchable_by=["Latios-EX", "Basic", "EX", "LatiosEX"],
    subtypes=["Basic", "EX"],
    collector_number=58,
    set_code="XY6",
    rarity=Rarities.RareHoloEX,
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
            effect=unimplemented,
        ),
    ],
)
"""STUB: effect not implemented — do not guess mechanics.
Wailord-EX (XY5 #147): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="50dc6278-ac4d-51ba-aaed-dc851cb390e3",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WailordEX.Name",
    display_name="Wailord-EX",
    searchable_by=["Wailord-EX", "Basic", "EX", "WailordEX"],
    subtypes=["Basic", "EX"],
    collector_number=147,
    set_code="XY5",
    rarity=Rarities.RareUltra,
    hp=250,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    family_id=321,
    abilities=[
        Ability(
            title="Water Veil",
            game_text="Whenever you attach an Energy card from your hand to this Pok\u00e9mon, remove all Special Conditions from it.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="High Breaching",
            game_text="This Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 5},
            damage=120,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)
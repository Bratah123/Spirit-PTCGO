"""STUB: effect not implemented — do not guess mechanics.
Latios-EX (Promo_XY #XY72): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e49f0fd0-ceac-5e21-b810-7fb78f317384",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LatiosEX.Name",
    display_name="Latios-EX",
    searchable_by=["Latios-EX", "Basic", "EX", "LatiosEX"],
    subtypes=["Basic", "EX"],
    collector_number=72,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
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
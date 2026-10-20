"""STUB: effect not implemented — do not guess mechanics.
Flying Pikachu (XY12 #110): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0d4f071a-3819-53f6-9aa3-b1dc8131a04a",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.FlyingPikachu.Name",
    display_name="Flying Pikachu",
    searchable_by=["Flying Pikachu", "Basic", "FlyingPikachu"],
    subtypes=["Basic"],
    collector_number=110,
    set_code="XY12",
    rarity=Rarities.RareSecret,
    hp=40,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=25,
    abilities=[
        Attack(
            title="Thunder Shock",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Fly",
            game_text="Flip a coin. If tails, this attack does nothing. If heads, prevent all effects of attacks, including damage, done to this Pok\u00e9mon during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)
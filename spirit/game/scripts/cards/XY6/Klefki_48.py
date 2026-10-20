"""STUB: effect not implemented — do not guess mechanics.
Klefki (XY6 #48): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="aa8eb436-ae05-5ba1-ac2c-a05c30e65b15",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Klefki.Name",
    display_name="Klefki",
    searchable_by=["Klefki", "Basic", "Klefki"],
    subtypes=["Basic"],
    collector_number=48,
    set_code="XY6",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=707,
    abilities=[
        Attack(
            title="Look for Keys",
            game_text="Reveal cards from the top of your deck until you reveal an Item card. Put it into your hand. Shuffle the other cards back into your deck.",
            cost={PokemonTypes.FAIRY: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Play Rough",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)
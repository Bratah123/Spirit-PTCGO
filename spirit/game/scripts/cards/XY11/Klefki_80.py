"""STUB: effect not implemented — do not guess mechanics.
Klefki (XY11 #80): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3d9825f4-a971-5dab-b11a-740f1a72c34a",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Klefki.Name",
    display_name="Klefki",
    searchable_by=["Klefki", "Basic", "Klefki"],
    subtypes=["Basic"],
    collector_number=80,
    set_code="XY11",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=707,
    abilities=[
        Ability(
            title="Wonder Lock",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon is on your Bench, you may discard all cards attached to this Pok\u00e9mon and attach it to 1 of your Pok\u00e9mon as a Pok\u00e9mon Tool card. Prevent any damage done to the Pok\u00e9mon this card is attached to by attacks from your opponent's Mega Evolution Pok\u00e9mon. If this card is attached to a Pok\u00e9mon, discard this card at the end of your opponent's turn.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Fairy Wind",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
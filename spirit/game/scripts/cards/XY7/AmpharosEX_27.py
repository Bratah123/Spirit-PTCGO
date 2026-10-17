"""STUB: effect not implemented — do not guess mechanics.
Ampharos-EX (XY7 #27): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a95137b4-4db8-5425-a630-ff6847a86531",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AmpharosEX.Name",
    display_name="Ampharos-EX",
    searchable_by=["Ampharos-EX", "Basic", "EX", "AmpharosEX"],
    subtypes=["Basic", "EX"],
    collector_number=27,
    set_code="XY7",
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    family_id=181,
    abilities=[
        Attack(
            title="Thunder Rod",
            game_text="Look at the top 4 cards of your deck and attach as many Lightning Energy cards you find there as you like to this Pok\u00e9mon. Shuffle the other cards back into your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Sparkling Tail",
            game_text="This attack's damage isn't affected by Weakness, Resistance, or any other effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 2},
            damage=100,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)
"""STUB: effect not implemented — do not guess mechanics.
Ho-Oh-EX (XY9 #121): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="350461da-78bb-55a3-aaa8-6e68200c6809",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HoOhEX.Name",
    display_name="Ho-Oh-EX",
    searchable_by=["Ho-Oh-EX", "Basic", "EX", "HoOhEX"],
    subtypes=["Basic", "EX"],
    collector_number=121,
    set_code="XY9",
    rarity=Rarities.RareUltra,
    hp=180,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=250,
    abilities=[
        Ability(
            title="Purifying Fire",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon has any basic Fire Energy attached to it, you may heal 50 damage from it.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Elemental Feather",
            game_text="This attack does 30 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 1},
            damage=130,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)
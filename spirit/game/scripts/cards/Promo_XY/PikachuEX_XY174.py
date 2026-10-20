"""STUB: effect not implemented — do not guess mechanics.
Pikachu-EX (Promo_XY #XY174): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="835e9104-c8c5-555c-baa5-9753b74ed22e",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PikachuEX.Name",
    display_name="Pikachu-EX",
    searchable_by=["Pikachu-EX", "Basic", "EX", "PikachuEX"],
    subtypes=["Basic", "EX"],
    collector_number=174,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=25,
    abilities=[
        Attack(
            title="Thunder Shock",
            game_text="Flip a coin. If heads your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Mega Thunderbolt",
            game_text="Discard all Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)
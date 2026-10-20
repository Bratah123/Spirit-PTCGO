"""STUB: effect not implemented — do not guess mechanics.
Espeon-EX (XY9 #52): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="cc7bc1cf-9c56-525c-a3b9-e38f62d409a5",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EspeonEX.Name",
    display_name="Espeon-EX",
    searchable_by=["Espeon-EX", "Basic", "EX", "EspeonEX"],
    subtypes=["Basic", "EX"],
    collector_number=52,
    set_code="XY9",
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=196,
    abilities=[
        Attack(
            title="Miraculous Shine",
            game_text="Devolve each of your opponent's evolved Pok\u00e9mon and put the highest Stage Evolution card on it into your opponent's hand.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Psyshock",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)
"""STUB: effect not implemented — do not guess mechanics.
Hawlucha (XY3 #63): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="589cda6d-cf8f-5120-9766-0f80057d6e7e",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hawlucha.Name",
    display_name="Hawlucha",
    searchable_by=["Hawlucha", "Basic", "Hawlucha"],
    subtypes=["Basic"],
    collector_number=63,
    set_code="XY3",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=701,
    abilities=[
        Ability(
            title="Shining Spirit",
            game_text="Damage from this Pok\u00e9mon's attacks isn't affected by Weakness or Resistance.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Flying Press",
            game_text="If your opponent's Active Pok\u00e9mon isn't a Pok\u00e9mon-EX, this attack does nothing.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=60,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)
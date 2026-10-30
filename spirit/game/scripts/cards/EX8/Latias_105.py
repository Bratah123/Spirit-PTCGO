"""STUB: effect not implemented — do not guess mechanics.
Latias ★ (EX8 #105): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import healing_light_all, shooting_star_vs_ex


card = PokemonCardDef(
    guid="15bfc3c6-c319-5dc9-b721-9754fbd37387",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Latias.Name",
    display_name="Latias ★",
    searchable_by=["Latias \u2605", "Basic", "Star", "Latias"],
    subtypes=["Basic", "Star"],
    collector_number=105,
    set_code="EX8",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.COLORLESS,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=380,
    abilities=[
        Attack(
            title="Healing Light",
            game_text="Remove 1 damage counter from each of your Pok\u00e9mon (including Latias Star).",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=healing_light_all(),
        ),
        Attack(
            title="Shooting Star",
            game_text="If the Defending Pok\u00e9mon is Pok\u00e9mon-ex, discard all Energy cards attached to Latias Star and this attack does 50 damage plus 100 more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1, PokemonTypes.PSYCHIC: 1},
            damage=50,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=shooting_star_vs_ex(),
        ),
    ],
)
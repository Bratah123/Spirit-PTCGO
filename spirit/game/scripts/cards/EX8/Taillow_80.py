"""STUB: effect not implemented — do not guess mechanics.
Taillow (EX8 #80): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import fly_flip_protect


card = PokemonCardDef(
    guid="4007e330-8fec-5d01-a41b-1cf2c7d3ed62",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Taillow.Name",
    display_name="Taillow",
    searchable_by=["Taillow", "Basic", "Taillow"],
    subtypes=["Basic"],
    collector_number=80,
    set_code="EX8",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=276,
    abilities=[
        Attack(
            title="Fly",
            game_text="Flip a coin. If tails, this attack does nothing. If heads, prevent all effects of an attack, including damage, done to Taillow during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=fly_flip_protect(),
        ),
    ],
)
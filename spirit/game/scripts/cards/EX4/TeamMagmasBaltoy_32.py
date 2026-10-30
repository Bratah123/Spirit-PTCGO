"""STUB: effect not implemented — do not guess mechanics.
Team Magma's Baltoy (EX4 #32): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import pain_amplifier, psymist

card = PokemonCardDef(
    guid="52026299-6c78-56b0-9523-37c8a45381c6",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasBaltoy.Name",
    display_name="Team Magma's Baltoy",
    searchable_by=["Team Magma's Baltoy", "Basic", "TeamMagmasBaltoy"],
    subtypes=["Basic"],
    collector_number=32,
    set_code="EX4",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=343,
    abilities=[
        Attack(
            title="Psymist",
            game_text="Flip 2 coins. For each heads, choose 1 of you opponent's Pok\u00e9mon and put 1 damage counter on that Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=psymist(),
        ),
        Attack(
            title="Pain Amplifier",
            game_text="Put 1 damage counter on each of your opponent's Pok\u00e9mon that already has damage counters on it.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=pain_amplifier(),
        ),
    ],
)
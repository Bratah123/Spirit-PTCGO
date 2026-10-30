"""STUB: effect not implemented — do not guess mechanics.
Team Magma's Poochyena (EX4 #65): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import snarl_or_paralyze

card = PokemonCardDef(
    guid="f5003ed5-fd88-5b5f-a55e-2f1485af7d62",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasPoochyena.Name",
    display_name="Team Magma's Poochyena",
    searchable_by=["Team Magma's Poochyena", "Basic", "TeamMagmasPoochyena"],
    subtypes=["Basic"],
    collector_number=65,
    set_code="EX4",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=261,
    abilities=[
        Attack(
            title="Snarl",
            game_text="Flip a coin. If heads, this attack does 10 damage to the Defending Pok\u00e9mon. If tails, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=snarl_or_paralyze(),
        ),
    ],
)
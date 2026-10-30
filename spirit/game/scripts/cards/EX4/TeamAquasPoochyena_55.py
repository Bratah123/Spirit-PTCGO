"""STUB: effect not implemented — do not guess mechanics.
Team Aqua's Poochyena (EX4 #55): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import discard_opponent_energy_attack
from spirit.game.card_effects.ex import force_opponent_switch


card = PokemonCardDef(
    guid="2aafdeb4-a79b-5fd3-9a9b-b8d5a36de1d5",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasPoochyena.Name",
    display_name="Team Aqua's Poochyena",
    searchable_by=["Team Aqua's Poochyena", "Basic", "TeamAquasPoochyena"],
    subtypes=["Basic"],
    collector_number=55,
    set_code="EX4",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=261,
    abilities=[
        Attack(
            title="Roar",
            game_text="Your opponent switches the Defending Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon, if any.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=force_opponent_switch(),
        ),
        Attack(
            title="Aqua Crush",
            game_text="Flip a coin. If heads, discard an Energy card attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=discard_opponent_energy_attack(1, flip=True),
        ),
    ],
)
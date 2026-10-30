"""STUB: effect not implemented — do not guess mechanics.
Poochyena (EX11 #79): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import force_opponent_switch
from spirit.game.card_effects.attacks_common import flip_bonus


card = PokemonCardDef(
    guid="70a1972e-bccf-58b8-8f8d-132ac83b41c2",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Poochyena.Name",
    display_name="Poochyena",
    searchable_by=["Poochyena", "Basic", "Poochyena"],
    subtypes=["Basic"],
    collector_number=79,
    set_code="EX11",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
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
            title="Ambush",
            game_text="Flip a coin. If heads, this attack does 10 damage plus 20 more damage.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=flip_bonus(20),
        ),
    ],
)
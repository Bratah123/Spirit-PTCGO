"""STUB: effect not implemented — do not guess mechanics.
Jirachi (EX5 #8): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, unimplemented
from spirit.game.attributes import AbilityTypes, PokemonStage, PokemonTypes, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ex import make_a_wish, poke_power_condition


card = PokemonCardDef(
    guid="313865b6-6236-54b4-a5d2-e592d3afa5b3",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jirachi.Name",
    display_name="Jirachi",
    searchable_by=["Jirachi", "Basic", "Jirachi"],
    subtypes=["Basic"],
    collector_number=8,
    set_code="EX5",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.PSYCHIC, PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=385,
    abilities=[
        Ability(
            title="Make a Wish",
            game_text="Search your deck for a card that evolves from 1 of your Pok\u00e9mon and put it on that Pok\u00e9mon. (This counts as evolving that Pok\u00e9mon.) If you do, put 1 damage counter on Jirachi. Shuffle your deck afterward.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=poke_power_condition(),
            effect=make_a_wish(),
        ),
        Attack(
            title="Mind Bend",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.METAL: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.CONFUSED, flip=True),
        ),
    ],
)
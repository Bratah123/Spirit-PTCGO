"""STUB: effect not implemented — do not guess mechanics.
Rocket's Persian ex (EX10 #116): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Activations, PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import night_cry_search, night_cry_condition
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="9371de7d-4e2c-5269-8fef-9b18997ddab6",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RocketsPersianex.Name",
    display_name="Rocket's Persian ex",
    searchable_by=["Rocket's Persian ex", "Stage 1", "ex", "RocketsPersianex"],
    subtypes=["Stage 1", "ex"],
    collector_number=116,
    set_code="EX10",
    rarity=Rarities.RareSecret,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.RocketsMeowth.Name",
    family_id=53,
    abilities=[
        Ability(
            title="Night Cry",
            game_text="Once during your turn, if Rocket's Persian ex is on your Bench, you may search your deck for a Pok\u00e9mon with Dark or Rocket's in its name. Show it to your opponent and put it into your hand. Shuffle your deck afterward.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            # STUB: ability effect not implemented
            condition=night_cry_condition(),
            effect=night_cry_search(),
        ),
        Attack(
            title="Toxic Claws",
            game_text="The Defending Pok\u00e9mon is now Poisoned. Put 2 damage counters instead of 1 on the Defending Pok\u00e9mon between turns.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.POISONED, counters=2),
        ),
    ],
)
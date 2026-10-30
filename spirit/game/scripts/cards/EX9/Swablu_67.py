"""STUB: effect not implemented — do not guess mechanics.
Swablu (EX9 #67): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import flip_or_nothing
from spirit.game.card_effects.ex import feathery_passive


card = PokemonCardDef(
    guid="354243fc-44c9-558f-8b5d-d606261848be",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swablu.Name",
    display_name="Swablu",
    searchable_by=["Swablu", "Basic", "Swablu"],
    subtypes=["Basic"],
    collector_number=67,
    set_code="EX9",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=333,
    abilities=[
        Ability(
            title="Feathery",
            game_text="As long as Swablu is on your Bench, prevent all damage done to Swablu by opponent's attacks.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=feathery_passive(),
        ),
        Attack(
            title="Razor Wind",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=flip_or_nothing(),
        ),
    ],
)
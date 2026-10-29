from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

from spirit.game.card_effects.sm8 import (
    bright_horns,
    path_of_life,
)

card = PokemonCardDef(
    guid="1078c2ac-187a-5a51-8092-f80a33af7601",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.XerneasPrismStar.Name",
    display_name="Xerneas {*}",
    searchable_by=["Xerneas {*}", "Basic", "Prism Star", "XerneasPrismStar"],
    subtypes=["Basic", "Prism Star"],
    collector_number=144,
    set_code="SM8",
    rarity=Rarities.Prism,
    hp=160,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=716,
    abilities=[
        Ability(
            title="Path of Life",
            game_text="Once during your turn, when this Pok\u00e9mon moves from your Bench to become your Active Pok\u00e9mon, you may move any number of Energy from your other Pok\u00e9mon to it.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=path_of_life,
            trigger=Triggers.ON_MOVE_TO_ACTIVE,
        ),
        Attack(
            title="Bright Horns",
            game_text="This Pok\u00e9mon can't use Bright Horns during your next turn.",
            cost={PokemonTypes.FAIRY: 3},
            damage=160,
            effect=bright_horns,
            locks_next_turn=True,
        ),
    ],
)
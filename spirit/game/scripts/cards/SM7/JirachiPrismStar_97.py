from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm7 import (
    perish_dream,
    wish_upon_a_star,
)
from spirit.game.data_utils import Triggers

card = PokemonCardDef(
    guid="729d4c52-67e8-5cbd-95ee-521f14c8505b",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.JirachiPrismStar.Name",
    display_name="Jirachi {*}",
    searchable_by=["Jirachi {*}", "Basic", "Prism Star", "JirachiPrismStar"],
    subtypes=["Basic", "Prism Star"],
    collector_number=97,
    set_code="SM7",
    rarity=Rarities.Prism,
    hp=80,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=385,
    abilities=[
        Ability(
            title="Wish Upon a Star",
            game_text="If you took this Pok\u00e9mon as a face-down Prize card during your turn and your Bench isn't full, before you put it into your hand, you may put it onto your Bench and take 1 more Prize card.",
            ability_type=AbilityTypes.POKE_ABILITY,
            trigger=Triggers.ON_TAKEN_AS_PRIZE,
            effect=wish_upon_a_star,
        ),
        Attack(
            title="Perish Dream",
            game_text="This Pok\u00e9mon is now Asleep. At the end of your opponent's next turn, the Defending Pok\u00e9mon will be Knocked Out.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=10,
            effect=perish_dream,
        ),
    ],
)
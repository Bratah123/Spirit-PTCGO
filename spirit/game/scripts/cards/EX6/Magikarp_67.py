from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing
from spirit.game.card_effects.ex import ascension


card = PokemonCardDef(
    guid="2463f803-4df3-5f93-bfd5-85899a240715",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magikarp.Name",
    display_name="Magikarp",
    searchable_by=["Magikarp", "Basic", "Magikarp"],
    subtypes=["Basic"],
    collector_number=67,
    set_code="EX6",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=129,
    abilities=[
        Attack(
            title="Surprise Attack",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=flip_or_nothing(),
        ),
        Attack(
            title="Ascension",
            game_text="Search your deck for a card that evolves from Magikarp and put it on Magikarp. (This counts as evolving Magikarp.) Shuffle your deck afterward.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            effect=ascension(),
        ),
    ],
)
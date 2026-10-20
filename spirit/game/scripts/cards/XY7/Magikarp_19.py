from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing


card = PokemonCardDef(
    guid="ea5b996a-0e3a-511d-999f-a69dd87c4b6f",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magikarp.Name",
    display_name="Magikarp",
    searchable_by=["Magikarp", "Basic", "Magikarp"],
    subtypes=["Basic"],
    collector_number=19,
    set_code="XY7",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=129,
    abilities=[
        Attack(
            title="Epic Splash",
            game_text="Flip 2 coins. If either of them is tails, this attack does nothing.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            effect=flip_or_nothing(coins=2),
        ),
    ],
)
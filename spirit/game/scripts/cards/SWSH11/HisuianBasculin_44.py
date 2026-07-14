from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing

card = PokemonCardDef(
    guid="9e6c47f3-403b-5067-8232-3cb5a58802a7",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianBasculin.Name",
    display_name="Hisuian Basculin",
    searchable_by=["Hisuian Basculin", "Basic", "HisuianBasculin"],
    subtypes=["Basic"],
    collector_number=44,
    set_code="SWSH11",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=550,
    abilities=[
        Attack(
            title="Surprise Attack",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={},
            damage=40,
            effect=flip_or_nothing(),
        ),
    ],
)
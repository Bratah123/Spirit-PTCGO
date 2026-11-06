from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import flip_protection


card = PokemonCardDef(
    guid="9e0554e5-8969-540a-a4f2-4caf64ba7ee1",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MistysMagikarp.Name",
    display_name="Misty's Magikarp",
    searchable_by=["Misty's Magikarp", "Basic", "MistysMagikarp"],
    subtypes=["Basic"],
    collector_number=88,
    set_code="GYM2",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=129,
    abilities=[
        Attack(
            title="Play Dead",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all effects of attacks, including damage, done to Misty's Magikarp.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=flip_protection(prevent=True, effects_too=True),
        ),
        Attack(
            title="Leap",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)

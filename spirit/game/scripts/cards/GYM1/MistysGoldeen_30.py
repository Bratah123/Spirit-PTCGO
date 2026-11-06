from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing


card = PokemonCardDef(
    guid="749a2ef7-889c-52f8-aa20-7a225fa50cfd",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MistysGoldeen.Name",
    display_name="Misty's Goldeen",
    searchable_by=["Misty's Goldeen", "Basic", "MistysGoldeen"],
    subtypes=["Basic"],
    collector_number=30,
    set_code="GYM1",
    rarity=Rarities.Rare,
    hp=30,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=118,
    abilities=[
        Attack(
            title="Horn Hazard",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            effect=flip_or_nothing(),
        ),
    ],
)

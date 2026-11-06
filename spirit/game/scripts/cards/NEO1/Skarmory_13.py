from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing
from spirit.game.card_effects.passives_common import flip_protection


card = PokemonCardDef(
    guid="639dc1d5-39c5-5fb3-afa8-b712d4d5a908",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Skarmory.Name",
    display_name="Skarmory",
    searchable_by=["Skarmory", "Basic", "Skarmory"],
    subtypes=["Basic"],
    collector_number=13,
    set_code="NEO1",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=227,
    abilities=[
        Attack(
            title="Claw",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=flip_or_nothing(),
        ),
        Attack(
            title="Steel Wing",
            game_text="Flip a coin. If heads, all damage done by attacks to Skarmory during your opponent's next turn is reduced by 20 (after applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=flip_protection(prevent=False, reduce=20),
        ),
    ],
)

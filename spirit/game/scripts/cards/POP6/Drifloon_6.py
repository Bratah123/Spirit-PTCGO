from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import blowing_wind_shuffle_bench, ominous_wind_confuse_lock


card = PokemonCardDef(
    guid="6eb06cd6-e409-5ad4-9f16-c5473424ca14",
    key="POP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drifloon.Name",
    display_name="Drifloon",
    searchable_by=["Drifloon", "Basic", "Drifloon"],
    subtypes=["Basic"],
    collector_number=6,
    set_code="POP6",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.COLORLESS,
    resistance_amount=20,
    family_id=425,
    abilities=[
        Attack(
            title="Blowing Wind",
            game_text="Flip a coin. If heads, put 1 of your Benched Pok\u00e9mon and all cards attached to it on top of your deck. Shuffle your deck afterward.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=blowing_wind_shuffle_bench(),
        ),
        Attack(
            title="Ominous Wind",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused and can't retreat during your opponent's next turn.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=ominous_wind_confuse_lock(10),
        ),
    ],
)

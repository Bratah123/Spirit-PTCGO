from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import sputter


card = PokemonCardDef(
    guid="c51b10ef-f6a3-5e55-be9b-393d622dd1fd",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magby.Name",
    display_name="Magby",
    searchable_by=["Magby", "Baby", "Magby"],
    subtypes=["Baby"],
    collector_number=23,
    set_code="NEO1",
    rarity=Rarities.Rare,
    hp=30,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    family_id=240,
    abilities=[
        Attack(
            title="Sputter",
            game_text="All Pok\u00e9mon Powers stop working until the end of your next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=sputter,
        ),
    ],
)

from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.gum import copy_anything

card = PokemonCardDef(
    guid="ae95efb5-ae66-5519-a8b0-98d0584dcaf1",
    key="GUM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ditto.Name",
    display_name="Ditto",
    searchable_by=["Ditto", "Basic", "Ditto"],
    subtypes=["Basic"],
    collector_number=17,
    set_code="GUM",
    rarity=Rarities.RareUltra,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=132,
    abilities=[
        Attack(
            title="Copy Anything",
            game_text="Choose 1 of your opponent's Pok\u00e9mon's attacks and use it as this attack. If this Pok\u00e9mon doesn't have the necessary Energy to use that attack, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=copy_anything,
        ),
    ],
)

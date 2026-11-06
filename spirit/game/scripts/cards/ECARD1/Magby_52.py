from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import energy_catch


card = PokemonCardDef(
    guid="c36fafde-da70-547d-a3e6-596f8adf4b32",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magby.Name",
    display_name="Magby",
    searchable_by=["Magby", "Baby", "Magby"],
    subtypes=["Baby"],
    collector_number=52,
    set_code="ECARD1",
    rarity=Rarities.Rare,
    hp=30,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=240,
    abilities=[
        Attack(
            title="Energy Catch",
            game_text="Flip a coin. If heads, put a basic Energy card from your discard pile into your hand.",
            cost={PokemonTypes.FIRE: 1},
            effect=energy_catch,
        ),
    ],
)

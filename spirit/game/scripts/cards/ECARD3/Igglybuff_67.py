from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import energy_heal


card = PokemonCardDef(
    guid="e1af3fe8-1828-5c6c-a16f-11dcc5ecc893",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Igglybuff.Name",
    display_name="Igglybuff",
    searchable_by=["Igglybuff", "Baby", "Igglybuff"],
    subtypes=["Baby"],
    collector_number=67,
    set_code="ECARD3",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=174,
    abilities=[
        Attack(
            title="Energy Heal",
            game_text="Choose 1 of your Pok\u00e9mon with an Energy card attached to it. Remove 1 damage counter from that Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=energy_heal,
        ),
    ],
)

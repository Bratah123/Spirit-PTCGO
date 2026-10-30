from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm6 import energy_teaser

card = PokemonCardDef(
    guid="dd29f874-9089-5313-b5ae-4195353fd6d1",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Espurr.Name",
    display_name="Espurr",
    searchable_by=["Espurr", "Basic", "Espurr"],
    subtypes=["Basic"],
    collector_number=44,
    set_code="SM6",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=677,
    abilities=[
        Attack(
            title="Energy Teaser",
            game_text="Move an Energy from 1 of your opponent's Benched Pok\u00e9mon to another of their Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=energy_teaser,
        ),
    ],
)

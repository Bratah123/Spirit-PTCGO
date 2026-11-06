from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import rainbow_wave


card = PokemonCardDef(
    guid="87a2036c-4ee8-532d-b98e-a2e0a95df53e",
    key="SI1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mew.Name",
    display_name="Mew",
    searchable_by=["Mew", "Basic", "Mew"],
    subtypes=["Basic"],
    collector_number=1,
    set_code="SI1",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=151,
    abilities=[
        Attack(
            title="Rainbow Wave",
            game_text="Choose a type of Energy other than Colorless attached to Mew. This attack does 20 damage to each of your opponent's Pok\u00e9mon of that type (including Benched Pok\u00e9mon). Don't apply Weakness and Resistance.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=rainbow_wave,
        ),
    ],
)

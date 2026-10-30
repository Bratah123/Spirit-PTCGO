from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import has_typed_basic_energy, return_energy_attack


card = PokemonCardDef(
    guid="e2aceb25-afa1-561b-a9cd-4aa70a9d2f67",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SabrinasAbra.Name",
    display_name="Sabrina's Abra",
    searchable_by=["Sabrina's Abra", "Basic", "SabrinasAbra"],
    subtypes=["Basic"],
    collector_number=91,
    set_code="GYM1",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=63,
    abilities=[
        Attack(
            title="Energy Loop",
            game_text="Return a Psychic Energy card attached to Sabrina's Abra to your hand in order to use this attack.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
            condition=has_typed_basic_energy(PokemonTypes.PSYCHIC),
            effect=return_energy_attack(PokemonTypes.PSYCHIC),
        ),
    ],
)

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_water_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.WATER.value)


find_ice = search_to_hand(
    predicate=_is_water_energy, count=2, reveal=True,
    prompt="Choose up to 2 Water Energy cards to put into your hand.",
)

card = PokemonCardDef(
    guid="30d21668-3a17-5b2d-96ef-d70f332f1446",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Snom.Name",
    display_name="Snom",
    searchable_by=["Snom", "Basic", "Snom"],
    subtypes=["Basic"],
    collector_number=84,
    set_code="SWSH8",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=872,
    abilities=[
        Attack(
            title="Find Ice",
            game_text="Search your deck for up to 2 Water Energy cards, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.WATER: 1},
            effect=find_ice,
        ),
    ],
)
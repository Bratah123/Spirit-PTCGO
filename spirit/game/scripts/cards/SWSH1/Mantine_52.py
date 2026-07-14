from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.pokemon import energy_provides_type

card = PokemonCardDef(
    guid="62adf16b-d007-52df-b559-e5bb9a831219",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mantine.Name",
    display_name="Mantine",
    searchable_by=["Mantine", "Basic", "Mantine"],
    subtypes=["Basic"],
    collector_number=52,
    set_code="SWSH1",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=226,
    abilities=[
        Attack(
            title="Water Reserve",
            game_text="Search your deck for up to 3 Water Energy cards, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.WATER: 1},
            effect=search_to_hand(
                lambda c: energy_provides_type(c, PokemonTypes.WATER.value),
                count=3, minimum=0,
                prompt="Choose up to 3 Water Energy cards to put into your hand.",
            ),
        ),
        Attack(
            title="Wave Splash",
            cost={PokemonTypes.WATER: 2},
            damage=60,
        ),
    ],
)
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.pokemon import energy_provides_type


card = PokemonCardDef(
    guid="4e6ce8a5-1bef-5d1b-8c44-626c575c3eb3",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mudkip.Name",
    display_name="Mudkip",
    searchable_by=["Mudkip", "Basic", "Mudkip"],
    subtypes=["Basic"],
    collector_number=32,
    set_code="SM7",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=258,
    abilities=[
        Attack(
            title="Water Reserve",
            game_text="Search your deck for up to 3 Water Energy cards, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=search_to_hand(lambda c: energy_provides_type(c, PokemonTypes.WATER.value), count=3, minimum=0, prompt='Choose up to 3 Water Energy cards to put into your hand.'),
        ),
    ],
)
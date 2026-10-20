from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_grass_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.GRASS.value)


card = PokemonCardDef(
    guid="cc0d4a4a-088a-5349-a094-9cd0a6363362",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chespin.Name",
    display_name="Chespin",
    searchable_by=["Chespin", "Basic", "Chespin"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="XY8",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=650,
    abilities=[
        Attack(
            title="Tree Climb",
            game_text="Search your deck for a Grass Energy card, reveal it, and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.GRASS: 1},
            effect=search_to_hand(_is_grass_energy, count=1, minimum=0, reveal=True,
                                   prompt='Choose a Grass Energy card'),
        ),
        Attack(
            title="Seed Bomb",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
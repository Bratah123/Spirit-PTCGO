from spirit.game.data_utils import PokemonCardDef, Attack, Ability, def_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.support_common import search_to_hand


def _is_melony(card):
    d = def_for(card.archetype_id)
    return bool(d) and d.display_name == "Melony"


card = PokemonCardDef(
    guid="48b6fafd-22c5-55b4-b36d-732bd1e49ec7",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lapras.Name",
    display_name="Lapras",
    searchable_by=["Lapras", "Basic", "Lapras"],
    subtypes=["Basic"],
    collector_number=29,
    set_code="SWSH6",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=131,
    abilities=[
        Attack(
            title="Wintry Call",
            game_text="Search your deck for up to 2 Melony cards, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_hand(
                _is_melony, count=2, minimum=0, reveal=True,
                prompt="Choose up to 2 Melony cards to put into your hand.",
            ),
        ),
        Attack(
            title="Icy Wind",
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)

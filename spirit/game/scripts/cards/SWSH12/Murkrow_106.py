from spirit.game.data_utils import PokemonCardDef, Attack, Ability, def_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import search_to_bench


def _is_murkrow(card) -> bool:
    d = def_for(card.archetype_id)
    return bool(d) and d.display_name == "Murkrow"


card = PokemonCardDef(
    guid="a1cc6396-8802-548d-9662-4288f7fb783f",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Murkrow.Name",
    display_name="Murkrow",
    searchable_by=["Murkrow", "Basic", "Murkrow"],
    subtypes=["Basic"],
    collector_number=106,
    set_code="SWSH12",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=198,
    abilities=[
        Attack(
            title="Flock",
            game_text="Search your deck for up to 2 Murkrow and put them onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_bench(predicate=_is_murkrow, count=2),
        ),
        Attack(
            title="Peck",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
        ),
    ],
)
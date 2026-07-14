from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import search_attach_energy
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_fighting_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.FIGHTING.value)


laser_focus = search_attach_energy(
    predicate=_is_fighting_energy, count=2, to_self=True,
    prompt="Choose up to 2 Fighting Energy cards to attach.",
)


card = PokemonCardDef(
    guid="2b4e5379-4f7a-58a8-8ab7-159118723a85",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SingleStrikeUrshifuV.Name",
    display_name="Single Strike Urshifu V",
    searchable_by=["Single Strike Urshifu V", "Basic", "V", "Single Strike", "SingleStrikeUrshifuV"],
    subtypes=["Basic", "V", "Single Strike"],
    collector_number=150,
    set_code="SWSH5",
    rarity=Rarities.RareUltra,
    hp=220,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=892,
    abilities=[
        Attack(
            title="Laser Focus",
            game_text="Search your deck for up to 2 Fighting Energy cards and attach them to this Pok\u00e9mon. Then, shuffle your deck.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=laser_focus,
        ),
        Attack(
            title="Impact Blow",
            game_text="During your next turn, this Pok\u00e9mon can't use Impact Blow.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=180,
            locks_next_turn=True,
        ),
    ],
)
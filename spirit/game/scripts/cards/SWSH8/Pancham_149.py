from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.card_effects.support_common import search_attach_energy


def _is_darkness_energy(card):
    return energy_provides_type(card, PokemonTypes.DARKNESS.value)


card = PokemonCardDef(
    guid="81f21ea7-ad34-5e5d-8d55-19b65fe7784c",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pancham.Name",
    display_name="Pancham",
    searchable_by=["Pancham", "Basic", "Pancham"],
    subtypes=["Basic"],
    collector_number=149,
    set_code="SWSH8",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=674,
    abilities=[
        Attack(
            title="Raised Bad",
            game_text="Search your deck for up to 2 Darkness Energy cards and attach them to this Pokémon. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_attach_energy(predicate=_is_darkness_energy, count=2, to_self=True),
        ),
        Attack(
            title="Smash Kick",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
        ),
    ],
)

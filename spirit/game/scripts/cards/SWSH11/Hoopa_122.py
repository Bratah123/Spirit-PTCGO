from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import search_attach_energy
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_darkness_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.DARKNESS)


card = PokemonCardDef(
    guid="c7318a02-a813-5c6c-8a1c-12eb05a05d07",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hoopa.Name",
    display_name="Hoopa",
    searchable_by=["Hoopa", "Basic", "Hoopa"],
    subtypes=["Basic"],
    collector_number=122,
    set_code="SWSH11",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=720,
    abilities=[
        Attack(
            title="Hand of Djinn",
            game_text="Search your deck for a Darkness Energy card and attach it to 1 of your Pok\u00e9mon. Then, shuffle your deck.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=search_attach_energy(
                _is_darkness_energy, count=1,
                prompt="Choose a Darkness Energy card to attach.",
            ),
        ),
        Attack(
            title="Tyrannical Hole",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
        ),
    ],
)
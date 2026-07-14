from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.card_effects.support_common import search_attach_energy


def _is_water_energy(card):
    return energy_provides_type(card, PokemonTypes.WATER.value)


card = PokemonCardDef(
    guid="d05205ad-77c3-5629-8d38-9e9878b8182b",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GlaceonV.Name",
    display_name="Glaceon V",
    searchable_by=["Glaceon V", "Basic", "V", "GlaceonV"],
    subtypes=["Basic", "V"],
    collector_number=38,
    set_code="CZ",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=471,
    abilities=[
        Attack(
            title="Frost Charge",
            game_text="Search your deck for a Water Energy card and attach it to this Pok\u00e9mon. Then, shuffle your deck.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            effect=search_attach_energy(predicate=_is_water_energy, count=1, to_self=True),
        ),
        Attack(
            title="Freezing Wind",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
    ],
)
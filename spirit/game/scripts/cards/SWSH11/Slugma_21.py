from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID, CardType
from spirit.game.card_effects.support_common import attach_from_discard


def _is_fire_energy_card(card):
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return card.get_attribute(AttrID.CARD_TYPE) == CardType.ENERGY.value \
        and PokemonTypes.FIRE.value in types


draw_in = attach_from_discard(
    predicate=_is_fire_energy_card, count=1, target="self", minimum=1,
    prompt="Choose a Fire Energy card to attach to this Pokémon",
)

card = PokemonCardDef(
    guid="c4f36c21-32b9-5413-b004-1fff5bc3f55a",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slugma.Name",
    display_name="Slugma",
    searchable_by=["Slugma", "Basic", "Slugma"],
    subtypes=["Basic"],
    collector_number=21,
    set_code="SWSH11",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=218,
    abilities=[
        Attack(
            title="Draw In",
            game_text="Attach a Fire Energy card from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1},
            effect=draw_in,
        ),
        Attack(
            title="Combustion",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)
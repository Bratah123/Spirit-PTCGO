from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID, TrainerType
from spirit.game.card_effects.support_common import recover_from_discard, requires_discard

_TOOL_TYPES = (TrainerType.POKEMON_TOOL.value, TrainerType.POKEMON_TOOL_F.value)


def _is_tool_card(card):
    return card.get_attribute(AttrID.TRAINER_TYPE) in _TOOL_TYPES


scrounge = recover_from_discard(
    predicate=_is_tool_card, count=1, minimum=1, reveal=False, to="hand",
    prompt="Choose a Pokémon Tool card to put into your hand.",
)

card = PokemonCardDef(
    guid="1107d6b1-b6b2-5e3a-b970-e5c169d2173a",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Skwovet.Name",
    display_name="Skwovet",
    searchable_by=["Skwovet", "Basic", "Skwovet"],
    subtypes=["Basic"],
    collector_number=127,
    set_code="SWSH6",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=819,
    abilities=[
        Attack(
            title="Scrounge",
            game_text="Put a Pok\u00e9mon Tool card from your discard pile into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=scrounge,
            condition=requires_discard(_is_tool_card),
        ),
        Attack(
            title="Gnaw",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
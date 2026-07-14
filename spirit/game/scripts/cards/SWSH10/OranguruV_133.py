from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities, TrainerType
from spirit.game.card_effects.attacks_common import damage_per, count_energy
from spirit.game.card_effects.pokemon import in_active_spot
from spirit.game.card_effects.support_common import search_to_hand


def _is_tool_card(card) -> bool:
    return card.get_attribute(AttrID.TRAINER_TYPE) in (
        TrainerType.POKEMON_TOOL.value, TrainerType.POKEMON_TOOL_F.value)


card = PokemonCardDef(
    guid="89fdfe37-7ef1-5be1-abfa-05bb78b92153",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.OranguruV.Name",
    display_name="Oranguru V",
    searchable_by=["Oranguru V", "Basic", "V", "OranguruV"],
    subtypes=["Basic", "V"],
    collector_number=133,
    set_code="SWSH10",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=765,
    abilities=[
        Ability(
            title="Back Order",
            game_text="Once during your turn, if this Pok\u00e9mon is in the Active Spot, you may search your deck for up to 2 Pok\u00e9mon Tool cards, reveal them, and put them into your hand. Then, shuffle your deck.",
            activation=Activations.ONCE_PER_TURN,
            condition=in_active_spot,
            effect=search_to_hand(predicate=_is_tool_card, count=2, reveal=True,
                                   prompt="Choose up to 2 Pok\u00e9mon Tool cards to put into your hand."),
        ),
        Attack(
            title="Psychic",
            game_text="This attack does 50 more damage for each Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator="+",
            effect=damage_per(count_energy("defender"), 50, base=30),
        ),
    ],
)
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if
from spirit.game.card_effects.support_common import recover_from_discard
from spirit.game.session.effects import is_item_card


def _empty_hand(ctx) -> bool:
    return ctx.hand_size() == 0


card = PokemonCardDef(
    guid="8eb645ee-906d-553a-9fd7-c7e8d99094b7",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Morpeko.Name",
    display_name="Morpeko",
    searchable_by=["Morpeko", "Basic", "Morpeko"],
    subtypes=["Basic"],
    collector_number=98,
    set_code="SWSH5",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=877,
    abilities=[
        Attack(
            title="Gather Food",
            game_text="Put an Item card from your discard pile into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=recover_from_discard(is_item_card, count=1, minimum=1, reveal=False, to="hand"),
        ),
        Attack(
            title="Hangry Tackle",
            game_text="If you have no cards in your hand, this attack does 90 more damage.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
            damage_operator="+",
            effect=bonus_if(_empty_hand, 90, base=20),
        ),
    ],
)
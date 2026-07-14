from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities, TrainerType
from spirit.game.session.effects import is_trainer_card
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.attacks_common import lock_all_attacks


def _is_stadium_card(card):
    return (
        is_trainer_card(card)
        and card.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.STADIUM.value
    )


async def hydro_break(ctx):
    """During your next turn, this Pokémon can't attack."""
    await ctx.deal_damage()
    lock_all_attacks(ctx, ctx.attacker)


card = PokemonCardDef(
    guid="5122f526-892d-531f-8e3b-073a265b6089",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.OriginFormePalkiaV.Name",
    display_name="Origin Forme Palkia V",
    searchable_by=["Origin Forme Palkia V", "Basic", "V", "OriginFormePalkiaV"],
    subtypes=["Basic", "V"],
    collector_number=39,
    set_code="SWSH10",
    rarity=Rarities.RareHoloV,
    hp=220,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=484,
    abilities=[
        Attack(
            title="Rule the Region",
            game_text="Search your deck for a Stadium card, reveal it, and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.WATER: 1},
            effect=search_to_hand(_is_stadium_card, count=1, minimum=0, reveal=True,
                                   prompt="Choose a Stadium card to put into your hand."),
        ),
        Attack(
            title="Hydro Break",
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=hydro_break,
        ),
    ],
)

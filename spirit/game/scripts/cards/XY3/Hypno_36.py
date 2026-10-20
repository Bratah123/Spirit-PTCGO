from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions, AttrID, TrainerType
from spirit.game.card_effects.attacks_common import condition_attack


def _is_supporter(card):
    return card.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.SUPPORTER.value


async def hand_control(ctx):
    """Your opponent reveals his or her hand. You may choose a Supporter card
    you find there. If you do, your opponent plays that Supporter card.
    However, you make all decisions for that card. (It is discarded.)"""
    opp = ctx.opponent_id
    if ctx.player_attack_shielded(opp):
        return
    hand = await ctx.reveal_hand(opp, ctx.player_id)
    supporters = [c for c in hand if _is_supporter(c)]
    if not supporters:
        return
    picks = await ctx.choose_cards(supporters, 1, minimum=0,
                                   prompt="You may choose a Supporter for your opponent to play")
    if picks:
        await ctx.play_opponent_supporter(picks[0])


card = PokemonCardDef(
    guid="093bbe28-2f07-573f-a308-b4fddb59d910",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hypno.Name",
    display_name="Hypno",
    searchable_by=["Hypno", "Stage 1", "Hypno"],
    subtypes=["Stage 1"],
    collector_number=36,
    set_code="XY3",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Drowzee.Name",
    family_id=96,
    abilities=[
        Attack(
            title="Hand Control",
            game_text="Your opponent reveals his or her hand. You may choose a Supporter card you find there. If you do, your opponent plays that Supporter card. However, you make all decisions for that card. (That Supporter card is discarded.)",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=hand_control,
        ),
        Attack(
            title="Hypnoblast",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=60,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)
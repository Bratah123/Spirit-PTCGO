from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import discard_random_from_hand
from spirit.game.card_effects.support_common import opponent_switches


async def knock_off(ctx):
    """discard a random card from the opponent's hand."""
    await ctx.deal_damage()
    await discard_random_from_hand(ctx, ctx.opponent_id, count=1)


async def _whirlwind(ctx):
    """Printed damage; you may have your opponent switch their Active."""
    await ctx.deal_damage()
    if ctx.opponent_bench() and await ctx.ask_yes_no(
            "Have your opponent switch the Defending Pok\u00e9mon?"):
        await opponent_switches(ctx)


card = PokemonCardDef(
    guid="fe40f556-61fb-52fe-98f9-c1105898b0ac",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Honchkrow.Name",
    display_name="Honchkrow",
    searchable_by=["Honchkrow", "Stage 1", "Honchkrow"],
    subtypes=["Stage 1"],
    collector_number=73,
    set_code="BW6",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Murkrow.Name",
    family_id=198,
    abilities=[
        Attack(
            title="Whirlwind",
            game_text="You may have your opponent switch the Defending Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=_whirlwind,
        ),
        Attack(
            title="Diving Swipe",
            game_text="Discard a random card from your opponent's hand.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=knock_off,
        ),
    ],
)
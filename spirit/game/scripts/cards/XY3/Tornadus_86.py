from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import opponent_switches
from spirit.game.card_effects.attacks_common import bonus_if


async def push_down(ctx):
    await ctx.deal_damage()
    opp_active = ctx.opponent_active()
    if opp_active is None or not ctx.opponent_bench() or ctx.effects_blocked(opp_active):
        return
    if await ctx.ask_yes_no("Have your opponent switch their Active Pokémon with 1 of their Benched Pokémon?"):
        await opponent_switches(ctx)


card = PokemonCardDef(
    guid="18073539-656f-5059-aa52-c1fa6384946e",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tornadus.Name",
    display_name="Tornadus",
    searchable_by=["Tornadus", "Basic", "Tornadus"],
    subtypes=["Basic"],
    collector_number=86,
    set_code="XY3",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=641,
    abilities=[
        Attack(
            title="Push Down",
            game_text="You may have your opponent switch his or her Active Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=push_down,
        ),
        Attack(
            title="Twister Throw",
            game_text="If you have the same number of cards in your hand as your opponent, this attack does 60 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            effect=bonus_if(lambda ctx: len(ctx.hand()) == len(ctx.hand(ctx.opponent_id)), 60),
        ),
    ],
)
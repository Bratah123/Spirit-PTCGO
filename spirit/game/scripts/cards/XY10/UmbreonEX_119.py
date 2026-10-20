from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.content.definitions import def_for


async def _veil_of_darkness(ctx):
    """20; discard any number of cards from your hand, then draw that many."""
    await ctx.deal_damage()
    hand = list(ctx.hand())
    if not hand:
        return
    picks = await ctx.choose_cards(hand, len(hand), minimum=0, prompt="Discard any number of cards")
    if picks:
        n = len(picks)
        await ctx.discard_cards(picks)
        await ctx.draw_cards(n)


def _is_mega(p):
    return "MEGA" in (getattr(def_for(p.archetype_id), "subtypes", None) or [])


async def _endgame(ctx):
    """70; if the opponent's Mega Evolution Pokemon is KO'd by this damage, take 2 more Prizes."""
    me = ctx.attacker
    ctx.add_extra_prize_watcher(attacker_predicate=lambda a: a is me,
                                target_predicate=_is_mega, prizes=2)
    await ctx.deal_damage()


card = PokemonCardDef(
    guid="88809045-f7cd-5f83-b5bd-a4efd567424a",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UmbreonEX.Name",
    display_name="Umbreon-EX",
    searchable_by=["Umbreon-EX", "Basic", "EX", "UmbreonEX"],
    subtypes=["Basic", "EX"],
    collector_number=119,
    set_code="XY10",
    rarity=Rarities.RareUltra,
    hp=170,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=197,
    abilities=[
        Attack(
            title="Veil of Darkness",
            game_text="Discard as many cards as you like from your hand. Then, draw that many cards.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=_veil_of_darkness,
        ),
        Attack(
            title="Endgame",
            game_text="If your opponent's Mega Evolution Pok\u00e9mon is Knocked Out by damage from this attack, take 2 more Prize cards.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=_endgame,
        ),
    ],
)
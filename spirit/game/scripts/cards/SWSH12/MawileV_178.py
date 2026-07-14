from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import discard_random_from_hand


async def pouty_slap(ctx):
    """30 damage; flip a coin, discard an Energy from the Defending Pokemon on heads."""
    await ctx.deal_damage()
    heads = (await ctx.flip_coins(1, ctx.ability.title))[0]
    if not heads:
        return
    target = ctx.opponent_active()
    if target is not None and not ctx.effects_blocked(target):
        await ctx.discard_energy_from(
            target, 1, prompt="Choose Energy to discard from the Defending Pokémon")


async def chomp_down(ctx):
    """100 damage; discard a random card from the opponent's hand."""
    await ctx.deal_damage()
    await discard_random_from_hand(ctx, ctx.opponent_id, 1)

card = PokemonCardDef(
    guid="1159942f-461f-5b31-b4ae-ddf854286a1d",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MawileV.Name",
    display_name="Mawile V",
    searchable_by=["Mawile V", "Basic", "V", "MawileV"],
    subtypes=["Basic", "V"],
    collector_number=178,
    set_code="SWSH12",
    rarity=Rarities.RareUltra,
    hp=200,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=303,
    abilities=[
        Attack(
            title="Pouty Slap",
            game_text="Flip a coin. If heads, discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=pouty_slap,
        ),
        Attack(
            title="Chomp Down",
            game_text="Discard a random card from your opponent's hand.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
            effect=chomp_down,
        ),
    ],
)
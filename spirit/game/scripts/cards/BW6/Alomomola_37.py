from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage


async def crunch(ctx):
    """30. Flip a coin. If heads, discard an Energy from the Defending Pokémon."""
    await ctx.deal_damage()
    heads = (await ctx.flip_coins(1, ctx.ability.title))[0]
    if not heads:
        return
    target = ctx.opponent_active()
    if target is not None and not ctx.effects_blocked(target):
        await ctx.discard_energy_from(
            target, 1, prompt="Choose Energy to discard from the Defending Pokémon")


card = PokemonCardDef(
    guid="3701bc7e-4103-5c1b-9e80-b819bdcf38ad",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Alomomola.Name",
    display_name="Alomomola",
    searchable_by=["Alomomola", "Basic", "Alomomola"],
    subtypes=["Basic"],
    collector_number=37,
    set_code="BW6",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=594,
    abilities=[
        Attack(
            title="Mysterious Beam",
            game_text="Flip a coin. If heads, discard an Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=crunch,
        ),
        Attack(
            title="Double Slap",
            game_text="Flip 2 coins. This attack does 50 damage times the number of heads.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=50),
        ),
    ],
)
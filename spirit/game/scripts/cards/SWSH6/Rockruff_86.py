from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def crunch(ctx):
    """Flip a coin. If heads, discard an Energy from the opponent's Active."""
    await ctx.deal_damage()
    heads = (await ctx.flip_coins(1, ctx.ability.title))[0]
    if heads:
        target = ctx.opponent_active()
        if target is not None and not ctx.effects_blocked(target):
            await ctx.discard_energy_from(
                target, 1, prompt="Choose Energy to discard from the Defending Pokémon")


card = PokemonCardDef(
    guid="055d764a-016f-5770-94a6-de719efb0cca",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rockruff.Name",
    display_name="Rockruff",
    searchable_by=["Rockruff", "Basic", "Single Strike", "Rockruff"],
    subtypes=["Basic", "Single Strike"],
    collector_number=86,
    set_code="SWSH6",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=744,
    abilities=[
        Attack(
            title="Crunch",
            game_text="Flip a coin. If heads, discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=30,
            effect=crunch,
        ),
    ],
)
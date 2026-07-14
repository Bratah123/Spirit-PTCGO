from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def pluck(ctx):
    """Before doing damage, discard all Pokémon Tools from the opponent's Active."""
    target = ctx.defender
    if target is not None and not ctx.effects_blocked(target):
        tools = [t for t, p in ctx.tools_in_play() if p is target]
        if tools:
            await ctx.discard_cards(tools)
    await ctx.deal_damage()

card = PokemonCardDef(
    guid="79899b78-7873-5d38-868d-792f413790b3",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vullaby.Name",
    display_name="Vullaby",
    searchable_by=["Vullaby", "Basic", "Vullaby"],
    subtypes=["Basic"],
    collector_number=119,
    set_code="SWSH2",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=629,
    abilities=[
        Attack(
            title="Pluck",
            game_text="Before doing damage, discard all Pok\u00e9mon Tools from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=pluck,
        ),
    ],
)
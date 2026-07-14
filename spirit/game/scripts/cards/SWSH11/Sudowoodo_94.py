from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def joust(ctx):
    defender = ctx.opponent_active()
    if defender is not None and not ctx.effects_blocked(defender):
        tools = [tool for tool, pokemon in ctx.tools_in_play() if pokemon is defender]
        if tools:
            await ctx.discard_cards(tools)
    await ctx.deal_damage()


async def impound(ctx):
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is not None and not ctx.effects_blocked(defender):
        ctx.lock_retreat(defender)


card = PokemonCardDef(
    guid="58307792-4a94-5143-ba5c-e2d03fa733a0",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sudowoodo.Name",
    display_name="Sudowoodo",
    searchable_by=["Sudowoodo", "Basic", "Sudowoodo"],
    subtypes=["Basic"],
    collector_number=94,
    set_code="SWSH11",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=185,
    abilities=[
        Attack(
            title="Joust",
            game_text="Before doing damage, discard all Pok\u00e9mon Tools from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            effect=joust,
        ),
        Attack(
            title="Impound",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=impound,
        ),
    ],
)
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def incinerate(ctx):
    """Before doing damage, discard all Tools from the opponent's Active."""
    defender = ctx.defender
    if defender is not None and not ctx.effects_blocked(defender):
        tools = [t for t, p in ctx.tools_in_play() if p is defender]
        if tools:
            await ctx.discard_cards(tools)
    await ctx.deal_damage()


card = PokemonCardDef(
    guid="7c859d59-2894-5783-8c83-60fb3049e133",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CharizardV.Name",
    display_name="Charizard V",
    searchable_by=["Charizard V", "Basic", "V", "CharizardV"],
    subtypes=["Basic", "V"],
    collector_number=18,
    set_code="CZ",
    rarity=Rarities.RareHoloV,
    hp=220,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=6,
    abilities=[
        Attack(
            title="Incinerate",
            game_text="Before doing damage, discard all Pok\u00e9mon Tools from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=incinerate,
        ),
        Attack(
            title="Heat Blast",
            cost={PokemonTypes.FIRE: 3, PokemonTypes.COLORLESS: 1},
            damage=180,
        ),
    ],
)
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

async def _obsidian_fang(ctx):
    """Before doing damage, discard all Pokemon Tools from the opponent's Active."""
    defender = ctx.defender
    if defender is not None and not ctx.effects_blocked(defender):
        tools = [t for t, p in ctx.tools_in_play() if p is defender]
        if tools:
            await ctx.discard_cards(tools)
    await ctx.deal_damage()

card = PokemonCardDef(
    guid="93539eb7-75b3-5449-8811-25fc5140b839",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pikipek.Name",
    display_name="Pikipek",
    searchable_by=["Pikipek", "Basic", "Pikipek"],
    subtypes=["Basic"],
    collector_number=163,
    set_code="SM8",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=731,
    abilities=[
        Attack(
            title="Peck Off",
            game_text="Before doing damage, discard all Pok\u00e9mon Tool cards from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=_obsidian_fang,
        ),
    ],
)
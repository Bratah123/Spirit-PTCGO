from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _constant_rattle(ctx):
    results = await ctx.flip_coins(3, ctx.ability.title)
    heads = sum(1 for r in results if r)
    amount = {1: 10, 2: 30, 3: 60}.get(heads, 0)
    if amount:
        await ctx.deal_damage(amount)


async def _giga_drain(ctx):
    dealt = await ctx.deal_damage()
    if dealt > 0:
        await ctx.heal(dealt)


card = PokemonCardDef(
    guid="3594d136-d42c-58ab-b9a3-e9f4900000a2",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Maractus.Name",
    display_name="Maractus",
    searchable_by=["Maractus", "Basic", "Maractus"],
    subtypes=["Basic"],
    collector_number=12,
    set_code="BW1",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    family_id=556,
    abilities=[
        Attack(
            title="Constant Rattle",
            game_text="Flip 3 coins. If 1 of them is heads, this attack does 10 damage. If 2 of them are heads, this attack does 30 damage. If all of them are heads, this attack does 60 damage.",
            cost={PokemonTypes.GRASS: 1},
            effect=_constant_rattle,
        ),
        Attack(
            title="Giga Drain",
            game_text="Heal from this Pok\u00e9mon the same amount of damage you did to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 3},
            damage=50,
            effect=_giga_drain,
        ),
    ],
)

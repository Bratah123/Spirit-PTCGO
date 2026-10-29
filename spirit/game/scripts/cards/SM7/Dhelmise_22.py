from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import lock_all_attacks


async def gulp_down(ctx):
    """Heal from this Pokémon the same amount of damage you did to your
    opponent's Active Pokémon."""
    dealt = await ctx.deal_damage()
    if dealt > 0:
        await ctx.heal(dealt, ctx.attacker)


async def _freeze_shock(ctx):
    """Printed damage; this Pokemon can't attack during your next turn."""
    await ctx.deal_damage()
    lock_all_attacks(ctx, ctx.attacker)


card = PokemonCardDef(
    guid="831941b3-97dd-533e-83a7-0a302c2f5b6c",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dhelmise.Name",
    display_name="Dhelmise",
    searchable_by=["Dhelmise", "Basic", "Dhelmise"],
    subtypes=["Basic"],
    collector_number=22,
    set_code="SM7",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    family_id=781,
    abilities=[
        Attack(
            title="Giga Drain",
            game_text="Heal from this Pok\u00e9mon the same amount of damage you did to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=gulp_down,
        ),
        Attack(
            title="Powerful Spin",
            game_text="This Pok\u00e9mon can't attack during your next turn.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            # STUB: attack effect not implemented
            effect=_freeze_shock,
        ),
    ],
)
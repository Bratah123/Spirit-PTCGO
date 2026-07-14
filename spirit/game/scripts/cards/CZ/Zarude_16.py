from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage


async def drag_off(ctx):
    """Switch 1 of the opponent's Benched Pokémon with their Active; 20
    damage to the new Active Pokémon."""
    bench = ctx.opponent_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(
        bench, "Choose your opponent's new Active Pokémon"
    )
    if target is not None and await ctx.switch_active(ctx.opponent_id, target):
        await ctx.deal_damage(20, target=target)


card = PokemonCardDef(
    guid="55826f80-1168-573d-a0e6-2487a0e1ca90",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zarude.Name",
    display_name="Zarude",
    searchable_by=["Zarude", "Basic", "Zarude"],
    subtypes=["Basic"],
    collector_number=16,
    set_code="CZ",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=893,
    abilities=[
        Attack(
            title="Drag Off",
            game_text="Switch 1 of your opponent's Benched Pok\u00e9mon with their Active Pok\u00e9mon. This attack does 20 damage to the new Active Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            effect=drag_off,
        ),
        Attack(
            title="Triple Whip",
            game_text="Flip 3 coins. This attack does 70 damage for each heads.",
            cost={PokemonTypes.GRASS: 2},
            damage=70,
            damage_operator="x",
            effect=flip_damage(coins=3, per_heads=70),
        ),
    ],
)
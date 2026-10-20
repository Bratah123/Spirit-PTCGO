from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def phat_sound(ctx):
    """Flip 3 coins. 10×heads to each of opponent's Pokémon (no W/R on bench)."""
    results = await ctx.flip_coins(3, ctx.ability.title)
    amount = 10 * sum(1 for r in results if r)
    if amount <= 0:
        return
    for p in ctx.opponent_pokemon_in_play():
        await ctx.deal_damage(amount, target=p, apply_modifiers=None)


card = PokemonCardDef(
    guid="4ebca1d6-11c4-5508-a3aa-587864218886",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swoobat.Name",
    display_name="Swoobat",
    searchable_by=["Swoobat", "Stage 1", "Swoobat"],
    subtypes=["Stage 1"],
    collector_number=37,
    set_code="BW2",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Woobat.Name",
    family_id=527,
    abilities=[
        Attack(
            title="Psyshot",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
        ),
        Attack(
            title="Phat Sound",
            game_text="Flip 3 coins. This attack does 10 damage times the number of heads to each of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=phat_sound,
        ),
    ],
)

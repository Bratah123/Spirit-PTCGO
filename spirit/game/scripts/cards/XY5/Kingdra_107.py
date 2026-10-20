from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import shred


async def _twister(ctx):
    """Flip 2 coins: discard an Energy from the opponent's Active per heads;
    both tails does nothing."""
    results = await ctx.flip_coins(2, ctx.ability.title) or []
    heads = sum(1 for r in results if r)
    if not heads:
        return
    await ctx.deal_damage()
    d = ctx.defender
    if d is not None and not ctx.effects_blocked(d):
        n = min(heads, len(ctx.attached_energies(d)))
        if n:
            await ctx.discard_energy_from(d, n, minimum=n)


card = PokemonCardDef(
    guid="82099f07-4297-5ca5-bf65-d9701727aa76",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kingdra.Name",
    display_name="Kingdra",
    searchable_by=["Kingdra", "Stage 2", "Kingdra"],
    subtypes=["Stage 2"],
    collector_number=107,
    set_code="XY5",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Seadra.Name",
    family_id=116,
    abilities=[
        Attack(
            title="Shred",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            effect=shred,
        ),
        Attack(
            title="Twister",
            game_text="Flip 2 coins. For each heads, discard an Energy attached to your opponent's Active Pok\u00e9mon. If both of them are tails, this attack does nothing.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 1},
            damage=70,
            effect=_twister,
        ),
    ],
)
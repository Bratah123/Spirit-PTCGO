from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def deleting_glare(ctx):
    """Flip a coin. If heads, discard an Energy from 1 of opponent's Pokémon."""
    results = await ctx.flip_coins(1, ctx.ability.title)
    if not results or not results[0]:
        return
    candidates = [
        p for p in ctx.opponent_pokemon_in_play() if ctx.attached_energies(p)
    ]
    if not candidates:
        return
    target = await ctx.choose_pokemon(
        candidates, "Choose 1 of your opponent's Pokémon",
    )
    if target is None or ctx.effects_blocked(target):
        return
    await ctx.discard_energy_from(
        target, 1,
        prompt="Choose Energy to discard",
    )


card = PokemonCardDef(
    guid="c5654b46-cfb8-5e38-b452-16eb3f1520be",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Electrode.Name",
    display_name="Electrode",
    searchable_by=["Electrode", "Stage 1", "Electrode"],
    subtypes=["Stage 1"],
    collector_number=45,
    set_code="XY1",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Voltorb.Name",
    family_id=100,
    abilities=[
        Attack(
            title="Eerie Impulse",
            game_text="Flip a coin. If heads, discard an Energy attached to 1 of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=deleting_glare,
        ),
        Attack(
            title="Rollout",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)
from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def crunch(ctx):
    """40 damage. Flip; if heads, discard an Energy from the Defending Pokémon."""
    await ctx.deal_damage()
    heads = (await ctx.flip_coins(1, ctx.ability.title))[0]
    if not heads:
        return
    target = ctx.opponent_active()
    if target is not None and not ctx.effects_blocked(target):
        await ctx.discard_energy_from(
            target, 1,
            prompt="Choose Energy to discard from the Defending Pokémon",
        )


card = PokemonCardDef(
    guid="060d174c-d499-52a6-9cfc-e4d73bf7125d",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Krokorok.Name",
    display_name="Krokorok",
    searchable_by=["Krokorok", "Stage 1", "Krokorok"],
    subtypes=["Stage 1"],
    collector_number=61,
    set_code="BW2",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sandile.Name",
    family_id=551,
    abilities=[
        Attack(
            title="Bite",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Crunch",
            game_text="Flip a coin. If heads, discard an Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=crunch,
        ),
    ],
)

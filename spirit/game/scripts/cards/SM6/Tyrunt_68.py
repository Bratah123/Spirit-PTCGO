from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

async def cut_down(ctx):
    """Printed damage; flip a coin, heads: discard an Energy from the opponent's Active."""
    await ctx.deal_damage()
    heads = await ctx.flip_coins(1, "Muddy Acid")
    if not heads[0]:
        return
    target = ctx.opponent_active()
    if target is None or ctx.effects_blocked(target):
        return
    await ctx.discard_energy_from(
        target, 1,
        prompt="Choose an Energy to discard from the Defending Pokémon.",
    )

card = PokemonCardDef(
    guid="5fba4b1b-fc09-54c5-9e3a-e2c92968a90d",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tyrunt.Name",
    display_name="Tyrunt",
    searchable_by=["Tyrunt", "Stage 1", "Tyrunt"],
    subtypes=["Stage 1"],
    collector_number=68,
    set_code="SM6",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.UnidentifiedFossil.Name",
    family_id=696,
    abilities=[
        Attack(
            title="Crunch",
            game_text="Flip a coin. If heads, discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            effect=cut_down,
        ),
        Attack(
            title="Hammer In",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)

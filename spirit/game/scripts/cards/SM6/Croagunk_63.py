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
    guid="2f76ab6e-56fe-545d-a7d0-d92ecd18d9be",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Croagunk.Name",
    display_name="Croagunk",
    searchable_by=["Croagunk", "Basic", "Croagunk"],
    subtypes=["Basic"],
    collector_number=63,
    set_code="SM6",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=453,
    abilities=[
        Attack(
            title="Swagger",
            game_text="Flip a coin. If heads, discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
            effect=cut_down,
        ),
    ],
)

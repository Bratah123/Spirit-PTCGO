from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def crunch(ctx):
    """30. Flip a coin. If heads, discard an Energy from the Defending Pokémon."""
    await ctx.deal_damage()
    heads = (await ctx.flip_coins(1, ctx.ability.title))[0]
    if not heads:
        return
    target = ctx.opponent_active()
    if target is not None and not ctx.effects_blocked(target):
        await ctx.discard_energy_from(
            target, 1, prompt="Choose Energy to discard from the Defending Pokémon")


card = PokemonCardDef(
    guid="b7ccf62f-c2c6-5b79-9369-a50c039fd5bd",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scrafty.Name",
    display_name="Scrafty",
    searchable_by=["Scrafty", "Stage 1", "Scrafty"],
    subtypes=["Stage 1"],
    collector_number=68,
    set_code="BW5",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Scraggy.Name",
    family_id=559,
    abilities=[
        Attack(
            title="Headbutt",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title="Crushing Blow",
            game_text="Flip a coin. If heads, discard an Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=crunch,
        ),
    ],
)
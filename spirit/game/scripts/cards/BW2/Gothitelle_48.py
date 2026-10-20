from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions


async def mental_shock(ctx):
    """60 damage. Flip: heads Confused, tails discard Energy from defender."""
    await ctx.deal_damage()
    heads = (await ctx.flip_coins(1, ctx.ability.title))[0]
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    if heads:
        await ctx.apply_special_condition(defender, SpecialConditions.CONFUSED)
    else:
        await ctx.discard_energy_from(
            defender, 1,
            prompt="Choose Energy to discard from the Defending Pokémon",
        )


card = PokemonCardDef(
    guid="e016bcab-0d9c-5692-8357-b54afe554425",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gothitelle.Name",
    display_name="Gothitelle",
    searchable_by=["Gothitelle", "Stage 2", "Gothitelle"],
    subtypes=["Stage 2"],
    collector_number=48,
    set_code="BW2",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gothorita.Name",
    family_id=574,
    abilities=[
        Attack(
            title="Smack",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
        ),
        Attack(
            title="Mental Shock",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused. If tails, discard an Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=mental_shock,
        ),
    ],
)

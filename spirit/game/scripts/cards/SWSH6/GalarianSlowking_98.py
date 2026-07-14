from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def mysterious_potion(ctx):
    """Once per turn: you may choose 1 of your Pokémon and flip a coin. Heads
    heals 90 from it; tails puts 3 damage counters on it."""
    if not await ctx.ask_yes_no("Choose 1 of your Pokémon and flip a coin?"):
        return
    target = await ctx.choose_pokemon(
        ctx.my_pokemon_in_play(), "Choose 1 of your Pokémon"
    )
    if target is None:
        return
    heads = (await ctx.flip_coins(1, "Mysterious Potion"))[0]
    if heads:
        await ctx.heal(90, target=target)
    else:
        await ctx.deal_damage(30, target=target, apply_modifiers=False, as_counters=True)


card = PokemonCardDef(
    guid="d944645a-0420-5347-b863-d5f6a19e1208",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianSlowking.Name",
    display_name="Galarian Slowking",
    searchable_by=["Galarian Slowking", "Stage 1", "GalarianSlowking"],
    subtypes=["Stage 1"],
    collector_number=98,
    set_code="SWSH6",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianSlowpoke.Name",
    family_id=79,
    abilities=[
        Ability(
            title="Mysterious Potion",
            game_text="Once during your turn, you may choose 1 of your Pok\u00e9mon and flip a coin. If heads, heal 90 damage from that Pok\u00e9mon. If tails, put 3 damage counters on that Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            effect=mysterious_potion,
        ),
        Attack(
            title="Spray Fluid",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
        ),
    ],
)
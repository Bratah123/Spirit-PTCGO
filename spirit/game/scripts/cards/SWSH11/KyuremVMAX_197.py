from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import energy_provides_type


async def glaciated_world(ctx):
    """Once per turn, discard the top deck card; if Water Energy, attach it."""
    if not await ctx.ask_yes_no("Discard the top card of your deck?"):
        return
    top = ctx.deck_top(1)
    if not top:
        return
    card = top[0]
    await ctx.discard_cards([card])
    if energy_provides_type(card, PokemonTypes.WATER):
        target = await ctx.choose_pokemon(
            ctx.my_pokemon_in_play(), "Attach the Water Energy to 1 of your Pokémon"
        )
        if target is not None:
            await ctx.attach_energy(card, target)


async def max_frost(ctx):
    """You may discard any amount of Water Energy from this Pokemon; +50 each."""
    attached = [
        e for e in ctx.attached_energies(ctx.attacker)
        if energy_provides_type(e, PokemonTypes.WATER)
    ]
    picks = []
    if attached:
        picks = await ctx.choose_cards(
            attached, len(attached), minimum=0,
            prompt="Discard any amount of Water Energy from this Pokémon.",
        )
        if picks:
            await ctx.discard_cards(picks)
    await ctx.deal_damage(120 + 50 * len(picks))


card = PokemonCardDef(
    guid="77fc6d36-e8c2-52f9-81eb-ac0ebe6ad0ae",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KyuremVMAX.Name",
    display_name="Kyurem VMAX",
    searchable_by=["Kyurem VMAX", "VMAX", "KyuremVMAX"],
    subtypes=["VMAX"],
    collector_number=197,
    set_code="SWSH11",
    rarity=Rarities.RareRainbow,
    hp=330,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.VMAX,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.KyuremV.Name",
    family_id=646,
    abilities=[
        Ability(
            title="Glaciated World",
            game_text="Once during your turn, you may discard the top card of your deck. If that card is a Water Energy card, attach it to 1 of your Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            effect=glaciated_world,
        ),
        Attack(
            title="Max Frost",
            game_text="You may discard any amount of Water Energy from this Pok\u00e9mon. This attack does 50 more damage for each card you discarded in this way.",
            cost={PokemonTypes.WATER: 3},
            damage=120,
            damage_operator="+",
            effect=max_frost,
        ),
    ],
)
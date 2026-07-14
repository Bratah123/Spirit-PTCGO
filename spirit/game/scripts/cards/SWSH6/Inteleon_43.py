from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def quick_shooting(ctx):
    """Once per turn: you may put 2 damage counters on 1 of your opponent's Pokemon."""
    if not await ctx.ask_yes_no("Put 2 damage counters on 1 of your opponent's Pokémon?"):
        return
    targets = ctx.opponent_pokemon_in_play()
    if not targets:
        return
    target = await ctx.choose_pokemon(targets, "Choose 1 of your opponent's Pokémon")
    if target is not None:
        await ctx.deal_damage(20, target=target, apply_modifiers=False, as_counters=True)


card = PokemonCardDef(
    guid="0b78ab70-a9d8-55b0-b36f-f25ef5471dbf",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Inteleon.Name",
    display_name="Inteleon",
    searchable_by=["Inteleon", "Stage 2", "Rapid Strike", "Inteleon"],
    subtypes=["Stage 2", "Rapid Strike"],
    collector_number=43,
    set_code="SWSH6",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Drizzile.Name",
    family_id=816,
    abilities=[
        Ability(
            title="Quick Shooting",
            game_text="Once during your turn, you may put 2 damage counters on 1 of your opponent's Pokémon.",
            activation=Activations.ONCE_PER_TURN,
            effect=quick_shooting,
        ),
        Attack(
            title="Waterfall",
            cost={PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import energy_provides_type


def lunar_blessing_condition(board, player_id, pokemon):
    active = board.active_pokemon(player_id)
    if active is None:
        return False
    return any(energy_provides_type(e, PokemonTypes.PSYCHIC.value)
               for e in board.attached_energies(active))


async def lunar_blessing(ctx):
    """Once during your turn, if your Active has Psychic Energy attached,
    you may heal 20 damage from it and have it recover from a Special Condition."""
    active = ctx.my_active()
    if active is None:
        return
    if not await ctx.ask_yes_no(
        "Heal 20 damage from your Active Pokémon and have it recover from a Special Condition?"
    ):
        return
    await ctx.heal(20, active)
    await ctx.cure_all_conditions(active)


card = PokemonCardDef(
    guid="e5976ae1-72b6-5c7e-8f2e-d3c99f7a5d65",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Clefable.Name",
    display_name="Clefable",
    searchable_by=["Clefable", "Stage 1", "Clefable"],
    subtypes=["Stage 1"],
    collector_number=64,
    set_code="SWSH4",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Clefairy.Name",
    family_id=35,
    abilities=[
        Ability(
            title="Lunar Blessing",
            game_text="Once during your turn, if your Active Pok\u00e9mon has any Psychic Energy attached, you may heal 20 damage from it, and it recovers from a Special Condition.",
            activation=Activations.ONCE_PER_TURN,
            condition=lunar_blessing_condition,
            effect=lunar_blessing,
        ),
        Attack(
            title="Magical Shot",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)
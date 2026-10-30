from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _shadow_shutdown(ctx):
    """Printed damage; flip 2, both heads discard all Energy from the Defending Pokémon."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(2, ctx.ability.title)
    defender = ctx.defender
    if len(results) == 2 and all(results) and defender is not None \
            and not ctx.effects_blocked(defender):
        energies = ctx.attached_energies(defender)
        if energies:
            await ctx.discard_cards(energies)


card = PokemonCardDef(
    guid="a0c61450-64a3-5631-9fde-144c52900306",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Altaria.Name",
    display_name="Altaria",
    searchable_by=["Altaria", "Stage 1", "Altaria"],
    subtypes=["Stage 1"],
    collector_number=92,
    set_code="BW11",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DRAGON,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Swablu.Name",
    family_id=333,
    abilities=[
        Attack(
            title="Speed Dive",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title="Cleave",
            game_text="Flip 2 coins. If both of them are heads, discard all Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=_shadow_shutdown,
        ),
    ],
)
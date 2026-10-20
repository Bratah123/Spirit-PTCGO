from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


async def _shadow_shutdown(ctx):
    """Printed damage; flip 2, both heads discard all Energy from the Defending Pokémon."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(2, "Shadow Shutdown")
    defender = ctx.defender
    if len(results) == 2 and all(results) and defender is not None \
            and not ctx.effects_blocked(defender):
        energies = ctx.attached_energies(defender)
        if energies:
            await ctx.discard_cards(energies)


card = PokemonCardDef(
    guid="c912b95b-b2d0-5f2c-b635-c2738631de94",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Umbreon.Name",
    display_name="Umbreon",
    searchable_by=["Umbreon", "Stage 1", "Umbreon"],
    subtypes=["Stage 1"],
    collector_number=61,
    set_code="BW5",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Confuse Ray",
            game_text="The Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
        Attack(
            title="Shadow Shutdown",
            game_text="Flip 2 coins. If both of them are heads, discard all Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=_shadow_shutdown,
        ),
    ],
)
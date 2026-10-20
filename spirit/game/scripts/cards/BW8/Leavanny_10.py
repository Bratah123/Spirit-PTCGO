from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus


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
    guid="924185b5-e4c7-5142-bd6e-0e60281f489d",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Leavanny.Name",
    display_name="Leavanny",
    searchable_by=["Leavanny", "Stage 2", "Leavanny"],
    subtypes=["Stage 2"],
    collector_number=10,
    set_code="BW8",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Swadloon.Name",
    family_id=540,
    abilities=[
        Attack(
            title="Cleave",
            game_text="Flip 2 coins. If both of them are heads, discard all Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=_shadow_shutdown,
        ),
        Attack(
            title="Leaf Blade",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            damage_operator="+",
            effect=flip_bonus(20),
        ),
    ],
)
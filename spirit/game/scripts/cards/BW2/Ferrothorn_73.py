from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import count_energy
from spirit.game.card_effects.passives_common import flip_protection


async def power_whip(ctx):
    """10 damage times Energy on self to 1 of opponent's Pokémon."""
    targets = ctx.opponent_pokemon_in_play()
    if not targets:
        return
    target = await ctx.choose_pokemon(targets, "Choose 1 of your opponent's Pokémon")
    if target is None:
        return
    amount = 10 * count_energy("self")(ctx)
    if amount <= 0:
        return
    await ctx.deal_damage(
        amount, target=target,
        apply_modifiers=(target is ctx.opponent_active()),
    )


card = PokemonCardDef(
    guid="44968a50-af8a-5500-8eda-54a2e3a1082b",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ferrothorn.Name",
    display_name="Ferrothorn",
    searchable_by=["Ferrothorn", "Stage 1", "Ferrothorn"],
    subtypes=["Stage 1"],
    collector_number=73,
    set_code="BW2",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ferroseed.Name",
    family_id=597,
    abilities=[
        Attack(
            title="Iron Defense",
            game_text="Flip a coin. If heads, prevent all effects of attacks, including damage, done to this Pok\u00e9mon during your opponent's next turn.",
            cost={PokemonTypes.METAL: 1},
            effect=flip_protection(prevent=True, effects_too=True),
        ),
        Attack(
            title="Power Whip",
            game_text="Does 10 damage for each Energy attached to this Pok\u00e9mon to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 2},
            effect=power_whip,
        ),
    ],
)

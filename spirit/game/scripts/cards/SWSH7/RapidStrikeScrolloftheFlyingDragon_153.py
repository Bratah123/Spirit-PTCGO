from spirit.game.data_utils import PokemonToolCardDef, Attack, subtypes_for
from spirit.game.attributes import Rarities, PokemonTypes


def _is_rapid_strike(board, player_id, pokemon):
    return "Rapid Strike" in subtypes_for(pokemon.archetype_id)


async def _meteor(ctx):
    """Discard 2 Energy from this Pokemon. 90 damage to 1 of your opponent's Pokemon (no W/R on Bench)."""
    await ctx.discard_energy_from(ctx.attacker, 2, prompt="Discard 2 Energy from this Pok\u00e9mon")
    targets = ctx.opponent_pokemon_in_play()
    if not targets:
        return
    target = await ctx.choose_pokemon(targets, "Choose 1 of your opponent's Pok\u00e9mon")
    if target is not None:
        await ctx.deal_damage(90, target=target, apply_modifiers=(target is ctx.defender))


card = PokemonToolCardDef(
    guid="f7a2e7e8-f18b-5d20-8e43-2f8a18506552",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RapidStrikeScrolloftheFlyingDragon.Name",
    display_name="Rapid Strike Scroll of the Flying Dragon",
    searchable_by=["Rapid Strike Scroll of the Flying Dragon", "Rapid Strike", "Item", "Pok\u00c3\u00a9mon Tool"],
    subtypes=["Rapid Strike", "Item", "Pok\u00e9mon Tool"],
    collector_number=153,
    set_code="SWSH7",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Attack(
            title="Meteor",
            game_text="Discard 2 Energy from this Pok\u00e9mon. This attack does 90 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.LIGHTNING: 1},
            effect=_meteor,
            condition=_is_rapid_strike,
        ),
    ],
)

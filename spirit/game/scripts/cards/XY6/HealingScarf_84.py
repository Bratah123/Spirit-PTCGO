from spirit.game.data_utils import PokemonToolCardDef, Ability, Triggers
from spirit.game.attributes import Rarities


async def _healing_scarf(ctx):
    """Whenever you attach an Energy card from your hand to this Pokemon, heal 20 damage from it."""
    if ctx.energy_receiver is not ctx.source or ctx.attaching_player_id != ctx.source.owning_player_id:
        return
    await ctx.heal(20, ctx.source)


card = PokemonToolCardDef(
    guid="3afe7f14-cec5-5487-b190-e53ffd5fbfa2",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HealingScarf.Name",
    display_name="Healing Scarf",
    searchable_by=["Healing Scarf", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=84,
    set_code="XY6",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Ability(
            title="Healing Scarf",
            game_text="Whenever you attach an Energy card from your hand to the Pok\u00e9mon this card is attached to, heal 20 damage from it.",
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=_healing_scarf,
        ),
    ]
)

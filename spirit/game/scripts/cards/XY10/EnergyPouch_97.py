from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import is_basic_energy_card


async def energy_pouch_on_ko(ctx):
    """Holder Knocked Out by damage from an opponent's attack: put all basic
    Energy that was attached to it into your hand."""
    discard = ctx.discard_pile(ctx.player_id)
    cards = [e for e in getattr(ctx, "ko_energies", []) or []
             if e in discard and is_basic_energy_card(e)]
    if cards:
        await ctx.put_in_hand(cards)


card = PokemonToolCardDef(
    guid="8067bf07-1cd5-588d-b3b2-dfd6ab99c2ff",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyPouch.Name",
    display_name="Energy Pouch",
    searchable_by=["Energy Pouch", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=97,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    on_carrier_knocked_out=energy_pouch_on_ko
)

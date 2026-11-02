from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.passives import TurnDamageModifier


async def plus_power(ctx):
    """During this turn, your Pokemon's attacks do 10 more damage to the
    Active Pokemon (before applying Weakness and Resistance)."""
    ctx.add_turn_damage_modifier(TurnDamageModifier(10, ctx.player_id))
    for pokemon in ctx.my_pokemon_in_play():
        await ctx.add_stat_visualization(
            pokemon, "Positive", "DamageDealtIncreased", card_text="+10 damage"
        )


card = ItemCardDef(
    guid="15ba7894-6949-50f2-ae3f-976e87d8615f",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PlusPower.Name",
    display_name="PlusPower",
    searchable_by=["PlusPower", "Item"],
    subtypes=["Item"],
    collector_number=96,
    set_code="BW1",
    rarity=Rarities.Uncommon,
    effect=plus_power,
)

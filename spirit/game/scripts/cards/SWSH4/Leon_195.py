from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.passives import TurnDamageModifier


async def leon_effect(ctx):
    """This turn, your Pokemon's attacks do 30 more damage to the opponent's Active (before W/R)."""
    ctx.add_turn_damage_modifier(TurnDamageModifier(30, ctx.player_id))
    for pokemon in ctx.my_pokemon_in_play():
        await ctx.add_stat_visualization(
            pokemon, "Positive", "DamageDealtIncreased", card_text="+30 damage"
        )


card = SupporterCardDef(
    guid="02ccdfeb-de31-52a4-88b5-3f88fd9295ff",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Leon.Name",
    display_name="Leon",
    searchable_by=["Leon", "Supporter"],
    subtypes=["Supporter"],
    collector_number=195,
    set_code="SWSH4",
    rarity=Rarities.RareRainbow,
    effect=leon_effect
)

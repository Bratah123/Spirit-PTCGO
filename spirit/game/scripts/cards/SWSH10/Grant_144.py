from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import AttrID, PokemonTypes, Rarities
from spirit.game.session.passives import TurnDamageModifier


async def grant(ctx):
    """This turn, your Fighting Pokemon's attacks do 30 more damage to the
    opponent's Active Pokemon (before W/R). (Discard-pile self-recovery
    clause needs Trainer PIE_ABILITIES support -- unscripted.)"""
    ctx.add_turn_damage_modifier(TurnDamageModifier(
        30, ctx.player_id,
        source_predicate=lambda p: PokemonTypes.FIGHTING.value in (
            p.get_attribute(AttrID.POKEMON_TYPES) or []),
    ))


card = SupporterCardDef(
    guid="a8f1995e-7be2-502c-a816-33872a499b32",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Grant.Name",
    display_name="Grant",
    searchable_by=["Grant", "Supporter"],
    subtypes=["Supporter"],
    collector_number=144,
    set_code="SWSH10",
    rarity=Rarities.Uncommon,
    effect=grant
)

from spirit.game.data_utils import PokemonToolCardDef, Ability, Triggers
from spirit.game.attributes import Rarities


async def _cursed_shovel_trigger(ctx):
    pokemon = ctx.source
    if ctx.damage_amount < ctx.pre_hit_hp:
        return
    attacker = ctx.damaged_by
    if attacker is None or attacker.owning_player_id == pokemon.owning_player_id:
        return
    await ctx.discard_cards(ctx.deck_top(2, player_id=ctx.opponent_id))


card = PokemonToolCardDef(
    guid="ca85413c-5592-5d35-bc93-723c6d0cc1d9",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CursedShovel.Name",
    display_name="Cursed Shovel",
    searchable_by=["Cursed Shovel", "Pok\u00c3\u00a9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=157,
    set_code="SWSH2",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Ability(
            title="Cursed Shovel",
            game_text="If the Pok\u00e9mon this card is attached to is Knocked Out by damage from an opponent's attack, discard the top 2 cards of your opponent's deck.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=_cursed_shovel_trigger,
        ),
    ],
)

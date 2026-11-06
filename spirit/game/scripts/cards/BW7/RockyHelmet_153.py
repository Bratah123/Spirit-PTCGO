from spirit.game.data_utils import PokemonToolCardDef, Ability, Triggers
from spirit.game.attributes import Rarities
from spirit.game.card_effects.passives_common import is_in_active_spot


async def _rocky_helmet_trigger(ctx):
    pokemon = ctx.source
    if not is_in_active_spot(pokemon):
        return
    attacker = ctx.damaged_by
    if attacker is None or attacker.owning_player_id == pokemon.owning_player_id:
        return
    await ctx.deal_damage(20, target=attacker, apply_modifiers=False, as_counters=True)


card = PokemonToolCardDef(
    guid="a91c2c3a-e8ff-5fcb-bfd0-da0b4eb7151f",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RockyHelmet.Name",
    display_name="Rocky Helmet",
    searchable_by=["Rocky Helmet", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=153,
    set_code="BW7",
    rarity=Rarities.RareSecret,
    granted_abilities=[
        Ability(
            title="Rocky Helmet",
            game_text="If the Pokémon this card is attached to is your Active Pokémon and is damaged by an attack from your opponent's Pokémon (even if that Pokémon is Knocked Out), put 2 damage counters on the Attacking Pokémon.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=_rocky_helmet_trigger,
        ),
    ],
)

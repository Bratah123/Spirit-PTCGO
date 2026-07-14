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
    guid="0bd49787-742b-52b6-ae1c-a3bc958c2f34",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RockyHelmet.Name",
    display_name="Rocky Helmet",
    searchable_by=["Rocky Helmet", "PokÃ©mon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=159,
    set_code="SWSH4",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Ability(
            title="Rocky Helmet",
            game_text="If the Pokémon this card is attached to is in the Active Spot and is damaged by an attack from your opponent's Pokémon (even if it is Knocked Out), put 2 damage counters on the Attacking Pokémon.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=_rocky_helmet_trigger,
        ),
    ],
)

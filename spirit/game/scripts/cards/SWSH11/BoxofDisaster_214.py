from spirit.game.data_utils import PokemonToolCardDef, Ability, Triggers, is_pokemon_v
from spirit.game.attributes import Rarities


async def box_of_disaster(ctx):
    """If the V holder had full HP and is Knocked Out by an opposing attack, put 8 counters on the attacker."""
    pokemon = ctx.source
    if not is_pokemon_v(pokemon.archetype_id):
        return
    if ctx.pre_hit_hp != ctx.max_hp(pokemon):
        return
    if ctx.damage_amount < ctx.pre_hit_hp:
        return
    attacker = ctx.damaged_by
    if attacker is None or attacker.owning_player_id == pokemon.owning_player_id:
        return
    await ctx.deal_damage(80, target=attacker, apply_modifiers=False, as_counters=True)


card = PokemonToolCardDef(
    guid="9bae7cf7-58df-5332-8607-39bf48170632",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BoxofDisaster.Name",
    display_name="Box of Disaster",
    searchable_by=["Box of Disaster", "Item", "Pokémon Tool"],
    subtypes=["Item", "Pokémon Tool"],
    collector_number=214,
    set_code="SWSH11",
    rarity=Rarities.RareSecret,
    granted_abilities=[
        Ability(
            title="Box of Disaster",
            game_text="If the Pokémon V this card is attached to has full HP and is Knocked Out by damage from an attack from your opponent's Pokémon, put 8 damage counters on the Attacking Pokémon.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=box_of_disaster,
        ),
    ],
)

from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.data_utils import Ability, Triggers
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.passives_common import is_in_active_spot


async def _poison_barb_trigger(ctx):
    pokemon = ctx.source
    if not is_in_active_spot(pokemon):
        return
    attacker = ctx.damaged_by
    if attacker is None or attacker.parent is None \
            or attacker.owning_player_id == pokemon.owning_player_id:
        return
    await ctx.apply_special_condition(attacker, SpecialConditions.POISONED)


card = PokemonToolCardDef(
    guid="b9cad71f-88b2-5d68-8769-ccc08ea903cf",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PoisonBarb.Name",
    display_name="Poison Barb",
    searchable_by=["Poison Barb", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=124,
    set_code="SM1",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Ability(
            title='Poison Barb',
            game_text="If the Pokémon this card is attached to is your Active Pokémon and is damaged by an opponent's attack (even if this Pokémon is Knocked Out), the Attacking Pokémon is now Poisoned.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=_poison_barb_trigger,
        ),
    ],
)

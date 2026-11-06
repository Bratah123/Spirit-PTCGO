from spirit.game.data_utils import PokemonToolCardDef, Ability, Triggers
from spirit.game.attributes import Rarities
from spirit.game.card_effects.passives_common import is_in_active_spot


async def _lucky_helmet_trigger(ctx):
    """Whenever the Pokemon this card is attached to is your Active Pokemon and
    is damaged by an opponent's attack, draw 2 cards."""
    pokemon = ctx.source
    if not is_in_active_spot(pokemon):
        return
    attacker = ctx.damaged_by
    if attacker is None or attacker.owning_player_id == pokemon.owning_player_id:
        return
    await ctx.draw_cards(2)


card = PokemonToolCardDef(
    guid="79c1619f-4224-537e-b42b-552570de9527",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LuckyHelmet.Name",
    display_name="Lucky Helmet",
    searchable_by=["Lucky Helmet", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=77,
    set_code="XY7",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Ability(
            title="Lucky Helmet",
            game_text="Whenever the Pok\u00e9mon this card is attached to is your Active Pok\u00e9mon and is damaged by an opponent's attack, draw 2 cards.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=_lucky_helmet_trigger,
        ),
    ],
)

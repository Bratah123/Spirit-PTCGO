from spirit.game.data_utils import PokemonToolCardDef, Ability, Triggers
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_basic_pokemon


async def _floral_crown(ctx):
    """At the end of your opponent's turn, heal 20 damage from the Basic Pokemon this card is attached to."""
    pokemon = ctx.source
    if ctx.session.turn_state.active_player_id in (None, pokemon.owning_player_id):
        return
    if is_basic_pokemon(pokemon):
        await ctx.heal(20, pokemon)


card = PokemonToolCardDef(
    guid="9ab49a52-5b8a-5019-9d63-c5e6a7855dd3",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FloralCrown.Name",
    display_name="Floral Crown",
    searchable_by=["Floral Crown", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=109,
    set_code="TwentiethAnn",
    rarity=Rarities.Common,
    granted_abilities=[
        Ability(
            title="Floral Crown",
            game_text="At the end of your opponent's turn, heal 20 damage from the Basic Pok\u00e9mon this card is attached to.",
            trigger=Triggers.BETWEEN_TURNS,
            effect=_floral_crown,
        ),
    ]
)

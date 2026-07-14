from spirit.game.data_utils import PokemonToolCardDef, Ability, Triggers
from spirit.game.attributes import Rarities, PokemonTypes, SpecialConditions, AttrID
from spirit.game.card_effects.passives_common import is_in_active_spot


async def _burning_scarf_trigger(ctx):
    pokemon = ctx.source
    types = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
    if PokemonTypes.FIRE.value not in types or not is_in_active_spot(pokemon):
        return
    await ctx.apply_special_condition(ctx.damaged_by, SpecialConditions.BURNED)


card = PokemonToolCardDef(
    guid="1c9666f9-be63-52b0-bd4e-ca7d86810e73",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BurningScarf.Name",
    display_name="Burning Scarf",
    searchable_by=["Burning Scarf", "Pok\u00c3\u00a9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=155,
    set_code="SWSH2",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Ability(
            title="Burning Scarf",
            game_text="If the Fire Pok\u00e9mon this card is attached to is in the Active Spot and is damaged by an opponent's attack (even if it is Knocked Out), the Attacking Pok\u00e9mon is now Burned.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=_burning_scarf_trigger,
        ),
    ],
)

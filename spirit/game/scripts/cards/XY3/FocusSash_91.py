from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities, AttrID, PokemonTypes
from spirit.game.card_effects.passives_common import GutsSurvivePassive
from spirit.game.session.passives import carrier_pokemon


class _FocusSash(GutsSurvivePassive):
    """Full-HP Fighting holder survives a KO hit at 10 HP; then discard this card."""
    def __init__(self):
        super().__init__(hp_floor=10, title="Focus Sash", flip=False, require_full_hp=True)

    async def damage_interceptor(self, ctx, calc, target, carrier):
        holder = carrier_pokemon(carrier)
        if holder is None or PokemonTypes.FIGHTING.value not in (
                holder.get_attribute(AttrID.POKEMON_TYPES) or []):
            return None
        result = await super().damage_interceptor(ctx, calc, target, carrier)
        if result is not None:
            await ctx.discard_cards([carrier])
        return result


card = PokemonToolCardDef(
    guid="aa83f6fc-449f-5100-9633-a1ff5d59271f",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FocusSash.Name",
    display_name="Focus Sash",
    searchable_by=["Focus Sash", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=91,
    set_code="XY3",
    rarity=Rarities.Uncommon,
    passive=_FocusSash()
)

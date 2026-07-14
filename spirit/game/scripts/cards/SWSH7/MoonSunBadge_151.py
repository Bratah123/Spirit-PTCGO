from spirit.game.data_utils import PokemonToolCardDef, def_for, is_pokemon_v
from spirit.game.attributes import Rarities, TrainerType
from spirit.game.session.passives import Passive, carrier_pokemon


class MoonSunBadgePassive(Passive):
    """An Espeon/Umbreon V holder is shielded from the effects an opposing
    Supporter card does to it."""

    def blocks_trainer_effects(self, affected_player_id, trainer_card,
                               trainer_type, carrier, affected_entity=None,
                               board=None):
        if trainer_type != TrainerType.SUPPORTER.value or affected_entity is None:
            return False
        holder = carrier_pokemon(carrier)
        if holder is None or holder is not carrier_pokemon(affected_entity):
            return False
        if not is_pokemon_v(holder.archetype_id):
            return False
        name = getattr(def_for(holder.archetype_id), "display_name", "") or ""
        return "Espeon" in name or "Umbreon" in name


card = PokemonToolCardDef(
    guid="292b0db0-0e61-56fc-b1ad-ce20eab2407a",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MoonSunBadge.Name",
    display_name="Moon & Sun Badge",
    searchable_by=["Moon & Sun Badge", "Item", "PokÃ©mon Tool"],
    subtypes=["Item", "Pokémon Tool"],
    collector_number=151,
    set_code="SWSH7",
    rarity=Rarities.Uncommon,
    passive=MoonSunBadgePassive(),
)

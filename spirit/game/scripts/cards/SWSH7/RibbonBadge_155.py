from spirit.game.data_utils import PokemonToolCardDef, is_pokemon_v, def_for
from spirit.game.attributes import Rarities
from spirit.game.session.passives import Passive, carrier_pokemon


class RibbonBadgePassive(Passive):
    def modify_prizes_for_knockout(self, pokemon, ctx, count, carrier):
        if carrier_pokemon(carrier) is not pokemon:
            return count
        if not is_pokemon_v(pokemon.archetype_id):
            return count
        definition = def_for(pokemon.archetype_id)
        name = getattr(definition, "display_name", "") or ""
        if "Sylveon" not in name:
            return count
        if not ctx.is_attack_effect() or ctx.player_id == pokemon.owning_player_id:
            return count
        return max(0, count - 1)


card = PokemonToolCardDef(
    guid="34e42b40-8244-5463-a3bb-931672c5d6de",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RibbonBadge.Name",
    display_name="Ribbon Badge",
    searchable_by=["Ribbon Badge", "Item", "PokÃ©mon Tool"],
    subtypes=["Item", "Pokémon Tool"],
    collector_number=155,
    set_code="SWSH7",
    rarity=Rarities.Uncommon,
    passive=RibbonBadgePassive(),
)

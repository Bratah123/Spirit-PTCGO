from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities, AttrID
from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects.pokemon import is_pokemon_vmax


class HerosMedalPassive(Passive):
    def max_hp_bonus(self, pokemon, carrier):
        if carrier_pokemon(carrier) is not pokemon:
            return 0
        return -100

    def modify_prizes_for_knockout(self, pokemon, ctx, count, carrier):
        if carrier_pokemon(carrier) is not pokemon:
            return count
        if not ctx.is_attack_effect() or ctx.player_id == pokemon.owning_player_id:
            return count
        return max(0, count - 1)


def _heros_medal_attach_to(pokemon):
    return is_pokemon_vmax(pokemon.archetype_id) and pokemon.get_attribute(AttrID.HP, 0) > 100


card = PokemonToolCardDef(
    guid="c2ea0f80-cb4b-5772-b86e-1f7490bbe80a",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HerosMedal.Name",
    display_name="Hero's Medal",
    searchable_by=["Hero's Medal", "Pok\u00c3\u00a9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=201,
    set_code="SWSH4",
    rarity=Rarities.RareSecret,
    attach_to=_heros_medal_attach_to,
    passive=HerosMedalPassive(),
)

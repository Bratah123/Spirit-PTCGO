from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.passives import Passive, carrier_pokemon


class BillowingSmokePassive(Passive):
    def prize_destination(self, pokemon, ctx, carrier):
        if carrier_pokemon(carrier) is not pokemon:
            return None
        if not ctx.is_attack_effect():
            return None
        attacker = getattr(ctx, "attacker", None)
        if attacker is None or attacker.owning_player_id == pokemon.owning_player_id:
            return None
        return "discard"


card = PokemonToolCardDef(
    guid="2508ef44-0afb-5957-8126-b92f2a37fd1e",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BillowingSmoke.Name",
    display_name="Billowing Smoke",
    searchable_by=["Billowing Smoke", "Pok\u00c3\u00a9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=158,
    set_code="SWSH3",
    rarity=Rarities.Uncommon,
    passive=BillowingSmokePassive()
)

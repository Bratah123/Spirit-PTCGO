from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.passives import Passive, carrier_pokemon


class RescueScarfPassive(Passive):
    """If the holder is Knocked Out by damage from an opponent's attack, the
    Pok\u00e9mon (and its pre-evolutions) go to hand; attachments still go to
    the discard pile (the engine routes non-Pok\u00e9mon cards there)."""

    def modify_prizes_for_knockout(self, pokemon, ctx, count, carrier):
        # Evaluated pre-move with the KO ctx: remember attack KOs only.
        if carrier_pokemon(carrier) is pokemon:
            attacker = getattr(ctx, "attacker", None)
            pokemon._rescue_scarf_ko = bool(
                ctx.is_attack_effect() and attacker is not None
                and attacker.owning_player_id != pokemon.owning_player_id)
        return count

    def knockout_destination(self, pokemon, carrier):
        if carrier_pokemon(carrier) is pokemon and getattr(pokemon, "_rescue_scarf_ko", False):
            pokemon._rescue_scarf_ko = False
            return "hand"
        return None


card = PokemonToolCardDef(
    guid="194759b5-60eb-5d11-96f9-7554d94329a1",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RescueScarf.Name",
    display_name="Rescue Scarf",
    searchable_by=["Rescue Scarf", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=115,
    set_code="BW6",
    rarity=Rarities.Uncommon,
    passive=RescueScarfPassive()
)

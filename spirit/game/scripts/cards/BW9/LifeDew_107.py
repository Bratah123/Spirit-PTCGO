from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.passives import Passive, carrier_pokemon


class LifeDewPassive(Passive):
    """ACE SPEC Tool: if the holder is Knocked Out by damage from an
    opponent's attack, the opponent takes 1 fewer Prize card."""

    def modify_prizes_for_knockout(self, pokemon, ctx, count, carrier):
        if pokemon is not carrier_pokemon(carrier) or ctx is None:
            return count
        attacker = getattr(ctx, "attacker", None)
        if (not ctx.is_attack_effect() or attacker is None
                or attacker.owning_player_id == pokemon.owning_player_id
                or pokemon.entity_id not in getattr(ctx, "attack_damage", {})):
            return count
        return max(0, count - 1)


card = PokemonToolCardDef(
    guid="691f6d4b-5916-5149-a203-625437431d99",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LifeDew.Name",
    display_name="Life Dew",
    searchable_by=["Life Dew", "Pok\u00e9mon Tool", "ACE SPEC"],
    subtypes=["Pok\u00e9mon Tool", "ACE SPEC"],
    collector_number=107,
    set_code="BW9",
    rarity=Rarities.Ace,
    # GAP: no AceSpecCardDef; ACE SPEC is a subtype flag only
    passive=LifeDewPassive()
)

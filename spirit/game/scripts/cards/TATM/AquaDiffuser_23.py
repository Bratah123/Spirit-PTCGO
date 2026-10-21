from spirit.game.data_utils import PokemonToolCardDef, Attack, ABILITIES_BY_ID
from spirit.game.attributes import Rarities, PokemonTypes, SpecialConditions
from spirit.game.content.definitions import def_for, ability_id_for
from spirit.game.session.passives import Passive, carrier_pokemon


_GUID = "c373ff38-28c1-5aee-9e52-dee864ade3ce"


def _team(p, team):
    name = getattr(def_for(p.archetype_id), "display_name", "") or ""
    return name.startswith("Team " + team + "'s ")


async def _effect(ctx):
    """The opponent's Active Pokemon is now Confused and Poisoned."""
    d = ctx.opponent_active()
    if d is not None:
        await ctx.apply_special_condition(d, SpecialConditions.CONFUSED)
        await ctx.apply_special_condition(d, SpecialConditions.POISONED)


AQUA_DIFFUSER = Attack(
    title="Aqua Diffuser",
    game_text="Your opponent's Active Pok\u00e9mon is now Confused and Poisoned.",
    cost={PokemonTypes.WATER: 1},
    damage=0,
    effect=_effect,
)
AQUA_DIFFUSER.ability_id = ability_id_for(_GUID, 0)
AQUA_DIFFUSER.is_granted = True
ABILITIES_BY_ID[AQUA_DIFFUSER.ability_id] = AQUA_DIFFUSER


class _Grant(Passive):
    """The Team Aqua Pokemon this card is attached to can also use the attack on this card."""
    def granted_attacks(self, board, pokemon, carrier):
        if carrier_pokemon(carrier) is not pokemon or not _team(pokemon, "Aqua"):
            return []
        return [AQUA_DIFFUSER]


card = PokemonToolCardDef(
    guid="c373ff38-28c1-5aee-9e52-dee864ade3ce",
    key="TATM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AquaDiffuser.Name",
    display_name="Aqua Diffuser",
    searchable_by=["Aqua Diffuser", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=23,
    set_code="TATM",
    rarity=Rarities.Uncommon,
    passive=_Grant()
)

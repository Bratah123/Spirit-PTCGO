from spirit.game.data_utils import PokemonToolCardDef, Attack, ABILITIES_BY_ID
from spirit.game.attributes import Rarities, PokemonTypes
from spirit.game.content.definitions import def_for, ability_id_for
from spirit.game.session.passives import Passive, carrier_pokemon


_GUID = "9f942b95-906b-59dc-8b63-2af80c264569"


async def _g_booster(ctx):
    """200 damage that isn't affected by any effects on the Defending Pokemon;
    discard 2 Energy attached to this Pokemon."""
    await ctx.deal_damage(ignore_target_effects=True)
    n = min(2, len(ctx.attached_energies(ctx.attacker)))
    if n:
        await ctx.discard_energy_from(ctx.attacker, n, minimum=n)


G_BOOSTER = Attack(
    title="G Booster",
    game_text="Discard 2 Energy attached to this Pok\u00e9mon. This attack's damage isn't affected by any effects on the Defending Pok\u00e9mon.",
    cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
    damage=200,
    effect=_g_booster,
)
G_BOOSTER.ability_id = ability_id_for(_GUID, 0)
G_BOOSTER.is_granted = True
ABILITIES_BY_ID[G_BOOSTER.ability_id] = G_BOOSTER


class _GenesectGrantPassive(Passive):
    """The Genesect-EX this card is attached to can also use the attack on
    this card (Energy cost still applies)."""

    def __init__(self, attack):
        self.attack = attack

    def granted_attacks(self, board, pokemon, carrier):
        if carrier_pokemon(carrier) is not pokemon:
            return []
        if getattr(def_for(pokemon.archetype_id), "display_name", "") != "Genesect-EX":
            return []
        return [self.attack]


card = PokemonToolCardDef(
    guid="9f942b95-906b-59dc-8b63-2af80c264569",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GBooster.Name",
    display_name="G Booster",
    searchable_by=["G Booster", "Pok\u00e9mon Tool", "ACE SPEC", "Team Plasma"],
    subtypes=["Pok\u00e9mon Tool", "ACE SPEC", "Team Plasma"],
    collector_number=92,
    set_code="BW10",
    rarity=Rarities.Ace,
    # GAP: no AceSpecCardDef; ACE SPEC is a subtype flag only
    passive=_GenesectGrantPassive(G_BOOSTER)
)

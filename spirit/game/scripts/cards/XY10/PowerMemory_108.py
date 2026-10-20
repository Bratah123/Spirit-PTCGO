from spirit.game.data_utils import PokemonToolCardDef, Attack, ABILITIES_BY_ID
from spirit.game.attributes import Rarities, PokemonTypes
from spirit.game.content.definitions import def_for, ability_id_for
from spirit.game.session.passives import Passive, carrier_pokemon


_GUID = "3ea92e06-a056-54ae-a05d-99ccf7955aba"


async def _all_cells_burn(ctx):
    """200 damage; discard 3 Energy attached to this Pokemon."""
    await ctx.deal_damage()
    n = min(3, len(ctx.attached_energies(ctx.attacker)))
    if n:
        await ctx.discard_energy_from(ctx.attacker, n, minimum=n)


ALL_CELLS_BURN = Attack(
    title="All Cells Burn",
    game_text="Discard 3 Energy attached to this Pok\u00e9mon.",
    cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
    damage=200,
    effect=_all_cells_burn,
)
ALL_CELLS_BURN.ability_id = ability_id_for(_GUID, 0)
ALL_CELLS_BURN.is_granted = True
ABILITIES_BY_ID[ALL_CELLS_BURN.ability_id] = ALL_CELLS_BURN


class _PowerMemory(Passive):
    """The Zygarde-EX this card is attached to can also use the attack on this card."""
    def granted_attacks(self, board, pokemon, carrier):
        if carrier_pokemon(carrier) is not pokemon:
            return []
        if getattr(def_for(pokemon.archetype_id), "display_name", "") != "Zygarde-EX":
            return []
        return [ALL_CELLS_BURN]


card = PokemonToolCardDef(
    guid="3ea92e06-a056-54ae-a05d-99ccf7955aba",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PowerMemory.Name",
    display_name="Power Memory",
    searchable_by=["Power Memory", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=108,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    passive=_PowerMemory()
)

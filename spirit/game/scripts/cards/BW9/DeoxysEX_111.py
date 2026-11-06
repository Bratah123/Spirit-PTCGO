from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.passives_common import team_damage_boost_passive
from spirit.game.session.effects import is_team_plasma_pokemon, plasma_energy_attached
from spirit.game.content.definitions import def_for
from spirit.game.card_effects.attacks_common import count_energy


def _named(pokemon, name):
    d = def_for(pokemon.archetype_id) if pokemon is not None else None
    return getattr(d, "display_name", "") == name


def _power_connect_attacker(pokemon):
    """Your Team Plasma Pokemon (excluding Deoxys-EX); copies stack."""
    return is_team_plasma_pokemon(pokemon) and not _named(pokemon, "Deoxys-EX")


_defender_energy = count_energy("defender")


async def _helix_force(ctx):
    """If this Pokemon has any Plasma Energy attached, 30 more damage for each
    Energy attached to the Defending Pokemon."""
    bonus = 30 * _defender_energy(ctx) if plasma_energy_attached(ctx.attacker) else 0
    await ctx.deal_damage(ctx.ability.damage + bonus)


card = PokemonCardDef(
    guid="fec05193-bd18-57e2-bf8d-9c67a0a8560b",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DeoxysEX.Name",
    display_name="Deoxys-EX",
    searchable_by=["Deoxys-EX", "Basic", "EX", "Team Plasma", "DeoxysEX"],
    subtypes=["Basic", "EX", "Team Plasma"],
    collector_number=111,
    set_code="BW9",
    rarity=Rarities.RareUltra,
    hp=170,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=386,
    abilities=[
        Ability(
            title="Power Connect",
            game_text="Your Team Plasma Pok\u00e9mon's attacks (excluding Deoxys-EX) do 10 more damage to the Active Pok\u00e9mon (before applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=team_damage_boost_passive(10, attacker_pred=_power_connect_attacker),
        ),
        Attack(
            title="Helix Force",
            game_text="If this Pok\u00e9mon has any Plasma Energy attached to it, this attack does 30 more damage for each Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=_helix_force,
        ),
    ],
)
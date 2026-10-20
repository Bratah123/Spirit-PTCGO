from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.content.definitions import def_for


def _is_pokemon_ex(pokemon):
    d = def_for(pokemon.archetype_id) if pokemon is not None else None
    return bool(d) and "EX" in (getattr(d, "subtypes", None) or [])


class _SteelSlashShield(Passive):
    def prevents_damage(self, calc, carrier):
        return bool(calc.is_attack and calc.is_opposing and carrier_pokemon(carrier) is calc.target
                    and _is_pokemon_ex(calc.attacker))


async def _steel_slash(ctx):
    """Printed damage; during your opponent's next turn prevent all damage done
    to this Pokemon by attacks from Pokemon-EX."""
    await ctx.deal_damage()
    ctx.add_passive_through_opponents_turn(ctx.attacker, _SteelSlashShield())


card = PokemonCardDef(
    guid="a68fe77c-62d4-54ca-a0c7-c28e9e3ca118",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scizor.Name",
    display_name="Scizor",
    searchable_by=["Scizor", "Stage 1", "Scizor"],
    subtypes=["Stage 1"],
    collector_number=94,
    set_code="BW7",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Scyther.Name",
    family_id=123,
    abilities=[
        Attack(
            title="Steel Slash",
            game_text="During your opponent's next turn, prevent all damage done to this Pok\u00e9mon by attacks from Pok\u00e9mon-EX.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=_steel_slash,
        ),
        Attack(
            title="Slashing Strike",
            game_text="This Pok\u00e9mon can't use Slashing Strike during your next turn.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=None,
            locks_next_turn=True,
        ),
    ],
)
from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import Passive, carrier_pokemon


async def _harden(ctx):
    ctx.add_passive_through_opponents_turn(ctx.attacker, _HardenPassive())


class _HardenPassive(Passive):
    """Prevent attack damage of 60 or less (after W/R) done to this Pokemon."""

    def prevents_damage(self, calc, carrier):
        return bool(calc.is_attack and calc.is_opposing
                    and carrier_pokemon(carrier) is calc.target
                    and calc.amount <= 60)


card = PokemonCardDef(
    guid="4d9b56fd-aa00-5eba-abef-66f75c68913f",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nuzleaf.Name",
    display_name="Nuzleaf",
    searchable_by=["Nuzleaf", "Stage 1", "Nuzleaf"],
    subtypes=["Stage 1"],
    collector_number=10,
    set_code="XY11",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Seedot.Name",
    family_id=273,
    abilities=[
        Attack(
            title="Harden",
            game_text="During your opponent's next turn, if this Pok\u00e9mon would be damaged by an attack, prevent that attack's damage done to this Pok\u00e9mon if that damage is 60 or less.",
            cost={PokemonTypes.GRASS: 1},
            effect=_harden,
        ),
        Attack(
            title="Razor Leaf",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import Passive, carrier_pokemon


class _HardenPassive(Passive):
    """Prevent attack damage of 60 or less (after W/R) done to this Pokemon."""

    def prevents_damage(self, calc, carrier):
        return bool(calc.is_attack and calc.is_opposing
                    and carrier_pokemon(carrier) is calc.target
                    and calc.amount <= 60)


async def _harden(ctx):
    ctx.add_passive_through_opponents_turn(ctx.attacker, _HardenPassive())


card = PokemonCardDef(
    guid="288a0583-699d-5828-8abb-7a1370a5da69",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Silcoon.Name",
    display_name="Silcoon",
    searchable_by=["Silcoon", "Stage 1", "Silcoon"],
    subtypes=["Stage 1"],
    collector_number=7,
    set_code="BW6",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wurmple.Name",
    family_id=265,
    abilities=[
        Attack(
            title="Harden",
            game_text="During your opponent's next turn, if this Pok\u00e9mon would be damaged by an attack, prevent that attack's damage done to this Pok\u00e9mon if that damage is 60 or less.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_harden,
        ),
        Attack(
            title="Bug Bite",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)
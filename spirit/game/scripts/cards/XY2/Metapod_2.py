from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import Passive, carrier_pokemon


class AdaptiveEvolutionPassive(Passive):
    def may_evolve_early(self, pokemon, carrier):
        return carrier_pokemon(carrier) is pokemon


async def _harden(ctx):
    ctx.add_passive_through_opponents_turn(ctx.attacker, _HardenPassive())


class _HardenPassive(Passive):
    """Prevent attack damage of 60 or less (after W/R) done to this Pokemon."""

    def prevents_damage(self, calc, carrier):
        return bool(calc.is_attack and calc.is_opposing
                    and carrier_pokemon(carrier) is calc.target
                    and calc.amount <= 60)


card = PokemonCardDef(
    guid="3ff96604-752e-58a2-b3d2-b16bfd788065",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Metapod.Name",
    display_name="Metapod",
    searchable_by=["Metapod", "Stage 1", "Metapod"],
    subtypes=["Stage 1"],
    collector_number=2,
    set_code="XY2",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Caterpie.Name",
    family_id=10,
    abilities=[
        Ability(
            title="Adaptive Evolution",
            game_text="This Pok\u00e9mon can evolve during your first turn or the turn you play it.",
            passive=AdaptiveEvolutionPassive(),
        ),
        Attack(
            title="Harden",
            game_text="During your opponent's next turn, if this Pok\u00e9mon would be damaged by an attack, prevent that attack's damage done to this Pok\u00e9mon if that damage is 60 or less.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=_harden,
        ),
    ],
)
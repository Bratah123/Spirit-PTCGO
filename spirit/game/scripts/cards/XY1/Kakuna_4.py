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
    guid="7eb4fcd0-3bb8-53d2-89c8-f884cb1e83c8",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kakuna.Name",
    display_name="Kakuna",
    searchable_by=["Kakuna", "Stage 1", "Kakuna"],
    subtypes=["Stage 1"],
    collector_number=4,
    set_code="XY1",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Weedle.Name",
    family_id=13,
    abilities=[
        Attack(
            title="Harden",
            game_text="During your opponent's next turn, if this Pok\u00e9mon would be damaged by an attack, prevent that attack's damage done to this Pok\u00e9mon if that damage is 60 or less.",
            cost={PokemonTypes.GRASS: 1},
            effect=_harden,
        ),
    ],
)
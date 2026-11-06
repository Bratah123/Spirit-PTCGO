from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import Passive, carrier_pokemon


class _ShellProtection(Passive):
    """Prevent attack damage of 50 or less done to this Pokemon."""
    def prevents_damage(self, calc, carrier):
        return (calc.is_attack and calc.is_opposing and calc.target is carrier_pokemon(carrier)
                and 0 < calc.amount <= 50)


async def _shell_protection(ctx):
    await ctx.deal_damage()
    ctx.add_passive_through_opponents_turn(ctx.attacker, _ShellProtection())


card = PokemonCardDef(
    guid="e0193a99-0d26-513b-8328-498e4151e5a5",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Clamperl.Name",
    display_name="Clamperl",
    searchable_by=["Clamperl", "Basic", "Clamperl"],
    subtypes=["Basic"],
    collector_number=49,
    set_code="XY5",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=366,
    abilities=[
        Attack(
            title="Shell Protection",
            game_text="During your opponent's next turn, if this Pok\u00e9mon would be damaged by an attack, prevent that attack's damage done to this Pok\u00e9mon if that damage is 50 or less.",
            cost={PokemonTypes.WATER: 1},
            effect=_shell_protection,
        ),
    ],
)
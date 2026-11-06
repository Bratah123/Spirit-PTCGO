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
    guid="6a486970-8f83-5635-be1c-c1f44c421ea6",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Onix.Name",
    display_name="Onix",
    searchable_by=["Onix", "Basic", "Onix"],
    subtypes=["Basic"],
    collector_number=61,
    set_code="XY12",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=95,
    abilities=[
        Attack(
            title="Harden",
            game_text="During your opponent's next turn, if this Pok\u00e9mon would be damaged by an attack, prevent that attack's damage done to this Pok\u00e9mon if that damage is 60 or less.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=_harden,
        ),
        Attack(
            title="Rock Throw",
            cost={PokemonTypes.FIGHTING: 2},
            damage=40,
        ),
    ],
)
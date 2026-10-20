from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.attacks_common import ignore_effects_attack
from spirit.game.session.passives import Passive


async def blockface(ctx):
    """70. During your opponent's next turn, prevent all damage done to this
    Pokemon by attacks from Basic Pokemon."""
    await ctx.deal_damage()
    ctx.add_passive_through_opponents_turn(ctx.attacker, BlockfacePassive())


class BlockfacePassive(Passive):
    """Prevent all damage from attacks by Basic Pokemon."""

    def prevents_damage(self, calc, carrier):
        return (
            calc.is_attack
            and calc.is_opposing
            and calc.target is carrier
            and calc.attacker is not None
            and calc.attacker.get_attribute(AttrID.STAGE) == PokemonStage.BASIC.value
        )


card = PokemonCardDef(
    guid="decd5fd4-92b6-5f8f-9a14-88d121cbb7c6",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.JolteonEX.Name",
    display_name="Jolteon-EX",
    searchable_by=["Jolteon-EX", "Basic", "EX", "JolteonEX"],
    subtypes=["Basic", "EX"],
    collector_number=116,
    set_code="TwentiethAnn",
    rarity=Rarities.RareUltra,
    hp=160,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=135,
    abilities=[
        Attack(
            title="Swift",
            game_text="This attack's damage isn't affected by Weakness, Resistance, or any other effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
            effect=ignore_effects_attack(ignore_weakness=True, ignore_resistance=True),
        ),
        Attack(
            title="Flash Ray",
            game_text="During your opponent's next turn, prevent all damage done to this Pok\u00e9mon by attacks from Basic Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=blockface,
        ),
    ],
)
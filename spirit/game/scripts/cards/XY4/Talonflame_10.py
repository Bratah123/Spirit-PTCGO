from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.session.passives import Passive, carrier_pokemon


class _JetShootExposed(Passive):
    """Attack damage to this Pokemon is increased by 40 (after W/R)."""
    def modify_damage_taken(self, calc, carrier):
        if calc.is_attack and calc.amount > 0 and calc.target is carrier_pokemon(carrier):
            calc.amount += 40


async def _jet_shoot(ctx):
    await ctx.deal_damage()
    ctx.add_passive_through_opponents_turn(ctx.attacker, _JetShootExposed())


card = PokemonCardDef(
    guid="8e25ad80-2455-5457-bbb0-d7ccdc8674da",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Talonflame.Name",
    display_name="Talonflame",
    searchable_by=["Talonflame", "Stage 2", "Talonflame"],
    subtypes=["Stage 2"],
    collector_number=10,
    set_code="XY4",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Fletchinder.Name",
    family_id=661,
    abilities=[
        Attack(
            title="Acrobatics",
            game_text="Flip 2 coins. This attack does 30 more damage for each heads.",
            cost={PokemonTypes.FIRE: 1},
            damage=30,
            damage_operator="+",
            effect=flip_damage(coins=2, bonus_per_heads=30),
        ),
        Attack(
            title="Jet Shoot",
            game_text="During your opponent's next turn, any damage done to this Pok\u00e9mon by attacks is increased by 40 (after applying Weakness and Resistance).",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=_jet_shoot,
        ),
    ],
)
from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.session.passives import Passive, carrier_pokemon


class _FluffyTagBoost(Passive):
    """During your next turn this Pokemon's attacks do 40 more damage to the
    opponent's Active (before Weakness and Resistance)."""

    def modify_damage_dealt(self, calc, carrier):
        if (calc.is_attack and calc.is_opposing and calc.to_active and calc.amount > 0
                and calc.attacker is carrier_pokemon(carrier)):
            calc.amount += 40


async def _fluffy_tag(ctx):
    """Switch this Pokemon with 1 of your Benched Pokemon; during your next
    turn the new Active's attacks do 40 more damage to the Active Pokemon."""
    bench = ctx.my_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(bench, "Choose your new Active Pok\u00e9mon")
    target = target or bench[0]
    await ctx.switch_active(ctx.player_id, target)
    ctx.add_passive_through_own_next_turn(target, _FluffyTagBoost())


card = PokemonCardDef(
    guid="d406af99-4832-5040-8262-b6ee1344db1f",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Whimsicott.Name",
    display_name="Whimsicott",
    searchable_by=["Whimsicott", "Stage 1", "Whimsicott"],
    subtypes=["Stage 1"],
    collector_number=15,
    set_code="BW7",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cottonee.Name",
    family_id=546,
    abilities=[
        Attack(
            title="Fluffy Tag",
            game_text="Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon. During your next turn, the attacks of that Pok\u00e9mon do 40 more damage to the Active Pok\u00e9mon (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_fluffy_tag,
        ),
        Attack(
            title="Stun Spore",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import lock_all_attacks
from spirit.game.card_effects.passives_common import condition_immunity_passive
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


async def _freeze_shock(ctx):
    """Printed damage; this Pokemon can't attack during your next turn."""
    await ctx.deal_damage()
    lock_all_attacks(ctx, ctx.attacker)


def _watered_teammate(target, carrier):
    return target.owning_player_id == carrier.owning_player_id and any(
        is_energy_card(e) and energy_provides_type(e, PokemonTypes.WATER.value)
        for e in target.children)


card = PokemonCardDef(
    guid="3db6faa8-68fa-5d77-a1c4-ebbc893a390f",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AurorusEX.Name",
    display_name="Aurorus-EX",
    searchable_by=["Aurorus-EX", "Basic", "EX", "AurorusEX"],
    subtypes=["Basic", "EX"],
    collector_number=102,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    family_id=699,
    abilities=[
        Ability(
            title="Frozen Charm",
            game_text="Each of your Pok\u00e9mon that has any Water Energy attached to it can't be Paralyzed. (If any of those Pok\u00e9mon are Paralyzed, remove that Special Condition.)",
            passive=condition_immunity_passive(SpecialConditions.PARALYZED, protects=_watered_teammate),
        ),
        Attack(
            title="Crystal Breath",
            game_text="This Pok\u00e9mon can't attack during your next turn.",
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=_freeze_shock,
        ),
    ],
)
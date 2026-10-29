from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


async def stick_and_absorb(ctx):
    """80 damage; heal 20; the Defending Pokémon can't retreat next turn."""
    await ctx.deal_damage()
    await ctx.heal(20, ctx.attacker)
    defender = ctx.defender
    if defender is not None and not ctx.effects_blocked(defender):
        ctx.lock_retreat(defender)


card = PokemonCardDef(
    guid="710be6ab-9eef-5bc8-8d2f-824988c86e5f",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Victreebel.Name",
    display_name="Victreebel",
    searchable_by=["Victreebel", "Stage 2", "Victreebel"],
    subtypes=["Stage 2"],
    collector_number=3,
    set_code="SM2",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Weepinbell.Name",
    family_id=69,
    abilities=[
        Attack(
            title="Pollen Hazard",
            game_text="Your opponent's Active Pok\u00e9mon is now Burned, Confused, and Poisoned.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=condition_attack(SpecialConditions.BURNED, SpecialConditions.CONFUSED, SpecialConditions.POISONED),
        ),
        Attack(
            title="Stick and Absorb",
            game_text="Heal 20 damage from this Pok\u00e9mon. The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=stick_and_absorb,
        ),
    ],
)
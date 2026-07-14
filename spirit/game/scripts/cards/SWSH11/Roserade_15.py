from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions, AttrID
from spirit.game.card_effects.attacks_common import condition_attack


async def assassins_rose(ctx):
    """60. If the opponent's Active is affected by a Special Condition,
    also do 60 to 1 of the opponent's Benched Pokemon (no W/R)."""
    defender = ctx.defender
    conditions = defender.get_attribute(AttrID.SPECIAL_CONDITIONS) if defender else None
    affected = bool(conditions)
    await ctx.deal_damage()
    if affected:
        bench = ctx.opponent_bench()
        if bench:
            target = await ctx.choose_pokemon(bench, "Choose 1 of your opponent's Benched Pokémon")
            if target is not None:
                await ctx.deal_damage(60, target=target, apply_modifiers=False)


card = PokemonCardDef(
    guid="0874fc18-71fa-5571-bf00-ce33b2b9defa",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Roserade.Name",
    display_name="Roserade",
    searchable_by=["Roserade", "Stage 1", "Roserade"],
    subtypes=["Stage 1"],
    collector_number=15,
    set_code="SWSH11",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Roselia.Name",
    family_id=315,
    abilities=[
        Attack(
            title="Poisonous Whip",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.POISONED),
        ),
        Attack(
            title="Assassin's Rose",
            game_text="If your opponent's Active Pok\u00e9mon is affected by a Special Condition, this attack also does 60 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=assassins_rose,
        ),
    ],
)
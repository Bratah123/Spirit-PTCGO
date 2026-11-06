from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes, SpecialConditions
from spirit.game.card_effects.attacks_common import flip_bonus


async def _sporprise(ctx):
    """On evolve from hand: you may make the opponent's Active Confused and Poisoned."""
    target = ctx.opponent_active()
    if target is None:
        return
    if not await ctx.ask_yes_no(
            "Use Sporprise? Your opponent's Active Pokémon is now Confused and Poisoned."):
        return
    await ctx.apply_special_condition(target, SpecialConditions.CONFUSED)
    await ctx.apply_special_condition(target, SpecialConditions.POISONED)


card = PokemonCardDef(
    guid="8c943f88-9d48-5caa-a51b-b2697d5b6809",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Amoonguss.Name",
    display_name="Amoonguss",
    searchable_by=["Amoonguss", "Stage 1", "Amoonguss"],
    subtypes=["Stage 1"],
    collector_number=9,
    set_code="BW4",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Foongus.Name",
    family_id=590,
    abilities=[
        Ability(
            title="Sporprise",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon, you may use this Ability. If you do, your opponent's Active Pok\u00e9mon is now Confused and Poisoned.",
            ability_type=AbilityTypes.POKE_ABILITY,
            trigger=Triggers.ON_EVOLVE,
            effect=_sporprise,
        ),
        Attack(
            title="Rising Lunge",
            game_text="Flip a coin. If heads, this attack does 30 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=flip_bonus(30),
        ),
    ],
)
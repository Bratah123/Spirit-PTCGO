from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


async def _gothic_fear(ctx):
    """On evolve from hand: you may leave both Active Pokemon Confused."""
    if not await ctx.ask_yes_no("Leave both Active Pokémon Confused?"):
        return
    for p in (ctx.my_active(), ctx.opponent_active()):
        if p is not None:
            await ctx.apply_special_condition(p, SpecialConditions.CONFUSED)


card = PokemonCardDef(
    guid="6d1afc96-49a5-5d18-bdef-4559b8c02305",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Haunter.Name",
    display_name="Haunter",
    searchable_by=["Haunter", "Stage 1", "Haunter"],
    subtypes=["Stage 1"],
    collector_number=59,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gastly.Name",
    family_id=92,
    abilities=[
        Ability(
            title="Gothic Fear",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon, you may leave both Active Pok\u00e9mon Confused.",
            trigger=Triggers.ON_EVOLVE,
            effect=_gothic_fear,
        ),
        Attack(
            title="Poison Ring",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned. That Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=condition_attack(SpecialConditions.POISONED, no_retreat=True),
        ),
    ],
)
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import flip_bonus


async def lethargy_spores(ctx):
    """On evolve: you may make both Active Pokemon Asleep and Poisoned."""
    if not await ctx.ask_yes_no("Make both Active Pokémon Asleep and Poisoned?"):
        return
    for target in (ctx.my_active(), ctx.opponent_active()):
        if target is None:
            continue
        await ctx.apply_special_condition(target, SpecialConditions.ASLEEP)
        await ctx.apply_special_condition(target, SpecialConditions.POISONED)

card = PokemonCardDef(
    guid="ed449976-a244-5eda-9c4b-493f8e47ce51",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Parasect.Name",
    display_name="Parasect",
    searchable_by=["Parasect", "Stage 1", "Parasect"],
    subtypes=["Stage 1"],
    collector_number=5,
    set_code="SWSH11",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Paras.Name",
    family_id=46,
    abilities=[
        Ability(
            title="Lethargy Spores",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may make both Active Pok\u00e9mon Asleep and Poisoned.",
            trigger=Triggers.ON_EVOLVE,
            effect=lethargy_spores,
        ),
        Attack(
            title="X-Scissor",
            game_text="Flip a coin. If heads, this attack does 50 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="+",
            effect=flip_bonus(50),
        ),
    ],
)
from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.passives_common import apply_defender_attack_cost_raise, apply_defender_retreat_cost_raise
from spirit.game.card_effects.attacks_common import condition_attack


async def chomp_chomp_hold(ctx):
    """During your opponent's next turn, the Defending Pokemon's attacks
    cost [C] more, and its Retreat Cost is [C] more."""
    await ctx.deal_damage()
    await apply_defender_attack_cost_raise(ctx, 1)
    await apply_defender_retreat_cost_raise(ctx, 1)


card = PokemonCardDef(
    guid="46531862-b540-5974-ad37-a1e93d0f849c",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gastrodon.Name",
    display_name="Gastrodon",
    searchable_by=["Gastrodon", "Stage 1", "Gastrodon"],
    subtypes=["Stage 1"],
    collector_number=29,
    set_code="XY11",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shellos.Name",
    family_id=422,
    abilities=[
        Attack(
            title="Sticky Shot",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon's attacks cost Colorless more, and its Retreat Cost is Colorless more.",
            cost={PokemonTypes.WATER: 1},
            damage=20,
            effect=chomp_chomp_hold,
        ),
        Attack(
            title="Water Pulse",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 3},
            damage=60,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)
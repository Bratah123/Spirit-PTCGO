from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.trainers import is_basic_energy_card


async def fling_fire(ctx):
    discarded = await ctx.discard_from_hand(
        2, minimum=0, predicate=is_basic_energy_card,
        prompt="Discard up to 2 basic Energy cards",
    )
    await ctx.deal_damage(60 * len(discarded))


card = PokemonCardDef(
    guid="fe6d1b3f-13c8-59d3-9701-e56aa2933627",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Simisear.Name",
    display_name="Simisear",
    searchable_by=["Simisear", "Stage 1", "Simisear"],
    subtypes=["Stage 1"],
    collector_number=38,
    set_code="SWSH8",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pansear.Name",
    family_id=513,
    abilities=[
        Attack(
            title="Light Punch",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Fling Fire",
            game_text="Discard up to 2 basic Energy cards from your hand. This attack does 60 damage for each card you discarded in this way.",
            cost={PokemonTypes.FIRE: 1},
            damage=60,
            damage_operator="x",
            effect=fling_fire,
        ),
    ],
)
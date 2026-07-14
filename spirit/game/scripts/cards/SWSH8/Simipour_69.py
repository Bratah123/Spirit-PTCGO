from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.session.effects import is_supporter_card


async def circus_soaking(ctx):
    """Opponent reveals their hand; 60 damage for each Supporter card there."""
    hand = await ctx.reveal_hand(of_player=ctx.opponent_id)
    count = sum(1 for c in hand if is_supporter_card(c))
    if count:
        await ctx.deal_damage(60 * count)

card = PokemonCardDef(
    guid="1ee72771-e075-5f79-9191-3bf8a805c6b4",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Simipour.Name",
    display_name="Simipour",
    searchable_by=["Simipour", "Stage 1", "Simipour"],
    subtypes=["Stage 1"],
    collector_number=69,
    set_code="SWSH8",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Panpour.Name",
    family_id=515,
    abilities=[
        Attack(
            title="Water Pulse",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 1},
            damage=20,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Circus Soaking",
            game_text="Your opponent reveals their hand. This attack does 60 damage for each Supporter card you find there.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="x",
            effect=circus_soaking,
        ),
    ],
)
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.pokemon import is_energy_card


async def searchlight_tail(ctx):
    """90 damage, +90 more if the opponent's revealed hand has an Energy card."""
    cards = await ctx.reveal_hand(ctx.opponent_id, ctx.player_id)
    amount = 90
    if any(is_energy_card(c) for c in cards):
        amount += 90
    await ctx.deal_damage(amount)


card = PokemonCardDef(
    guid="857c9944-4f37-5316-a64f-e92e9019d867",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ampharos.Name",
    display_name="Ampharos",
    searchable_by=["Ampharos", "Stage 2", "Ampharos"],
    subtypes=["Stage 2"],
    collector_number=49,
    set_code="SWSH6",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Flaaffy.Name",
    family_id=179,
    abilities=[
        Attack(
            title="Thunder Shock",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=50,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Searchlight Tail",
            game_text="Your opponent reveals their hand. If you find any Energy cards there, this attack does 90 more damage.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=90,
            damage_operator="+",
            effect=searchlight_tail,
        ),
    ],
)
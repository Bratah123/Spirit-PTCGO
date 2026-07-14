from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.pokemon import is_energy_card


async def ground_burn(ctx):
    """Each player discards the top card of their deck; +100 damage per
    Energy card discarded that way."""
    discarded = list(ctx.deck_top(1, player_id=ctx.player_id)) + \
        list(ctx.deck_top(1, player_id=ctx.opponent_id))
    await ctx.discard_cards(discarded)
    energy_count = sum(1 for c in discarded if is_energy_card(c))
    await ctx.deal_damage(80 + 100 * energy_count)


card = PokemonCardDef(
    guid="2ee86c9a-0c58-542d-8065-41fa646e8ab4",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magmortar.Name",
    display_name="Magmortar",
    searchable_by=["Magmortar", "Stage 1", "Magmortar"],
    subtypes=["Stage 1"],
    collector_number=30,
    set_code="SWSH2",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magmar.Name",
    family_id=126,
    abilities=[
        Attack(
            title="Burst Punch",
            game_text="Your opponent's Active Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.BURNED),
        ),
        Attack(
            title="Ground Burn",
            game_text="Each player discards the top card of their deck. This attack does 100 more damage for each Energy card discarded in this way.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            effect=ground_burn,
        ),
    ],
)
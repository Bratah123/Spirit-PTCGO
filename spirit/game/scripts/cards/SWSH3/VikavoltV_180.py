from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack
from spirit.game.session.effects import is_item_card


async def paralyzing_bolt(ctx):
    """50 damage. During your opponent's next turn, they can't play any Item
    cards from their hand."""
    await ctx.deal_damage()
    ctx.lock_plays(ctx.opponent_id, is_item_card)


card = PokemonCardDef(
    guid="09a65584-324e-5e4a-a62f-062639f24345",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.VikavoltV.Name",
    display_name="Vikavolt V",
    searchable_by=["Vikavolt V", "Basic", "V", "VikavoltV"],
    subtypes=["Basic", "V"],
    collector_number=180,
    set_code="SWSH3",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=738,
    abilities=[
        Attack(
            title="Paralyzing Bolt",
            game_text="During your opponent's next turn, they can't play any Item cards from their hand.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=paralyzing_bolt,
        ),
        Attack(
            title="Super Zap Cannon",
            game_text="Discard 2 Energy from this Pokémon.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=190,
            effect=self_energy_discard_attack(count=2),
        ),
    ],
)

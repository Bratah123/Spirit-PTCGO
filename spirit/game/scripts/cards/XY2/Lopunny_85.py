from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import remove_self_from_play
from spirit.game.card_effects.attacks_common import lock_all_attacks


async def power_rush(ctx):
    """120 damage. Flip a coin. If tails, this Pokémon can't attack during your next turn."""
    await ctx.deal_damage()
    heads = (await ctx.flip_coins(1, "Power Rush"))[0]
    if not heads:
        lock_all_attacks(ctx, ctx.attacker)


card = PokemonCardDef(
    guid="690c6029-bae0-5aae-8dcd-bb1d586144f3",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lopunny.Name",
    display_name="Lopunny",
    searchable_by=["Lopunny", "Stage 1", "Lopunny"],
    subtypes=["Stage 1"],
    collector_number=85,
    set_code="XY2",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Buneary.Name",
    family_id=427,
    abilities=[
        Ability(
            title="Big Jump",
            game_text="Once during your turn (before your attack), you may return this Pok\u00e9mon and all cards attached to it to your hand.",
            activation=Activations.ONCE_PER_TURN,
            effect=remove_self_from_play('hand'),
        ),
        Attack(
            title="Sitdown Bounce",
            game_text="Flip a coin. If tails, this Pok\u00e9mon can't attack during your next turn.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            effect=power_rush,
        ),
    ],
)
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import mill_attack


async def primeval_beak(ctx):
    """30 damage; during the opponent's next turn, Energy can't be attached
    from their hand to the Defending Pokémon."""
    await ctx.deal_damage()
    target = ctx.defender
    if target is not None and not ctx.effects_blocked(target):
        ctx.restrict_attachments(target)


card = PokemonCardDef(
    guid="054530ab-3af2-5f88-b55a-cf2d919d2780",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DracozoltV.Name",
    display_name="Dracozolt V",
    searchable_by=["Dracozolt V", "Basic", "V", "DracozoltV"],
    subtypes=["Basic", "V"],
    collector_number=178,
    set_code="SWSH7",
    rarity=Rarities.RareUltra,
    hp=220,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=880,
    abilities=[
        Attack(
            title="Primeval Beak",
            game_text="During your opponent's next turn, Energy cards can't be attached from your opponent's hand to the Defending Pokémon.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
            effect=primeval_beak,
        ),
        Attack(
            title="Mountain Swing",
            game_text="Discard the top 3 cards of your deck.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=180,
            effect=mill_attack(3, opponent=False),
        ),
    ],
)

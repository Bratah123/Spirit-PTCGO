from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if


async def rock_hurl(ctx):
    """50; this attack's damage isn't affected by Resistance."""
    await ctx.deal_damage(ignore_resistance=True)


def _more_hand_cards(ctx) -> bool:
    return ctx.hand_size() > ctx.hand_size(ctx.opponent_id)

card = PokemonCardDef(
    guid="9665df54-ad69-5f4b-b27e-02e1c8ff3111",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Barbaracle.Name",
    display_name="Barbaracle",
    searchable_by=["Barbaracle", "Stage 1", "Barbaracle"],
    subtypes=["Stage 1"],
    collector_number=104,
    set_code="SWSH2",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Binacle.Name",
    family_id=688,
    abilities=[
        Attack(
            title="Rock Hurl",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=rock_hurl,
        ),
        Attack(
            title="Hand Press",
            game_text="If you have more cards in your hand than your opponent, this attack does 80 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="+",
            effect=bonus_if(_more_hand_cards, 80),
        ),
    ],
)
from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage


async def _scout(ctx):
    """Your opponent reveals their hand."""
    await ctx.reveal_hand(ctx.opponent_id)


card = PokemonCardDef(
    guid="967c15b0-2fa9-5c58-84a9-8eb0c29057e8",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Munna.Name",
    display_name="Munna",
    searchable_by=["Munna", "Basic", "Munna"],
    subtypes=["Basic"],
    collector_number=39,
    set_code="XY4",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=517,
    abilities=[
        Attack(
            title="See Through",
            game_text="Your opponent reveals his or her hand.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=_scout,
        ),
        Attack(
            title="Double Headbutt",
            game_text="Flip 2 coins. This attack does 20 damage times the number of heads.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=flip_damage(2, per_heads=20),
        ),
    ],
)
from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.trainers import is_basic_energy_card


async def _positive_hand(ctx):
    """Discard a basic Energy card from your hand. If you do, draw 2."""
    if not any(is_basic_energy_card(c) for c in ctx.hand()):
        return
    picked = await ctx.discard_from_hand(1, minimum=1, predicate=is_basic_energy_card,
                                         prompt="Discard a basic Energy card")
    if picked:
        await ctx.draw_cards(2)


card = PokemonCardDef(
    guid="293a41af-6f07-5698-87f1-34ff09a2b93c",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Plusle.Name",
    display_name="Plusle",
    searchable_by=["Plusle", "Basic", "Plusle"],
    subtypes=["Basic"],
    collector_number=31,
    set_code="XY3",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=311,
    abilities=[
        Attack(
            title="Positive Hand",
            game_text="Discard a basic Energy card from your hand. If you do, draw 2 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_positive_hand,
        ),
        Attack(
            title="Electric Tail",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)
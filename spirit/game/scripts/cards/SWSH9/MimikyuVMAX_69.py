from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import place_counters, discard_random_from_hand


async def max_shadow(ctx):
    """120 damage; discard a random card from the opponent's hand."""
    await ctx.deal_damage()
    await discard_random_from_hand(ctx, player_id=ctx.opponent_id, count=1)

card = PokemonCardDef(
    guid="4982ce9a-4bdd-5895-9974-d3c4895a1dcd",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MimikyuVMAX.Name",
    display_name="Mimikyu VMAX",
    searchable_by=["Mimikyu VMAX", "VMAX", "MimikyuVMAX"],
    subtypes=["VMAX"],
    collector_number=69,
    set_code="SWSH9",
    rarity=Rarities.RareHoloVMAX,
    hp=300,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.VMAX,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MimikyuV.Name",
    family_id=778,
    abilities=[
        Attack(
            title="Ominous Numbers",
            game_text="Put 4 damage counters on your opponent's Pok\u00e9mon in any way you like. If you played Acerola's Premonition from your hand during this turn, place 13 damage counters instead.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=place_counters(
                lambda ctx: 13 if ctx.played_trainer_this_turn("Acerola's Premonition") else 4,
                "choose_any_opponent",
            ),
        ),
        Attack(
            title="Max Shadow",
            game_text="Discard a random card from your opponent's hand.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=120,
            effect=max_shadow,
        ),
    ],
)
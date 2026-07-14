from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_trainer_card
from spirit.game.card_effects.attacks_common import count_energy


async def gathering_food(ctx):
    """For each Energy attached to this Pokemon, search the deck for a
    Trainer card, reveal it, and put it into your hand. Then, shuffle."""
    n = count_energy("self")(ctx)
    if n <= 0:
        return
    picks = await ctx.search_deck(
        is_trainer_card, count=n, minimum=0,
        prompt=f"Choose up to {n} Trainer card(s) to put into your hand.",
    )
    await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="6650b0bd-2604-5224-9cc2-0ec89e4a6b43",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Durant.Name",
    display_name="Durant",
    searchable_by=["Durant", "Basic", "Durant"],
    subtypes=["Basic"],
    collector_number=132,
    set_code="SWSH2",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=632,
    abilities=[
        Attack(
            title="Gathering Food",
            game_text="For each Energy attached to this Pok\u00e9mon, search your deck for a Trainer card, reveal it, and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=gathering_food,
        ),
        Attack(
            title="Metal Claw",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)
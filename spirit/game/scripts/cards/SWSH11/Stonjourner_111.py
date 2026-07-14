from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.trainers import is_energy_card
from spirit.game.card_effects.support_common import distribute_energy


def _is_fighting_energy_card(card):
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_energy_card(card) and PokemonTypes.FIGHTING.value in types


async def power_stone(ctx):
    """Attach up to 2 Fighting Energy cards from your hand to your Pokemon in any way you like."""
    hand_fighting = [c for c in ctx.hand() if _is_fighting_energy_card(c)]
    if not hand_fighting:
        return
    picks = await ctx.choose_cards(
        hand_fighting, 2, minimum=0,
        prompt="Attach up to 2 Fighting Energy cards to your Pokémon.",
    )
    if not picks:
        return
    candidates = ctx.my_pokemon_in_play()
    if not candidates:
        return
    await distribute_energy(ctx, picks, candidates)


async def lost_shot(ctx):
    """120. Put the top card of your opponent's deck in the Lost Zone."""
    await ctx.deal_damage()
    top = ctx.deck_top(1, player_id=ctx.opponent_id)
    if top:
        await ctx.move_to_lost_zone(top)


card = PokemonCardDef(
    guid="9f5472cf-1f35-562d-af9d-7372d55adcb8",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Stonjourner.Name",
    display_name="Stonjourner",
    searchable_by=["Stonjourner", "Basic", "Stonjourner"],
    subtypes=["Basic"],
    collector_number=111,
    set_code="SWSH11",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    family_id=874,
    abilities=[
        Attack(
            title="Power Stone",
            game_text="Attach up to 2 Fighting Energy cards from your hand to your Pokémon in any way you like.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=power_stone,
        ),
        Attack(
            title="Lost Shot",
            game_text="Put the top card of your opponent's deck in the Lost Zone.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=120,
            effect=lost_shot,
        ),
    ],
)

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

from spirit.game.card_effects.sm10 import (
    wall_of_stone_passive,
)

async def deck_distiller(ctx):
    heads = await ctx.flip_until_tails("Deck Distiller")
    if heads <= 0:
        return
    top_cards = ctx.deck_top(heads, ctx.opponent_id)
    if top_cards:
        await ctx.discard_cards(top_cards)

card = PokemonCardDef(
    guid="5a81c427-f77e-5480-a1f9-98a04c933ec8",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Stakataka.Name",
    display_name="Stakataka",
    searchable_by=["Stakataka", "Basic", "Ultra Beast", "Stakataka"],
    subtypes=["Basic", "Ultra Beast"],
    collector_number=180,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    family_id=805,
    abilities=[
        Ability(
            title="Wall of Stone",
            game_text="If your opponent has 3 or fewer Prize cards remaining, this Pok\u00e9mon's maximum HP is 200.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=wall_of_stone_passive
        ),
        Attack(
            title="Top Down",
            game_text="Flip a coin until you get tails. For each heads, discard the top card of your opponent's deck.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=110,
            effect=deck_distiller,
        ),
    ],
)
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.trainers import is_basic_energy_card

from spirit.game.card_effects.sm8 import (
    fresh_squeezed,
)

async def _flower_supply(ctx):
    """40; attach 2 basic Energy cards from your discard pile to your Pokemon in any way you like."""
    await ctx.deal_damage()
    for _ in range(2):
        cards = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
        mine = ctx.my_pokemon_in_play()
        if not cards or not mine:
            return
        picks = await ctx.choose_cards(cards, 1, minimum=1, prompt="Choose a basic Energy card")
        if not picks:
            return
        target = mine[0] if len(mine) == 1 else await ctx.choose_pokemon(mine, "Attach it to which Pokémon?")
        await ctx.attach_energy(picks[0], target or mine[0])

card = PokemonCardDef(
    guid="d766af80-2f7b-598a-83e2-ace501a6ed18",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shuckle.Name",
    display_name="Shuckle",
    searchable_by=["Shuckle", "Basic", "Shuckle"],
    subtypes=["Basic"],
    collector_number=16,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=213,
    abilities=[
        Ability(
            title="Fresh Squeezed",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may search your deck for up to 3 basic Energy cards and discard them. Then, shuffle your deck.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=fresh_squeezed,
            trigger=Triggers.ON_PLAY,
        ),
        Attack(
            title="Energy Drink",
            game_text="Attach 2 basic Energy cards from your discard pile to your Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.GRASS: 1},
            effect=_flower_supply,
        ),
    ],
)
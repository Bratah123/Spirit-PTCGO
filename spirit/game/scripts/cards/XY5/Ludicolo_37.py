"""STUB: effect not implemented — do not guess mechanics.
Ludicolo (XY5 #37): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ancient_traits import ancient_trait


async def _astonish(ctx):
    """Choose a random card from your opponent's hand; they reveal it and
    shuffle it into their deck."""
    import random
    hand = ctx.hand(ctx.opponent_id)
    if not hand:
        return
    card = random.choice(hand)
    await ctx.reveal_cards([card])
    await ctx.shuffle_into_deck([card], ctx.opponent_id)


card = PokemonCardDef(
    guid="505dc3a7-af6f-585a-9439-c50342baeb2e",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ludicolo.Name",
    display_name="Ludicolo",
    searchable_by=["Ludicolo", "Stage 2", "Ludicolo"],
    subtypes=["Stage 2"],
    collector_number=37,
    set_code="XY5",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lombre.Name",
    family_id=270,
    abilities=[
        ancient_trait('α Recovery'),
        Attack(
            title="Astonish",
            game_text="Choose a random card from your opponent's hand. Your opponent reveals that card and shuffles it into his or her deck.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=_astonish,
        ),
        Attack(
            title="Splash Dance",
            game_text="During your next turn, this Pok\u00e9mon's Splash Dance attack does 60 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)
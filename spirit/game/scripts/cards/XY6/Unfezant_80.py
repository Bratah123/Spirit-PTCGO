from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.models.board import PokemonEntity


async def _strong_winds(ctx):
    """Shuffle all cards attached to each player's Pokemon into that player's deck."""
    await ctx.deal_damage()
    for pid, pokemon in ((ctx.player_id, ctx.my_pokemon_in_play()),
                         (ctx.opponent_id, ctx.opponent_pokemon_in_play())):
        cards = [c for p in pokemon for c in list(p.children) if not isinstance(c, PokemonEntity)]
        if cards:
            await ctx.shuffle_into_deck(cards, pid)


card = PokemonCardDef(
    guid="5960d499-327f-5316-b013-dd74925fd4f3",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Unfezant.Name",
    display_name="Unfezant",
    searchable_by=["Unfezant", "Stage 2", "Unfezant"],
    subtypes=["Stage 2"],
    collector_number=80,
    set_code="XY6",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tranquill.Name",
    family_id=519,
    abilities=[
        Attack(
            title="Quick Attack",
            game_text="Flip a coin. If heads, this attack does 30 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=flip_bonus(30),
        ),
        Attack(
            title="Strong Winds",
            game_text="Shuffle all cards attached to each player's Pok\u00e9mon into that player's deck.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=_strong_winds,
        ),
    ],
)
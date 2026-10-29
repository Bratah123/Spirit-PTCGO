from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.data_utils import Activations


async def _feather_arrow(ctx):
    """Once during your turn: put 2 damage counters on 1 of your opponent's Pokemon."""
    pool = ctx.opponent_pokemon_in_play()
    if not pool:
        return
    target = pool[0] if len(pool) == 1 else await ctx.choose_pokemon(
        pool, "Put 2 damage counters on which Pokémon?")
    if target is not None:
        await ctx.place_damage_counters(2, [target])


async def _hollow_hunt(ctx):
    """Put 3 cards from your discard pile into your hand."""
    cards = list(ctx.discard_pile())
    if not cards:
        return
    n = min(3, len(cards))
    picks = await ctx.choose_cards(cards, n, minimum=n,
                                   prompt="Choose 3 cards to put into your hand.")
    await ctx.put_in_hand(picks, reveal=True)


card = PokemonCardDef(
    guid="e53d8005-b0e8-5c3f-9556-5b3bbd207c34",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DecidueyeGX.Name",
    display_name="Decidueye-GX",
    searchable_by=["Decidueye-GX", "Stage 2", "GX", "DecidueyeGX"],
    subtypes=["Stage 2", "GX"],
    collector_number=146,
    set_code="SM2",
    rarity=Rarities.RareRainbow,
    hp=240,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dartrix.Name",
    family_id=722,
    abilities=[
        Ability(
            title="Feather Arrow",
            game_text="Once during your turn (before your attack), you may put 2 damage counters on 1 of your opponent's Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            activation=Activations.ONCE_PER_TURN,
            effect=_feather_arrow,
        ),
        Attack(
            title="Razor Leaf",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
        ),
        Attack(
            title="Hollow Hunt-GX",
            game_text="Put 3 cards from your discard pile into your hand. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.GRASS: 1},
            effect=_hollow_hunt,
        ),
    ],
)
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def night_footsteps(ctx):
    """Choose 2 of your opponent's Pokemon and put 2 damage counters on each."""
    candidates = ctx.opponent_pokemon_in_play()
    if not candidates:
        return
    count = min(2, len(candidates))
    targets = await ctx.choose_cards(
        candidates, count, prompt="Choose 2 of your opponent's Pokémon"
    )
    for target in targets:
        await ctx.deal_damage(20, target=target, apply_modifiers=False, as_counters=True)


card = PokemonCardDef(
    guid="6876c033-5158-5bb9-b7fd-51b525cb65b1",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spectrier.Name",
    display_name="Spectrier",
    searchable_by=["Spectrier", "Basic", "Spectrier"],
    subtypes=["Basic"],
    collector_number=81,
    set_code="SWSH11",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=897,
    abilities=[
        Attack(
            title="Night Footsteps",
            game_text="Choose 2 of your opponent's Pok\u00e9mon and put 2 damage counters on each of them.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=night_footsteps,
        ),
        Attack(
            title="Phantom Strike",
            game_text="During your next turn, this Pok\u00e9mon can't use Phantom Strike.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            locks_next_turn=True,
        ),
    ],
)
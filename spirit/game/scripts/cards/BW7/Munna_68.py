from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes, SpecialConditions


async def _long_distance_hypnosis(ctx):
    """Flip a coin. Heads: your opponent's Active is Asleep. Tails: your Active is Asleep."""
    results = await ctx.flip_coins(1, "Long-Distance Hypnosis")
    target = ctx.opponent_active() if results and results[0] else ctx.my_active()
    if target is not None and not ctx.effects_blocked(target):
        await ctx.apply_special_condition(target, SpecialConditions.ASLEEP)


card = PokemonCardDef(
    guid="84d781a9-306b-5923-b098-889669e17382",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Munna.Name",
    display_name="Munna",
    searchable_by=["Munna", "Basic", "Munna"],
    subtypes=["Basic"],
    collector_number=68,
    set_code="BW7",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=517,
    abilities=[
        Ability(
            title="Long-Distance Hypnosis",
            game_text="Once during your turn (before your attack), you may flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Asleep. If tails, your Active Pok\u00e9mon is now Asleep.",
            ability_type=AbilityTypes.POKE_ABILITY,
            activation=Activations.ONCE_PER_TURN,
            effect=_long_distance_hypnosis,
        ),
        Attack(
            title="Psyshot",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
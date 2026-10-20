from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.trainers import is_basic_energy_card


async def _energy_color(ctx):
    """Flip a coin. If heads, search for a basic Energy and attach it to 1 of your Pokemon. Shuffle."""
    results = await ctx.flip_coins(1, ctx.ability.title)
    if results and results[0]:
        picks = await ctx.search_deck(is_basic_energy_card, count=1, minimum=0, prompt="Choose a basic Energy card")
        if picks:
            mine = ctx.my_pokemon_in_play()
            target = mine[0] if len(mine) == 1 else await ctx.choose_pokemon(mine, "Attach to which Pokémon?")
            if target is not None:
                await ctx.attach_energy(picks[0], target)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="af80e064-f379-5ef7-99ef-3ed4383dd858",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vivillon.Name",
    display_name="Vivillon",
    searchable_by=["Vivillon", "Stage 2", "Vivillon"],
    subtypes=["Stage 2"],
    collector_number=15,
    set_code="XY8",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Spewpa.Name",
    family_id=664,
    abilities=[
        Ability(
            title="Energy Color",
            game_text="Once during your turn (before your attack), you may flip a coin. If heads, search your deck for a basic Energy card and attach it to 1 of your Pok\u00e9mon. Shuffle your deck afterward.",
            activation=Activations.ONCE_PER_TURN,
            effect=_energy_color,
        ),
        Attack(
            title="Sleep Powder",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)
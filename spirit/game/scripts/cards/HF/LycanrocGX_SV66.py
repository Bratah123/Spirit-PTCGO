from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.data_utils import Triggers
from spirit.game.card_effects.attacks_common import damage_per, count_bench

async def dark_signal(ctx):
    """When you play this Pokémon from your hand to evolve 1 of your Pokémon
    during your turn, you may switch 1 of your opponent's Benched Pokémon
    with their Active Pokémon."""
    bench = ctx.opponent_bench()
    active = ctx.opponent_active()
    if not bench or active is None or ctx.effects_blocked(active):
        return
    if await ctx.ask_yes_no(
        "Switch 1 of your opponent's Benched Pokémon with their Active Pokémon?"
    ):
        target = await ctx.choose_pokemon(
            bench, "Choose the opponent's new Active Pokémon"
        ) or bench[0]
        await ctx.switch_active(ctx.opponent_id, target)

card = PokemonCardDef(
    guid="9fdb84c6-6d45-5362-8898-6ad65efa6a03",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LycanrocGX.Name",
    display_name="Lycanroc-GX",
    searchable_by=["Lycanroc-GX", "Stage 1", "GX", "LycanrocGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=135,
    set_code="HF",
    rarity=Rarities.RareUltra,
    hp=200,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rockruff.Name",
    family_id=744,
    abilities=[
        Ability(
            title="Bloodthirsty Eyes",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may switch 1 of your opponent's Benched Pok\u00e9mon with their Active Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            trigger=Triggers.ON_EVOLVE,
            effect=dark_signal,
        ),
        Attack(
            title="Claw Slash",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=110,
        ),
        Attack(
            title="Dangerous Rogue-GX",
            game_text="This attack does 50 damage for each of your opponent's Benched Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="x",
            effect=damage_per(count_bench('opponent'), 50),
        ),
    ],
)
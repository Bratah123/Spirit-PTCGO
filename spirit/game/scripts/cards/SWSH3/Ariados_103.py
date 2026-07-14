from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.session.effects import is_evolution_pokemon


async def spider_net(ctx):
    """On evolve: you may gust one of the opponent's Benched Evolution Pokemon."""
    candidates = [p for p in ctx.opponent_bench() if is_evolution_pokemon(p)]
    if not candidates:
        return
    if not await ctx.ask_yes_no(
            "Switch 1 of your opponent's Benched Evolution Pokémon with their Active Pokémon?"):
        return
    target = await ctx.choose_pokemon(
        candidates, "Choose the opponent's new Active Pokémon"
    )
    if target is not None:
        await ctx.switch_active(ctx.opponent_id, target)


card = PokemonCardDef(
    guid="41922bdd-3fa5-526a-aaa3-1c10938a5733",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ariados.Name",
    display_name="Ariados",
    searchable_by=["Ariados", "Stage 1", "Ariados"],
    subtypes=["Stage 1"],
    collector_number=103,
    set_code="SWSH3",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Spinarak.Name",
    family_id=167,
    abilities=[
        Ability(
            title="Spider Net",
            game_text="When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may switch 1 of your opponent's Benched Evolution Pokémon with their Active Pokémon.",
            trigger=Triggers.ON_EVOLVE,
            effect=spider_net,
        ),
        Attack(
            title="Poison Sting",
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.POISONED),
        ),
    ],
)

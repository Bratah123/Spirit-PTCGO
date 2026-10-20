from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import devolve_depth


async def _flip_discard_defender_energy(ctx):
    """Printed damage; flip a coin. If heads, discard an Energy attached to
    your opponent's Active Pokemon."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, ctx.ability.title)
    target = ctx.opponent_active()
    if results and results[0] and target is not None and not ctx.effects_blocked(target):
        await ctx.discard_energy_from(target, 1, minimum=1,
                                      prompt="Choose an Energy to discard")


async def _rewind(ctx):
    """Devolve each of your opponent's evolved Pokemon; the highest Stage card
    goes to your opponent's hand."""
    for p in list(ctx.opponent_pokemon_in_play()):
        if devolve_depth(p) > 0 and not ctx.effects_blocked(p):
            await ctx.devolve_pokemon(p, 1, destination="hand")


card = PokemonCardDef(
    guid="993e7a68-fc02-5294-a71c-4def82503786",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Claydol.Name",
    display_name="Claydol",
    searchable_by=["Claydol", "Stage 1", "Claydol"],
    subtypes=["Stage 1"],
    collector_number=33,
    set_code="XY7",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Baltoy.Name",
    family_id=343,
    abilities=[
        Attack(
            title="Rewind",
            game_text="Devolve each of your opponent's evolved Pok\u00e9mon and put the highest Stage Evolution card on it into your opponent's hand.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=_rewind,
        ),
        Attack(
            title="Hyper Beam",
            game_text="Flip a coin. If heads, discard an Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=_flip_discard_defender_energy,
        ),
    ],
)
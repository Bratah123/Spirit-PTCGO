from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def shocking_smash(ctx):
    """Flip a coin. If heads, discard an Energy from 1 of the opponent's Pokémon."""
    results = await ctx.flip_coins(1, "Shocking Smash")
    if not results or not results[0]:
        return
    candidates = [p for p in ctx.opponent_pokemon_in_play()
                  if not ctx.effects_blocked(p) and ctx.attached_energies(p)]
    if not candidates:
        return
    target = await ctx.choose_pokemon(
        candidates, "Choose 1 of your opponent's Pokémon to discard an Energy from")
    if target is not None:
        await ctx.discard_energy_from(target, 1)

card = PokemonCardDef(
    guid="aebb42ba-5d2b-5752-aebd-791d8d2a0308",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eelektrik.Name",
    display_name="Eelektrik",
    searchable_by=["Eelektrik", "Stage 1", "Eelektrik"],
    subtypes=["Stage 1"],
    collector_number=58,
    set_code="SWSH4",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tynamo.Name",
    family_id=602,
    abilities=[
        Attack(
            title="Shocking Smash",
            game_text="Flip a coin. If heads, discard an Energy from 1 of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=shocking_smash,
        ),
        Attack(
            title="Head Bolt",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)
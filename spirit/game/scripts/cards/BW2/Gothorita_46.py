from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def deleting_glare(ctx):
    """Flip a coin. If heads, discard an Energy from 1 of opponent's Pokémon."""
    results = await ctx.flip_coins(1, ctx.ability.title)
    if not results or not results[0]:
        return
    candidates = [
        p for p in ctx.opponent_pokemon_in_play() if ctx.attached_energies(p)
    ]
    if not candidates:
        return
    target = await ctx.choose_pokemon(
        candidates, "Choose 1 of your opponent's Pokémon",
    )
    if target is None or ctx.effects_blocked(target):
        return
    await ctx.discard_energy_from(
        target, 1,
        prompt="Choose Energy to discard",
    )


card = PokemonCardDef(
    guid="88dd4bc9-c658-5515-beac-fb09469f024b",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gothorita.Name",
    display_name="Gothorita",
    searchable_by=["Gothorita", "Stage 1", "Gothorita"],
    subtypes=["Stage 1"],
    collector_number=46,
    set_code="BW2",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gothita.Name",
    family_id=574,
    abilities=[
        Attack(
            title="Deleting Glare",
            game_text="Flip a coin. If heads, discard an Energy attached to 1 of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=deleting_glare,
        ),
        Attack(
            title="Super Psy Bolt",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)

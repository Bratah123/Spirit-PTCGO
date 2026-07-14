from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import lost_mine_condition


async def lost_impact(ctx):
    """280. Put 2 Energy attached to your Pokemon in the Lost Zone."""
    await ctx.deal_damage()
    energies = []
    for pokemon in ctx.my_pokemon_in_play():
        energies.extend(ctx.attached_energies(pokemon))
    if not energies:
        return
    picks = await ctx.choose_cards(
        energies, 2,
        prompt="Choose 2 Energy to put in the Lost Zone",
    )
    if picks:
        await ctx.move_to_lost_zone(picks)


async def star_requiem(ctx):
    """VSTAR Power: your opponent's Active Pokemon is Knocked Out."""
    target = ctx.defender
    if target is not None:
        await ctx.knock_out(target)


card = PokemonCardDef(
    guid="2448f7fd-1959-5e6d-af1c-714542a5835c",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GiratinaVSTAR.Name",
    display_name="Giratina VSTAR",
    searchable_by=["Giratina VSTAR", "VSTAR", "GiratinaVSTAR"],
    subtypes=["VSTAR"],
    collector_number=131,
    set_code="SWSH11",
    rarity=Rarities.RareHoloVSTAR,
    hp=280,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.VSTAR,
    retreat_cost=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GiratinaV.Name",
    family_id=487,
    abilities=[
        Attack(
            title="Lost Impact",
            game_text="Put 2 Energy attached to your Pokémon in the Lost Zone.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=280,
            effect=lost_impact,
        ),
        Attack(
            title="Star Requiem",
            game_text="You can use this attack only if you have 10 or more cards in the Lost Zone. Your opponent's Active Pokémon is Knocked Out. (You can't use more than 1 VSTAR Power in a game.)",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.PSYCHIC: 1},
            vstar=True,
            condition=lost_mine_condition,
            effect=star_requiem,
        ),
    ],
)

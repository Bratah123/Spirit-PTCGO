from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.trainers import is_basic_energy_card


async def _rainbow_shower(ctx):
    """Attach any number of basic Energy cards from your hand to your Pokemon."""
    for _ in range(60):
        cards = [c for c in ctx.hand() if is_basic_energy_card(c)]
        if not cards:
            return
        picks = await ctx.choose_cards(cards, 1, minimum=0,
                                       prompt="Choose a basic Energy to attach (or none to stop)")
        if not picks:
            return
        mine = ctx.my_pokemon_in_play()
        target = mine[0] if len(mine) == 1 else await ctx.choose_pokemon(
            mine, "Attach it to which Pokémon?")
        if target is None:
            return
        await ctx.attach_energy(picks[0], target)


async def _sand_sweep(ctx):
    """70; heal 30 from each of your Pokemon with any Energy attached."""
    await ctx.deal_damage()
    for p in ctx.my_pokemon_in_play():
        if ctx.attached_energies(p):
            await ctx.heal(30, p)


card = PokemonCardDef(
    guid="9999aee0-8e7d-5f09-912f-5eee510f8325",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flygon.Name",
    display_name="Flygon",
    searchable_by=["Flygon", "Stage 2", "Flygon"],
    subtypes=["Stage 2"],
    collector_number=76,
    set_code="XY3",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vibrava.Name",
    family_id=328,
    abilities=[
        Attack(
            title="Rainbow Shower",
            game_text="Attach as many basic Energy cards as you like from your hand to your Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_rainbow_shower,
        ),
        Attack(
            title="Sand Sweep",
            game_text="Heal 30 damage from each of your Pok\u00e9mon that has any Energy attached to it.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=_sand_sweep,
        ),
    ],
)
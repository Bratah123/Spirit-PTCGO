from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.card_effects.support_common import distribute_energy


async def turbo_storm(ctx):
    """30 damage; attach 2 basic Energy from discard to 1 Benched Pokémon."""
    await ctx.deal_damage()
    bench = ctx.my_bench()
    if not bench:
        return
    pool = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
    if not pool:
        return
    picks = await ctx.choose_cards(
        pool, 2, minimum=0,
        prompt="Choose up to 2 basic Energy cards to attach",
    )
    if not picks:
        return
    target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon to attach the Energy to")
    if target is None:
        return
    for energy in picks:
        await ctx.attach_energy(energy, target)


card = PokemonCardDef(
    guid="21a380f8-2e94-5d73-ba05-0437b7d1e237",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rayquaza.Name",
    display_name="Rayquaza",
    searchable_by=["Rayquaza", "Basic", "Rayquaza"],
    subtypes=["Basic"],
    collector_number=106,
    set_code="SM2",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=384,
    abilities=[
        Attack(
            title="Turbo Storm",
            game_text="Attach 2 basic Energy cards from your discard pile to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=turbo_storm,
        ),
        Attack(
            title="Dragon Claw",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
        ),
    ],
)
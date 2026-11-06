from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import spread_damage
from spirit.game.card_effects.trainers import is_basic_energy_card


async def _enefountain(ctx):
    """Printed damage; attach 2 basic Energy cards from your hand to 1 of your Pokemon."""
    await ctx.deal_damage()
    pool = [c for c in ctx.hand() if is_basic_energy_card(c)]
    n = min(2, len(pool))
    if n <= 0:
        return
    picks = await ctx.choose_cards(pool, n, minimum=n, prompt="Choose 2 basic Energy cards to attach")
    target = await ctx.choose_pokemon(ctx.my_pokemon_in_play(), "Choose a Pokémon to attach them to")
    for card in picks:
        await ctx.attach_energy(card, target or ctx.attacker)


card = PokemonCardDef(
    guid="030a25e9-94ae-54a0-b791-d8233e2289be",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vanilluxe.Name",
    display_name="Vanilluxe",
    searchable_by=["Vanilluxe", "Stage 2", "Vanilluxe"],
    subtypes=["Stage 2"],
    collector_number=37,
    set_code="BW8",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vanillish.Name",
    family_id=582,
    abilities=[
        Attack(
            title="Enefountain",
            game_text="Attach 2 basic Energy cards from your hand to 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=_enefountain,
        ),
        Attack(
            title="Blizzard",
            game_text="Does 10 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=spread_damage(10, also_base=True),
        ),
    ],
)
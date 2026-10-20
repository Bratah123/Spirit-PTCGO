from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.card_effects.trainers import is_basic_energy_card


async def _double_assist(ctx):
    """Printed damage; attach 2 basic Energy cards from your discard pile to 1 of your Pokemon."""
    await ctx.deal_damage()
    pool = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
    n = min(2, len(pool))
    if n <= 0:
        return
    picks = await ctx.choose_cards(pool, n, minimum=n, prompt="Choose 2 basic Energy cards to attach")
    target = await ctx.choose_pokemon(ctx.my_pokemon_in_play(), "Choose a Pokémon to attach them to")
    for card in picks:
        await ctx.attach_energy(card, target or ctx.attacker)


card = PokemonCardDef(
    guid="1107b031-fb45-54e6-9c6b-634b6140879e",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magnezone.Name",
    display_name="Magnezone",
    searchable_by=["Magnezone", "Stage 2", "Magnezone"],
    subtypes=["Stage 2"],
    collector_number=47,
    set_code="BW8",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magneton.Name",
    family_id=81,
    abilities=[
        Attack(
            title="Double Assist",
            game_text="Attach 2 basic Energy cards from your discard pile to 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
            effect=_double_assist,
        ),
        Attack(
            title="Tumbling Attack",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            damage_operator="+",
            effect=flip_bonus(20),
        ),
    ],
)
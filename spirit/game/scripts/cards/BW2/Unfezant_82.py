from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.trainers import is_energy_card


async def tailwind(ctx):
    """Attach an Energy from your hand to 1 of your Pokémon."""
    energies = [c for c in ctx.hand() if is_energy_card(c)]
    if not energies:
        return
    picks = await ctx.choose_cards(
        energies, 1, minimum=0,
        prompt="Choose an Energy card from your hand to attach",
    )
    if not picks:
        return
    target = await ctx.choose_pokemon(
        ctx.my_pokemon_in_play(),
        "Choose a Pokémon to attach the Energy to",
    )
    if target is not None:
        await ctx.attach_energy(picks[0], target)


async def feather_strike(ctx):
    """Flip: heads +40; tails discard Energy from defender. Printed 40 either way."""
    heads = (await ctx.flip_coins(1, ctx.ability.title))[0]
    await ctx.deal_damage(40 + (40 if heads else 0))
    if not heads:
        defender = ctx.defender
        if defender is None or ctx.effects_blocked(defender):
            return
        await ctx.discard_energy_from(
            defender, 1,
            prompt="Choose Energy to discard from the Defending Pokémon",
        )


card = PokemonCardDef(
    guid="c7ca7565-d40e-50d6-bd3e-0510dbfeb0a4",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Unfezant.Name",
    display_name="Unfezant",
    searchable_by=["Unfezant", "Stage 2", "Unfezant"],
    subtypes=["Stage 2"],
    collector_number=82,
    set_code="BW2",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tranquill.Name",
    family_id=519,
    abilities=[
        Attack(
            title="Tailwind",
            game_text="Attach an Energy from your hand to 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=tailwind,
        ),
        Attack(
            title="Feather Strike",
            game_text="Flip a coin. If heads, this attack does 40 more damage. If tails, discard an Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            damage_operator="+",
            effect=feather_strike,
        ),
    ],
)

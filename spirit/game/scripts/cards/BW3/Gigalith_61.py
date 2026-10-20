from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import count_energy


async def core_cannon(ctx):
    """20 damage to 1 of opponent's Pokemon per Fighting Energy on self."""
    amount = 20 * count_energy("self", energy_type=PokemonTypes.FIGHTING)(ctx)
    if amount <= 0:
        return
    candidates = ctx.opponent_pokemon_in_play()
    if not candidates:
        return
    target = await ctx.choose_pokemon(
        candidates, "Choose 1 of your opponent's Pokémon")
    if target is not None:
        await ctx.deal_damage(amount, target=target)


card = PokemonCardDef(
    guid="4ff358ff-cb75-59f3-996d-026b00e7be33",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gigalith.Name",
    display_name="Gigalith",
    searchable_by=["Gigalith", "Stage 2", "Gigalith"],
    subtypes=["Stage 2"],
    collector_number=61,
    set_code="BW3",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Boldore.Name",
    family_id=526,
    abilities=[
        Attack(
            title="Core Cannon",
            game_text="This attack does 20 damage to 1 of your opponent's Pok\u00e9mon for each Fighting Energy attached to this Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 1},
            effect=core_cannon,
        ),
        Attack(
            title="Power Gem",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=90,
        ),
    ],
)

from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.pokemon import energy_provides_type


async def _jet_woofer(ctx):
    """For each Psychic Energy attached to this Pokemon, discard the top card
    of your opponent's deck."""
    n = sum(1 for e in ctx.attached_energies(ctx.attacker)
            if energy_provides_type(e, PokemonTypes.PSYCHIC.value))
    if n:
        await ctx.discard_cards(ctx.deck_top(n, player_id=ctx.opponent_id))


card = PokemonCardDef(
    guid="08b45b0a-f763-570f-b3cf-dbea70b6abe3",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swoobat.Name",
    display_name="Swoobat",
    searchable_by=["Swoobat", "Stage 1", "Swoobat"],
    subtypes=["Stage 1"],
    collector_number=71,
    set_code="BW7",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Woobat.Name",
    family_id=527,
    abilities=[
        Attack(
            title="Jet Woofer",
            game_text="For each Psychic Energy attached to this Pok\u00e9mon, discard the top card of your opponent's deck.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=_jet_woofer,
        ),
        Attack(
            title="Acrobatics",
            game_text="Flip 2 coins. This attack does 20 more damage for each heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=flip_damage(coins=2, bonus_per_heads=20),
        ),
    ],
)
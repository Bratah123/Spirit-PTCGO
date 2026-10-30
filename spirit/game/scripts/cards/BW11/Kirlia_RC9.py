from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage, count_energy


_psychic_energy = count_energy("self", energy_type=PokemonTypes.PSYCHIC)


async def _tiptoe_step(ctx):
    """Draw a card for each Psychic Energy attached to this Pokemon."""
    n = _psychic_energy(ctx)
    if n:
        await ctx.draw_cards(n)


card = PokemonCardDef(
    guid="463ccdb8-0dc8-5795-b62a-69f7cc343cc2",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kirlia.Name",
    display_name="Kirlia",
    searchable_by=["Kirlia", "Stage 1", "Kirlia"],
    subtypes=["Stage 1"],
    collector_number=124,
    set_code="BW11",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ralts.Name",
    family_id=280,
    abilities=[
        Attack(
            title="Tiptoe Step",
            game_text="Draw a card for each Psychic Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=_tiptoe_step,
        ),
        Attack(
            title="Double Slap",
            game_text="Flip 2 coins. This attack does 20 damage times the number of heads.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=flip_damage(2, per_heads=20),
        ),
    ],
)
from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


async def _draw_in(ctx):
    """Attach 2 Darkness Energy cards from your discard pile to this Pokemon."""
    pool = [c for c in ctx.discard_pile()
            if is_energy_card(c) and energy_provides_type(c, PokemonTypes.DARKNESS.value)]
    if not pool:
        return
    picks = await ctx.choose_cards(pool, min(2, len(pool)), minimum=min(2, len(pool)),
                                   prompt="Choose 2 Darkness Energy cards to attach")
    for card in picks:
        await ctx.attach_energy(card, ctx.attacker)


card = PokemonCardDef(
    guid="1198ec4f-cfc0-5918-967c-3f21c4c9166a",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zweilous.Name",
    display_name="Zweilous",
    searchable_by=["Zweilous", "Stage 1", "Zweilous"],
    subtypes=["Stage 1"],
    collector_number=96,
    set_code="BW6",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.DRAGON,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Deino.Name",
    family_id=633,
    abilities=[
        Attack(
            title="Draw In",
            game_text="Attach 2 Darkness Energy cards from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_draw_in,
        ),
        Attack(
            title="Dragon Headbutt",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)
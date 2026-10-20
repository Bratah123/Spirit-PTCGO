from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_fighting_energy_card(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.FIGHTING.value)


async def _rock_rush(ctx):
    """Discard any number of Fighting Energy cards from your hand: 30 damage
    times the number discarded."""
    n = sum(1 for c in ctx.hand() if _is_fighting_energy_card(c))
    picked = await ctx.discard_from_hand(n, minimum=0, predicate=_is_fighting_energy_card,
                                         prompt="Discard any number of Fighting Energy cards") if n else []
    await ctx.deal_damage(30 * len(picked or []))


card = PokemonCardDef(
    guid="374729a7-d56c-580f-9f5d-38daf420f121",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Barbaracle.Name",
    display_name="Barbaracle",
    searchable_by=["Barbaracle", "Stage 1", "Barbaracle"],
    subtypes=["Stage 1"],
    collector_number=49,
    set_code="XY2",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Binacle.Name",
    family_id=688,
    abilities=[
        Attack(
            title="Rock Rush",
            game_text="Discard as many Fighting Energy cards as you like from your hand. This attack does 30 damage times the number of Energy cards you discarded.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=30,
            damage_operator="x",
            effect=_rock_rush,
        ),
        Attack(
            title="Boulder Crush",
            cost={PokemonTypes.FIGHTING: 3},
            damage=80,
        ),
    ],
)
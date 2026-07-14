from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_fighting_energy_card(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.FIGHTING.value)


async def roaring_resolve(ctx):
    """Once per turn: you may put 2 damage counters on this Pokémon. If you
    do, search your deck for a Fighting Energy card and attach it here."""
    if not await ctx.ask_yes_no("Put 2 damage counters on this Pokémon?"):
        return
    await ctx.deal_damage(20, target=ctx.source, apply_modifiers=False, as_counters=True)
    picks = await ctx.search_deck(
        _is_fighting_energy_card, count=1, minimum=0,
        prompt="Choose a Fighting Energy card to attach.",
    )
    if picks:
        await ctx.attach_energy(picks[0], ctx.source)
    await ctx.shuffle_deck()


async def aura_sphere_volley(ctx):
    """Discard all Fighting Energy from this Pokémon. This attack does 60
    more damage for each card discarded this way."""
    discarded = await ctx.discard_energy_from(
        ctx.source, 99, predicate=_is_fighting_energy_card,
        prompt="Discard all Fighting Energy from this Pokémon",
    )
    await ctx.deal_damage(10 + 60 * len(discarded))

card = PokemonCardDef(
    guid="2bd1d15a-29ba-5870-9b34-3ed6be0f3294",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lucario.Name",
    display_name="Lucario",
    searchable_by=["Lucario", "Stage 1", "Lucario"],
    subtypes=["Stage 1"],
    collector_number=79,
    set_code="SWSH9",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Riolu.Name",
    family_id=447,
    abilities=[
        Ability(
            title="Roaring Resolve",
            game_text="Once during your turn, you may put 2 damage counters on this Pok\u00e9mon. If you do, search your deck for a Fighting Energy card and attach it to this Pok\u00e9mon. Then, shuffle your deck.",
            activation=Activations.ONCE_PER_TURN,
            effect=roaring_resolve,
        ),
        Attack(
            title="Aura Sphere Volley",
            game_text="Discard all Fighting Energy from this Pok\u00e9mon. This attack does 60 more damage for each card you discarded in this way.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=10,
            damage_operator="+",
            effect=aura_sphere_volley,
        ),
    ],
)
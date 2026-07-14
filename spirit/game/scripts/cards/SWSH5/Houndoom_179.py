from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations, subtypes_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import is_energy_card


def _is_single_strike_energy(card):
    return is_energy_card(card) and "Single Strike" in subtypes_for(card.archetype_id)


def _is_single_strike_pokemon(pokemon):
    return "Single Strike" in subtypes_for(pokemon.archetype_id)


async def single_strike_roar(ctx):
    """Once per turn: you may search for a Single Strike Energy card and
    attach it to 1 of your Single Strike Pokémon; if you did, put 2 damage
    counters on that Pokémon."""
    if not await ctx.ask_yes_no(
        "Search your deck for a Single Strike Energy card and attach it to "
        "1 of your Single Strike Pokémon?"
    ):
        return
    picks = await ctx.search_deck(
        _is_single_strike_energy, count=1, minimum=0,
        prompt="Choose a Single Strike Energy card to attach.",
    )
    await ctx.shuffle_deck()
    if not picks:
        return
    candidates = [p for p in ctx.my_pokemon_in_play() if _is_single_strike_pokemon(p)]
    if not candidates:
        return
    target = await ctx.choose_pokemon(
        candidates, "Choose a Single Strike Pokémon to attach the Energy to"
    )
    if target is None:
        return
    await ctx.attach_energy(picks[0], target)
    await ctx.deal_damage(20, target=target, apply_modifiers=False, as_counters=True)


card = PokemonCardDef(
    guid="81c2ef9b-3afd-53ec-b712-ad81e64d944c",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Houndoom.Name",
    display_name="Houndoom",
    searchable_by=["Houndoom", "Stage 1", "Single Strike", "Houndoom"],
    subtypes=["Stage 1", "Single Strike"],
    collector_number=179,
    set_code="SWSH5",
    rarity=Rarities.RareSecret,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Houndour.Name",
    family_id=228,
    abilities=[
        Ability(
            title="Single Strike Roar",
            game_text="Once during your turn, you may search your deck for a Single Strike Energy card and attach it to 1 of your Single Strike Pok\u00e9mon. Then, shuffle your deck. If you attached Energy to a Pok\u00e9mon in this way, put 2 damage counters on that Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            effect=single_strike_roar,
        ),
        Attack(
            title="Darkness Fang",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)
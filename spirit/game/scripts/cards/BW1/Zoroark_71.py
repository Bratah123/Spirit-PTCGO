from spirit.game.data_utils import PokemonCardDef, Attack, def_for
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities


async def nasty_plot(ctx):
    """Search deck for a card and put it into your hand."""
    picks = await ctx.search_deck(
        count=1, minimum=1,
        prompt="Choose a card to put into your hand.",
    )
    await ctx.put_in_hand(picks, reveal=False)
    await ctx.shuffle_deck()


async def foul_play(ctx):
    """Choose 1 of the Defending Pokémon's attacks and use it."""
    defender = ctx.opponent_active()
    if defender is None:
        return
    definition = def_for(defender.archetype_id)
    candidates = [
        (defender, ability) for ability in getattr(definition, "abilities", [])
        if isinstance(ability, Attack)
    ]
    if not candidates:
        return
    picked = await ctx.choose_attack_to_copy(candidates, "Choose an attack to copy")
    if picked is None:
        return
    _, chosen = picked
    if not await ctx.use_attack(chosen):
        return
    if getattr(chosen, "locks_next_turn", False):
        for entry in ctx.attacker.get_attribute(AttrID.PIE_ABILITIES) or []:
            if isinstance(entry, dict) and entry.get("abilityType") == "Attack":
                ctx.session.turn_state.lock_attack(
                    ctx.attacker.entity_id, entry["abilityID"]
                )


def _foul_play_condition(board, player_id, pokemon=None) -> bool:
    opponent = next((p for p in board.player_ids if p != player_id), None)
    if opponent is None:
        return False
    target = board.active_pokemon(opponent)
    if target is None:
        return False
    definition = def_for(target.archetype_id)
    return any(
        isinstance(ability, Attack)
        for ability in getattr(definition, "abilities", [])
    )


card = PokemonCardDef(
    guid="0fd5f3f6-5246-5165-afec-b3bccb0ae4c7",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zoroark.Name",
    display_name="Zoroark",
    searchable_by=["Zoroark", "Stage 1", "Zoroark"],
    subtypes=["Stage 1"],
    collector_number=71,
    set_code="BW1",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Zorua.Name",
    family_id=570,
    abilities=[
        Attack(
            title="Nasty Plot",
            game_text="Search your deck for a card and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=nasty_plot,
        ),
        Attack(
            title="Foul Play",
            game_text="Choose 1 of the Defending Pok\u00e9mon's attacks and use it as this attack.",
            cost={PokemonTypes.COLORLESS: 2},
            condition=_foul_play_condition,
            effect=foul_play,
        ),
    ],
)

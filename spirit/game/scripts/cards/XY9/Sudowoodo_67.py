from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.content.definitions import def_for


async def _watch_and_learn(ctx):
    """If the opponent's Pokemon used an attack during their last turn, use it as this attack."""
    for entity_id, archetype_id, title in reversed(ctx.session.turn_state.attacks_used_last_turn):
        entity = ctx.board.get_entity(entity_id)
        owner = getattr(entity, "owning_player_id", None)
        if owner is not None and owner != ctx.opponent_id:
            continue
        chosen = next((a for a in getattr(def_for(archetype_id), "abilities", None) or []
                       if isinstance(a, Attack) and a.title == title), None)
        if chosen is not None:
            await ctx.use_attack(chosen)
            return


card = PokemonCardDef(
    guid="37ca15b6-e223-56c7-8d1b-b456d276642b",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sudowoodo.Name",
    display_name="Sudowoodo",
    searchable_by=["Sudowoodo", "Basic", "Sudowoodo"],
    subtypes=["Basic"],
    collector_number=67,
    set_code="XY9",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=185,
    abilities=[
        Attack(
            title="Watch and Learn",
            game_text="If your opponent's Pok\u00e9mon used an attack during his or her last turn, use it as this attack.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            effect=_watch_and_learn,
        ),
    ],
)
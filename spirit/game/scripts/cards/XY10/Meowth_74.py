from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.session.passives import effective_max_hp


async def _turmoil_strike(ctx):
    """50 to 1 of your opponent's Pokemon that has any damage counters."""
    pool = [p for p in ctx.opponent_pokemon_in_play()
            if effective_max_hp(ctx.board, p) > p.get_attribute(AttrID.HP, 0)]
    if pool:
        target = pool[0] if len(pool) == 1 else await ctx.choose_pokemon(pool, "Choose a damaged Pokémon")
        if target is not None:
            await ctx.deal_damage(50, target=target)


card = PokemonCardDef(
    guid="0baa24b3-38a8-581f-b7d8-293845d2b373",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meowth.Name",
    display_name="Meowth",
    searchable_by=["Meowth", "Basic", "Meowth"],
    subtypes=["Basic"],
    collector_number=74,
    set_code="XY10",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=52,
    abilities=[
        Attack(
            title="Turmoil Strike",
            game_text="This attack does 50 damage to 1 of your opponent's Pok\u00e9mon that has any damage counters on it. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 2},
            effect=_turmoil_strike,
        ),
    ],
)
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import condition_attack


async def perish_body(ctx):
    """If in the Active Spot and Knocked Out by damage from an opponent's
    attack, flip a coin. If heads, the Attacking Pokemon is Knocked Out."""
    if not ctx.ko_from_attack:
        return
    active_area = ctx.board.find_player_area(ctx.player_id, "activePokemonArea")
    if active_area is not None and active_area.children:
        return  # was Benched, not Active, when Knocked Out
    results = await ctx.flip_coins(1, "Perish Body")
    if results and results[0]:
        await ctx.knock_out(ctx.ko_attacker)


card = PokemonCardDef(
    guid="7c46f16c-86b7-5ad4-8c5a-b9525c7c87c4",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianCursola.Name",
    display_name="Galarian Cursola",
    searchable_by=["Galarian Cursola", "Stage 1", "GalarianCursola"],
    subtypes=["Stage 1"],
    collector_number=79,
    set_code="SWSH2",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianCorsola.Name",
    family_id=222,
    abilities=[
        Ability(
            title="Perish Body",
            game_text="If this Pokémon is in the Active Spot and is Knocked Out by damage from an opponent's attack, flip a coin. If heads, the Attacking Pokémon is Knocked Out.",
            trigger=Triggers.ON_KNOCKED_OUT,
            effect=perish_body,
        ),
        Attack(
            title="Corner",
            game_text="During your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=condition_attack(no_retreat=True),
        ),
    ],
)

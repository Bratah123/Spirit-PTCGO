from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.attacks_common import damage_per


async def field_crush(ctx):
    """20 damage; if the opponent has a Stadium in play, discard it."""
    await ctx.deal_damage()
    stadium = ctx.stadium_in_play()
    if stadium is not None and stadium.owning_player_id == ctx.opponent_id:
        await ctx.discard_stadium()


def _damaged_bench_count(ctx):
    return sum(
        1 for p in ctx.my_bench() if p.get_attribute(AttrID.HP, 0) < ctx.max_hp(p)
    )


card = PokemonCardDef(
    guid="988bcc33-8ed5-53b4-b0c4-678e5a4a2490",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Primeape.Name",
    display_name="Primeape",
    searchable_by=["Primeape", "Stage 1", "Single Strike", "Primeape"],
    subtypes=["Stage 1", "Single Strike"],
    collector_number=67,
    set_code="SWSH5",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Mankey.Name",
    family_id=56,
    abilities=[
        Attack(
            title="Field Crush",
            game_text="If your opponent has a Stadium in play, discard it.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=field_crush,
        ),
        Attack(
            title="Steamin' Mad Strike",
            game_text="This attack does 50 damage for each of your Benched Pok\u00e9mon that has any damage counters on it.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=50,
            damage_operator="x",
            effect=damage_per(_damaged_bench_count, 50),
        ),
    ],
)
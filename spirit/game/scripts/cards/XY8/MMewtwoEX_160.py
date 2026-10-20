from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import count_energy


_mine = count_energy('self')
_theirs = count_energy('defender')


async def _psychic_infinity(ctx):
    """10+; 30 more per Energy attached to both Active Pokemon; ignores Weakness."""
    await ctx.deal_damage(ctx.ability.damage + 30 * (_mine(ctx) + _theirs(ctx)), ignore_weakness=True)


card = PokemonCardDef(
    guid="f37e9b3c-677b-55db-903f-b02aef3885fe",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MMewtwoEX.Name",
    display_name="M Mewtwo-EX",
    searchable_by=["M Mewtwo-EX", "MEGA", "EX", "MMewtwoEX"],
    subtypes=["MEGA", "EX"],
    collector_number=160,
    set_code="XY8",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MewtwoEX.Name",
    family_id=150,
    abilities=[
        Attack(
            title="Psychic Infinity",
            game_text="This attack does 30 more damage times the amount of Energy attached to both Active Pok\u00e9mon. This attack's damage isn't affected by Weakness.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=_psychic_infinity,
        ),
    ],
)
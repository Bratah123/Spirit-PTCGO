from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import boost_own_next_turn


async def _curly_ribbon(ctx):
    """30; move an Energy from the opponent's Active to 1 of their Benched."""
    await ctx.deal_damage()
    target = ctx.defender
    bench = ctx.opponent_bench()
    if target is None or not bench or ctx.effects_blocked(target):
        return
    if not ctx.attached_energies(target):
        return
    await ctx.move_energy_freely([target], bench, max_count=1,
                                 prompt="Choose an Energy to move")


card = PokemonCardDef(
    guid="6ac1bd1c-5bf6-518b-87d7-1fd9dc547a03",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sylveon.Name",
    display_name="Sylveon",
    searchable_by=["Sylveon", "Stage 1", "Sylveon"],
    subtypes=["Stage 1"],
    collector_number=72,
    set_code="XY3",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Curly Ribbon",
            game_text="Move an Energy attached to your opponent's Active Pok\u00e9mon to 1 of his or her Benched Pok\u00e9mon.",
            cost={PokemonTypes.FAIRY: 1},
            damage=30,
            effect=_curly_ribbon,
        ),
        Attack(
            title="Echoed Voice",
            game_text="During your next turn, this Pok\u00e9mon's Echoed Voice attack does 50 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=boost_own_next_turn(50, attack_title='Echoed Voice'),
        ),
    ],
)
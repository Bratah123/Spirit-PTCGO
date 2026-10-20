from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import protect_next_turn


async def _rushing_water(ctx):
    """40; move an Energy from the opponent's Active to 1 of their Benched Pokemon."""
    await ctx.deal_damage()
    d = ctx.opponent_active()
    bench = ctx.opponent_bench()
    if d is None or not bench or not ctx.attached_energies(d) or ctx.effects_blocked(d):
        return
    await ctx.move_energy_freely([d], bench, max_count=1, prompt="Move an Energy to which Benched Pokémon?")


card = PokemonCardDef(
    guid="a5d26d39-3366-546f-964e-d4d839297b2f",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Armaldo.Name",
    display_name="Armaldo",
    searchable_by=["Armaldo", "Stage 1", "Armaldo"],
    subtypes=["Stage 1"],
    collector_number=57,
    set_code="XY11",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Anorith.Name",
    family_id=347,
    abilities=[
        Attack(
            title="Rushing Water",
            game_text="Move an Energy from your opponent's Active Pok\u00e9mon to 1 of his or her Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=_rushing_water,
        ),
        Attack(
            title="Guard Claw",
            game_text="During your opponent's next turn, any damage done to this Pok\u00e9mon by attacks is reduced by 30 (after applying Weakness and Resistance).",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=protect_next_turn(reduce=30),
        ),
    ],
)
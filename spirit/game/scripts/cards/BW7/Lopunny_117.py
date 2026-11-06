from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import gust_attack


async def _healing_melody(ctx):
    """Flip a coin. If heads, heal 60 damage from each of your Pokemon."""
    results = await ctx.flip_coins(1, "Healing Melody")
    if results and results[0]:
        for pokemon in ctx.my_pokemon_in_play():
            await ctx.heal(60, pokemon)


card = PokemonCardDef(
    guid="3ea161c5-e9f7-51e7-98cc-913e4c85acff",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lopunny.Name",
    display_name="Lopunny",
    searchable_by=["Lopunny", "Stage 1", "Lopunny"],
    subtypes=["Stage 1"],
    collector_number=117,
    set_code="BW7",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Buneary.Name",
    family_id=427,
    abilities=[
        Attack(
            title="Healing Melody",
            game_text="Flip a coin. If heads, heal 60 damage from each of your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_healing_melody,
        ),
        Attack(
            title="Kick Away",
            game_text="Your opponent switches the Defending Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            effect=gust_attack(opponent_chooses=True),
        ),
    ],
)
from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def feint(ctx):
    """30. This attack's damage isn't affected by Resistance."""
    await ctx.deal_damage(ignore_resistance=True)


card = PokemonCardDef(
    guid="5f3cfa72-2b29-5d75-8721-bcf26f454db2",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TerrakionEX.Name",
    display_name="Terrakion-EX",
    searchable_by=["Terrakion-EX", "Basic", "EX", "TerrakionEX"],
    subtypes=["Basic", "EX"],
    collector_number=121,
    set_code="BW6",
    rarity=Rarities.RareUltra,
    hp=180,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=639,
    abilities=[
        Attack(
            title="Rock Tumble",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=feint,
        ),
        Attack(
            title="Pump-up Smash",
            game_text="Attach 2 basic Energy cards from your hand to your Benched Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=unimplemented,
        ),
    ],
)
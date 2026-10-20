from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def feint(ctx):
    """30. This attack's damage isn't affected by Resistance."""
    await ctx.deal_damage(ignore_resistance=True)


card = PokemonCardDef(
    guid="cd38d6f4-8fa3-5a84-8138-1822a01b7b42",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hawlucha.Name",
    display_name="Hawlucha",
    searchable_by=["Hawlucha", "Basic", "Hawlucha"],
    subtypes=["Basic"],
    collector_number=87,
    set_code="XY8",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=701,
    abilities=[
        Attack(
            title="High Jump Kick",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
        ),
        Attack(
            title="Skyward Kick",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=40,
            effect=feint,
        ),
    ],
)
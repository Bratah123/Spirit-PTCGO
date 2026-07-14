from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def battle_legion(ctx):
    """20+10 per Benched Pokemon; ignores Weakness and effects on the Active."""
    amount = 20 + 10 * len(ctx.my_bench())
    await ctx.deal_damage(amount, ignore_weakness=True, ignore_target_effects=True)


card = PokemonCardDef(
    guid="5fb73471-acf0-589f-85db-f5100a774a14",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zacian.Name",
    display_name="Zacian",
    searchable_by=["Zacian", "Basic", "Zacian"],
    subtypes=["Basic"],
    collector_number=94,
    set_code="CZ",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=888,
    abilities=[
        Attack(
            title="Battle Legion",
            game_text="This attack does 10 more damage for each of your Benched Pok\u00e9mon. This attack's damage isn't affected by Weakness or by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 1},
            damage=20,
            damage_operator="+",
            effect=battle_legion,
        ),
        Attack(
            title="Slicing Blade",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)
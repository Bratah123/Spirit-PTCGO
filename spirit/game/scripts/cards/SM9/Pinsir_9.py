from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import condition_attack

async def _timber_cleave(ctx):
    """Flip 2 coins. If both are heads, the opponent's Active is Knocked Out."""
    coins = await ctx.flip_coins(2, "Timber Cleave")
    if all(coins):
        await ctx.knock_out(ctx.defender)

card = PokemonCardDef(
    guid="76e06626-2eb6-56dd-980d-2ad0ad400e26",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pinsir.Name",
    display_name="Pinsir",
    searchable_by=["Pinsir", "Basic", "Pinsir"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="SM9",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    family_id=127,
    abilities=[
        Attack(
            title="Grip and Squeeze",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=condition_attack(no_retreat=True),
        ),
        Attack(
            title="Guillotine Hug",
            game_text="Flip 2 coins. If both of them are heads, your opponent's Active Pok\u00e9mon is Knocked Out.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            effect=_timber_cleave,
        ),
    ],
)
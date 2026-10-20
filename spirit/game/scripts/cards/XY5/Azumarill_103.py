from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack, recoil_attack


async def _superpower(ctx):
    """60; you may do 30 more damage. If you do, 30 damage to itself."""
    if await ctx.ask_yes_no("Do 30 more damage (this Pokémon does 30 damage to itself)?"):
        await recoil_attack(30, damage=90)(ctx)
    else:
        await ctx.deal_damage()


card = PokemonCardDef(
    guid="b5fc9805-782e-5182-9164-f6c2a6dd8f1d",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Azumarill.Name",
    display_name="Azumarill",
    searchable_by=["Azumarill", "Stage 1", "Azumarill"],
    subtypes=["Stage 1"],
    collector_number=103,
    set_code="XY5",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Marill.Name",
    family_id=183,
    abilities=[
        Attack(
            title="Bubble Beam",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Superpower",
            game_text="You may do 30 more damage. If you do, this Pok\u00e9mon does 30 damage to itself.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=_superpower,
        ),
    ],
)
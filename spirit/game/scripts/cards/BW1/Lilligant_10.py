from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import (
    AttrID, PokemonTypes, PokemonStage, Rarities, SpecialConditions,
)
from spirit.game.card_effects.attacks_common import flip_damage


async def _petal_dance(ctx):
    await flip_damage(coins=3, per_heads=30)(ctx)
    await ctx.apply_special_condition(ctx.attacker, SpecialConditions.CONFUSED)


async def _leaf_storm(ctx):
    await ctx.deal_damage()
    for pokemon in ctx.my_pokemon_in_play():
        types = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
        if PokemonTypes.GRASS.value in types:
            await ctx.heal(20, pokemon)


card = PokemonCardDef(
    guid="765819c4-849a-5aa1-9b34-064a52008037",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lilligant.Name",
    display_name="Lilligant",
    searchable_by=["Lilligant", "Stage 1", "Lilligant"],
    subtypes=["Stage 1"],
    collector_number=10,
    set_code="BW1",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Petilil.Name",
    family_id=548,
    abilities=[
        Attack(
            title="Petal Dance",
            game_text="Flip 3 coins. This attack does 30 damage times the number of heads. This Pok\u00e9mon is now confused.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            damage_operator="x",
            effect=_petal_dance,
        ),
        Attack(
            title="Leaf Storm",
            game_text="Heal 20 damage from each of your Grass Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=_leaf_storm,
        ),
    ],
)

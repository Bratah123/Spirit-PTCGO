from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.trainers import is_dragon_pokemon


async def _ice_age(ctx):
    """80; if the opponent's Active is a Dragon Pokemon, it is now Paralyzed."""
    await ctx.deal_damage()
    d = ctx.opponent_active()
    if d is not None and is_dragon_pokemon(d):
        await ctx.apply_special_condition(d, SpecialConditions.PARALYZED)


card = PokemonCardDef(
    guid="e1d6367b-0987-52d0-afc6-d69dbffbaf8e",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Abomasnow.Name",
    display_name="Abomasnow",
    searchable_by=["Abomasnow", "Stage 1", "Abomasnow"],
    subtypes=["Stage 1"],
    collector_number=40,
    set_code="XY8",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Snover.Name",
    family_id=459,
    abilities=[
        Attack(
            title="Ice Age",
            game_text="If your opponent's Active Pok\u00e9mon is a Dragon Pok\u00e9mon, it is now Paralyzed.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=_ice_age,
        ),
        Attack(
            title="Frost Breath",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=110,
        ),
    ],
)
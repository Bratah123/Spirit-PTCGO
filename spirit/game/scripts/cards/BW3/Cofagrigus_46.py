from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


async def damagriiigus(ctx):
    """Move all damage counters from 1 of your Benched Pokémon to the Defending Pokémon."""
    damaged = [p for p in ctx.my_bench()
               if p.get_attribute(AttrID.HP, 0) < ctx.max_hp(p)]
    if not damaged or ctx.defender is None:
        return
    source = await ctx.choose_pokemon(
        damaged, "Choose a Benched Pokémon to move all damage counters from")
    if source is None:
        return
    await ctx.move_damage_counters(source, ctx.defender)


card = PokemonCardDef(
    guid="ff222600-2fc3-5396-b4c9-635368c6d50c",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cofagrigus.Name",
    display_name="Cofagrigus",
    searchable_by=["Cofagrigus", "Stage 1", "Cofagrigus"],
    subtypes=["Stage 1"],
    collector_number=46,
    set_code="BW3",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Yamask.Name",
    family_id=562,
    abilities=[
        Attack(
            title="Damagriiigus",
            game_text="Move all damage counters from 1 of your Benched Pok\u00e9mon to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=damagriiigus,
        ),
        Attack(
            title="Perplex",
            game_text="The Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)

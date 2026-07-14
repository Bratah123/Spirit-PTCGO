from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


async def worst_gift(ctx):
    """10 damage for each damage counter on all of your opponent's Pokémon."""
    total_counters = 0
    for pokemon in ctx.opponent_pokemon_in_play():
        total_counters += (ctx.max_hp(pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10
    await ctx.deal_damage(10 * total_counters)


card = PokemonCardDef(
    guid="664d118d-9f67-597a-b47a-59daa0b5d3c5",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mimikyu.Name",
    display_name="Mimikyu",
    searchable_by=["Mimikyu", "Basic", "Mimikyu"],
    subtypes=["Basic"],
    collector_number=80,
    set_code="SWSH11",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=778,
    abilities=[
        Attack(
            title="Perplex",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
        Attack(
            title="Worst Gift",
            game_text="This attack does 10 damage for each damage counter on all of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            effect=worst_gift,
        ),
    ],
)
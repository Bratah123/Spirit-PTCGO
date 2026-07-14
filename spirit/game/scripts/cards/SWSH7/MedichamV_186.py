from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.pokemon import yoga_loop, yoga_loop_condition
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def smash_uppercut(ctx):
    """Printed damage; not affected by Resistance."""
    await ctx.deal_damage(ignore_resistance=True)

card = PokemonCardDef(
    guid="44be1f86-562c-5c4d-b833-f7e036824a98",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MedichamV.Name",
    display_name="Medicham V",
    searchable_by=["Medicham V", "Basic", "V", "Rapid Strike", "MedichamV"],
    subtypes=["Basic", "V", "Rapid Strike"],
    collector_number=186,
    set_code="SWSH7",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=308,
    abilities=[
        Attack(
            title="Yoga Loop",
            game_text="Put 2 damage counters on 1 of your opponent's Pok\u00e9mon. If your opponent's Pok\u00e9mon is Knocked Out by this attack, take another turn after this one. (Skip Pok\u00e9mon Checkup.) If 1 of your Pok\u00e9mon used Yoga Loop during your last turn, this attack can't be used.",
            cost={PokemonTypes.COLORLESS: 2},
            condition=yoga_loop_condition,
            effect=yoga_loop,
        ),
        Attack(
            title="Smash Uppercut",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=smash_uppercut,
        ),
    ],
)
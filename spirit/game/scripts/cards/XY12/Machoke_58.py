from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import recoil_attack, damage_counters_on


async def _karate_chop(ctx):
    """60 minus 10 for each damage counter on this Pokemon."""
    await ctx.deal_damage(max(0, 60 - 10 * damage_counters_on('self')(ctx)))


card = PokemonCardDef(
    guid="c765d06d-1318-527f-a782-dbf65f739797",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Machoke.Name",
    display_name="Machoke",
    searchable_by=["Machoke", "Stage 1", "Machoke"],
    subtypes=["Stage 1"],
    collector_number=58,
    set_code="XY12",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Machop.Name",
    family_id=66,
    abilities=[
        Attack(
            title="Karate Chop",
            game_text="This attack does 60 damage minus 10 damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=60,
            damage_operator="-",
            effect=_karate_chop,
        ),
        Attack(
            title="Submission",
            game_text="This Pok\u00e9mon does 20 damage to itself.",
            cost={PokemonTypes.FIGHTING: 3},
            damage=80,
            effect=recoil_attack(20),
        ),
    ],
)
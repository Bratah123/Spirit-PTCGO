from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if, lock_defender_attacks

GLIMWOOD_TANGLE_GUID = "4d910b75-6845-5f9b-99b1-e6b12b65af27"


def _glimwood_tangle_in_play(ctx):
    stadium = ctx.stadium_in_play()
    return stadium is not None and stadium.archetype_id == GLIMWOOD_TANGLE_GUID


async def flickering_light(ctx):
    await ctx.deal_damage()
    heads = await ctx.flip_coins(1, "Flickering Light")
    if heads[0]:
        lock_defender_attacks(ctx)

card = PokemonCardDef(
    guid="2f3e87ab-1777-56bd-9b30-ab1fc0286201",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shiinotic.Name",
    display_name="Shiinotic",
    searchable_by=["Shiinotic", "Stage 1", "Shiinotic"],
    subtypes=["Stage 1"],
    collector_number=80,
    set_code="SWSH3",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Morelull.Name",
    family_id=755,
    abilities=[
        Attack(
            title="Flickering Light",
            game_text="Flip a coin. If heads, during your opponent's next turn, the Defending Pok\u00e9mon can't attack.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=flickering_light,
        ),
        Attack(
            title="Fear the Forest",
            game_text="If Glimwood Tangle is in play, this attack does 60 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="+",
            effect=bonus_if(_glimwood_tangle_in_play, 60),
        ),
    ],
)
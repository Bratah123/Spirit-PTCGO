from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if
from spirit.game.card_effects.passives_common import takes_less_passive


async def _discard_stadium_after(ctx):
    await ctx.discard_stadium()


card = PokemonCardDef(
    guid="405e7be5-a208-59db-b327-f0a9cfbd566b",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianAvalugg.Name",
    display_name="Hisuian Avalugg",
    searchable_by=["Hisuian Avalugg", "Stage 1", "HisuianAvalugg"],
    subtypes=["Stage 1"],
    collector_number=48,
    set_code="SWSH10",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bergmite.Name",
    family_id=712,
    abilities=[
        Ability(
            title="Massive Ice",
            game_text="This Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            passive=takes_less_passive(30),
        ),
        Attack(
            title="Mountain Gale",
            game_text="If a Stadium is in play, this attack does 120 more damage. Then, discard that Stadium.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator="+",
            effect=bonus_if(lambda ctx: ctx.stadium_in_play() is not None, 120, base=100,
                             also=_discard_stadium_after),
        ),
    ],
)
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import TakesLessPassive


async def diving_uppercut(ctx):
    """120. During your opponent's next turn, this Pokemon takes 50 more
    damage from attacks (after applying Weakness and Resistance)."""
    await ctx.deal_damage()
    ctx.add_passive_through_opponents_turn(ctx.attacker, TakesLessPassive(-50))


card = PokemonCardDef(
    guid="8bdd8b77-da42-5060-9fd8-f57b5e2f59b7",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Toxicroak.Name",
    display_name="Toxicroak",
    searchable_by=["Toxicroak", "Stage 1", "Toxicroak"],
    subtypes=["Stage 1"],
    collector_number=110,
    set_code="SWSH12",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Croagunk.Name",
    family_id=453,
    abilities=[
        Attack(
            title="Pierce",
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
        ),
        Attack(
            title="Diving Uppercut",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 50 more damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=diving_uppercut,
        ),
    ],
)
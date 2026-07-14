from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import TakesLessPassive


async def leaf_guard(ctx):
    """30. During your opponent's next turn, this Pokémon takes 30 less
    damage from attacks (after applying Weakness and Resistance)."""
    await ctx.deal_damage()
    ctx.add_passive_through_opponents_turn(ctx.attacker, TakesLessPassive(30))


card = PokemonCardDef(
    guid="af49d502-c4b6-5599-bde4-b5c95992105a",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LeafeonV.Name",
    display_name="Leafeon V",
    searchable_by=["Leafeon V", "Basic", "V", "LeafeonV"],
    subtypes=["Basic", "V"],
    collector_number=13,
    set_code="CZ",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=470,
    abilities=[
        Attack(
            title="Leaf Guard",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=leaf_guard,
        ),
        Attack(
            title="Slashing Strike",
            game_text="During your next turn, this Pok\u00e9mon can't use Slashing Strike.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=180,
            locks_next_turn=True,
        ),
    ],
)
from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def sonic_boom(ctx):
    """40. This attack's damage isn't affected by Weakness or Resistance."""
    await ctx.deal_damage(apply_modifiers=False)


async def _fight_alone(ctx):
    """30+; 60 more for each Pokemon fewer you have in play than your opponent."""
    diff = len(ctx.opponent_pokemon_in_play()) - len(ctx.my_pokemon_in_play())
    await ctx.deal_damage(ctx.ability.damage + 60 * max(0, diff))


card = PokemonCardDef(
    guid="2cab615f-b11d-52d6-aa1f-eb9f1acc90c8",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lucario.Name",
    display_name="Lucario",
    searchable_by=["Lucario", "Stage 1", "Lucario"],
    subtypes=["Stage 1"],
    collector_number=63,
    set_code="XY10",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Riolu.Name",
    family_id=447,
    abilities=[
        Attack(
            title="Vacuum Wave",
            game_text="This attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.METAL: 1},
            damage=50,
            effect=sonic_boom,
        ),
        Attack(
            title="Fight Alone",
            game_text="If you have fewer Pok\u00e9mon in play than your opponent, this attack does 60 more damage for each Pok\u00e9mon fewer you have in play.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=_fight_alone,
        ),
    ],
)
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.passives_common import protect_next_turn
from spirit.game.session.passives import effective_max_hp


def _moisture_star_condition(board, player_id, pokemon):
    return pokemon.get_attribute(AttrID.HP, 0) < effective_max_hp(board, pokemon)


async def moisture_star(ctx):
    if await ctx.ask_yes_no("Heal all damage from this Pokémon?"):
        await ctx.heal(9999, target=ctx.source)


card = PokemonCardDef(
    guid="45ec4250-3b7d-5915-b6c3-db05452d2cce",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianGoodraVSTAR.Name",
    display_name="Hisuian Goodra VSTAR",
    searchable_by=["Hisuian Goodra VSTAR", "VSTAR", "HisuianGoodraVSTAR"],
    subtypes=["VSTAR"],
    collector_number=202,
    set_code="SWSH11",
    rarity=Rarities.RareRainbow,
    hp=270,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.VSTAR,
    retreat_cost=3,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianGoodraV.Name",
    family_id=706,
    abilities=[
        Ability(
            title="Moisture Star",
            game_text="During your turn, you may heal all damage from this Pok\u00e9mon. (You can't use more than 1 VSTAR Power in a game.)",
            activation=Activations.ONCE_PER_TURN,
            vstar=True,
            condition=_moisture_star_condition,
            effect=moisture_star,
        ),
        Attack(
            title="Rolling Iron",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 80 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.WATER: 1, PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=protect_next_turn(reduce=80),
        ),
    ],
)
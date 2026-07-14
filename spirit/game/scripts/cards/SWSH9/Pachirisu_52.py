from spirit.game.card_effects.attacks_common import damage_per
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


def _my_tools(ctx):
    return sum(
        1 for tool, pokemon in ctx.tools_in_play()
        if pokemon.owning_player_id == ctx.player_id
    )

card = PokemonCardDef(
    guid="d1f956bb-8776-551a-9602-be7fb5b66b86",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pachirisu.Name",
    display_name="Pachirisu",
    searchable_by=["Pachirisu", "Basic", "Pachirisu"],
    subtypes=["Basic"],
    collector_number=52,
    set_code="SWSH9",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=417,
    abilities=[
        Attack(
            title="Windup Thunder",
            game_text="This attack does 30 damage for each Pok\u00e9mon Tool attached to all of your Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="x",
            effect=damage_per(_my_tools, 30),
        ),
    ],
)
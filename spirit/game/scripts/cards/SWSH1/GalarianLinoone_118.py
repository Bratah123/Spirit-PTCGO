from spirit.game.card_effects.support_common import switch_self_attack
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9145f076-a3a9-58a5-b711-a8f1284ee70b",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianLinoone.Name",
    display_name="Galarian Linoone",
    searchable_by=["Galarian Linoone", "Stage 1", "GalarianLinoone"],
    subtypes=["Stage 1"],
    collector_number=118,
    set_code="SWSH1",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianZigzagoon.Name",
    family_id=263,
    abilities=[
        Attack(
            title="Night Slash",
            game_text="Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
            effect=switch_self_attack(),
        ),
        Attack(
            title="Hammer In",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7e19ba01-e7b5-5404-a007-27609ce70773",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianPerrserkerV.Name",
    display_name="Galarian Perrserker V",
    searchable_by=["Galarian Perrserker V", "Basic", "V", "GalarianPerrserkerV"],
    subtypes=["Basic", "V"],
    collector_number=183,
    set_code="SWSH11",
    rarity=Rarities.RareUltra,
    hp=200,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=863,
    abilities=[
        Attack(
            title="Feelin' Fine",
            game_text="Draw 3 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Treasure Rush",
            game_text="This attack does 20 damage for each card in your hand.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)
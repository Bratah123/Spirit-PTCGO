from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a5c94ec1-7a70-58f1-a782-0bb279f6e4d5",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.VikavoltV.Name",
    display_name="Vikavolt V",
    searchable_by=["Vikavolt V", "Basic", "V", "VikavoltV"],
    subtypes=["Basic", "V"],
    collector_number=60,
    set_code="SWSH3",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=738,
    abilities=[
        Attack(
            title="Paralyzing Bolt",
            game_text="During your opponent's next turn, they can't play any Item cards from their hand.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=unimplemented,
        ),
        Attack(
            title="Super Zap Cannon",
            game_text="Discard 2 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=190,
            effect=unimplemented,
        ),
    ],
)
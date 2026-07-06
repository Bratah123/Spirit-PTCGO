from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="dc29d870-7d97-58cb-9baf-6185bd8733af",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RegidragoVSTAR.Name",
    display_name="Regidrago VSTAR",
    searchable_by=["Regidrago VSTAR", "VSTAR", "RegidragoVSTAR"],
    subtypes=["VSTAR"],
    collector_number=201,
    set_code="SWSH12",
    rarity=Rarities.RareRainbow,
    hp=280,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.VSTAR,
    retreat_cost=3,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.RegidragoV.Name",
    family_id=895,
    abilities=[
        Ability(
            title="Legacy Star",
            game_text="During your turn, you may discard the top 7 cards of your deck. Then, put up to 2 cards from your discard pile into your hand. (You can't use more than 1 VSTAR Power in a game.)",
            effect=unimplemented,
        ),
        Attack(
            title="Apex Dragon",
            game_text="Choose an attack from a Dragon Pok\u00e9mon in your discard pile and use it as this attack.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.FIRE: 1},
            effect=unimplemented,
        ),
    ],
)
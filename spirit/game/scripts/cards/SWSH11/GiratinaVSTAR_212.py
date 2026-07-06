from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1c7f1469-e68a-524d-9c09-4c39ed86a34b",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GiratinaVSTAR.Name",
    display_name="Giratina VSTAR",
    searchable_by=["Giratina VSTAR", "VSTAR", "GiratinaVSTAR"],
    subtypes=["VSTAR"],
    collector_number=212,
    set_code="SWSH11",
    rarity=Rarities.RareSecret,
    hp=280,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.VSTAR,
    retreat_cost=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GiratinaV.Name",
    family_id=487,
    abilities=[
        Attack(
            title="Lost Impact",
            game_text="Put 2 Energy attached to your Pok\u00e9mon in the Lost Zone.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=280,
            effect=unimplemented,
        ),
        Attack(
            title="Star Requiem",
            game_text="You can use this attack only if you have 10 or more cards in the Lost Zone. Your opponent's Active Pok\u00e9mon is Knocked Out. (You can't use more than 1 VSTAR Power in a game.)",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.PSYCHIC: 1},
            effect=unimplemented,
        ),
    ],
)
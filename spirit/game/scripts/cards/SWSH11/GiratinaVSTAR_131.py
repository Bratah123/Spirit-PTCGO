from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2448f7fd-1959-5e6d-af1c-714542a5835c",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GiratinaVSTAR.Name",
    display_name="Giratina VSTAR",
    searchable_by=["Giratina VSTAR", "VSTAR", "GiratinaVSTAR"],
    subtypes=["VSTAR"],
    collector_number=131,
    set_code="SWSH11",
    rarity=Rarities.RareHoloVSTAR,
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
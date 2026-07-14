from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="87d64657-cb5b-58a6-82c6-11ff214e6cb1",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DuraludonV.Name",
    display_name="Duraludon V",
    searchable_by=["Duraludon V", "Basic", "V", "Single Strike", "DuraludonV"],
    subtypes=["Basic", "V", "Single Strike"],
    collector_number=103,
    set_code="CZ",
    rarity=Rarities.RareHoloV,
    hp=220,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=884,
    abilities=[
        Attack(
            title="Metal Claw",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.METAL: 1},
            damage=70,
        ),
        Attack(
            title="Breaking Swipe",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon's attacks do 30 less damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.METAL: 2},
            damage=140,
            effect=unimplemented,
        ),
    ],
)
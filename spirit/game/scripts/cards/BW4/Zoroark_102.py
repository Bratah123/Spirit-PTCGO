from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ed987ee1-1c65-52de-ada4-8f26b9c512d2",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zoroark.Name",
    display_name="Zoroark",
    searchable_by=["Zoroark", "Stage 1", "Zoroark"],
    subtypes=["Stage 1"],
    collector_number=102,
    set_code="BW4",
    rarity=Rarities.RareSecret,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Zorua.Name",
    family_id=571,
    abilities=[
        Attack(
            title="Nasty Plot",
            game_text="Search your deck for a card and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Foul Play",
            game_text="Choose 1 of the Defending Pok\u00e9mon's attacks and use it as this attack.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
    ],
)
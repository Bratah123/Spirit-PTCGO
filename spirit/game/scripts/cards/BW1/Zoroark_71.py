from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0fd5f3f6-5246-5165-afec-b3bccb0ae4c7",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zoroark.Name",
    display_name="Zoroark",
    searchable_by=["Zoroark", "Stage 1", "Zoroark"],
    subtypes=["Stage 1"],
    collector_number=71,
    set_code="BW1",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Zorua.Name",
    family_id=570,
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
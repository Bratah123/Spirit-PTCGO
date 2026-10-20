from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="706f6a5e-33c1-5912-85d8-044837a7cf1e",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Liepard.Name",
    display_name="Liepard",
    searchable_by=["Liepard", "Stage 1", "Liepard"],
    subtypes=["Stage 1"],
    collector_number=91,
    set_code="BW7",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Purrloin.Name",
    family_id=509,
    abilities=[
        Attack(
            title="Tail Trickery",
            game_text="The Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Assist",
            game_text="Flip a coin. If heads, choose 1 of your Benched Pok\u00e9mon's attacks and use it as this attack.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
    ],
)
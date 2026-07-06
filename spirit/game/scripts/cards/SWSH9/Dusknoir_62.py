from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1ec71624-7a88-544d-9d72-106cf636d8b1",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dusknoir.Name",
    display_name="Dusknoir",
    searchable_by=["Dusknoir", "Stage 2", "Dusknoir"],
    subtypes=["Stage 2"],
    collector_number=62,
    set_code="SWSH9",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dusclops.Name",
    family_id=355,
    abilities=[
        Ability(
            title="Special Transfer",
            game_text="As often as you like during your turn, you may move a Special Energy from 1 of your Pok\u00e9mon to another of your Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Devour Soul",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
        ),
    ],
)
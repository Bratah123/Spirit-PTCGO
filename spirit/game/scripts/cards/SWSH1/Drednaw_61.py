from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c5f3a167-6b62-513b-9fde-d8e4e304c7b2",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drednaw.Name",
    display_name="Drednaw",
    searchable_by=["Drednaw", "Stage 1", "Drednaw"],
    subtypes=["Stage 1"],
    collector_number=61,
    set_code="SWSH1",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Chewtle.Name",
    family_id=833,
    abilities=[
        Attack(
            title="Vise Bite",
            game_text="This attack does 30 more damage for each Colorless in your opponent's Active Pok\u00e9mon's Retreat Cost.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Jaw Lock",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 3},
            damage=130,
            effect=unimplemented,
        ),
    ],
)
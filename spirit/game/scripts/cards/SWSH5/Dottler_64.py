from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="811a4a95-aed5-51ab-8852-a49f7fe19727",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dottler.Name",
    display_name="Dottler",
    searchable_by=["Dottler", "Stage 1", "Dottler"],
    subtypes=["Stage 1"],
    collector_number=64,
    set_code="SWSH5",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Blipbug.Name",
    family_id=824,
    abilities=[
        Attack(
            title="Radar",
            game_text="Look at the top 4 cards of your deck and put them back in any order.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Ram",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
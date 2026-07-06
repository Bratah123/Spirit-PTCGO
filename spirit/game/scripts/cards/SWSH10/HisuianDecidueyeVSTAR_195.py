from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="dbe58393-7634-5707-9f52-90033c4d4ca1",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianDecidueyeVSTAR.Name",
    display_name="Hisuian Decidueye VSTAR",
    searchable_by=["Hisuian Decidueye VSTAR", "VSTAR", "HisuianDecidueyeVSTAR"],
    subtypes=["VSTAR"],
    collector_number=195,
    set_code="SWSH10",
    rarity=Rarities.RareRainbow,
    hp=270,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.VSTAR,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianDecidueyeV.Name",
    family_id=724,
    abilities=[
        Ability(
            title="Star of Fortune",
            game_text="During your turn, you may draw cards until you have 8 cards in your hand. (You can't use more than 1 VSTAR Power in a game.)",
            effect=unimplemented,
        ),
        Attack(
            title="Somersault Feathers",
            game_text="You may discard up to 3 Energy cards from your hand. This attack does 30 more damage for each card you discarded in this way.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=160,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)
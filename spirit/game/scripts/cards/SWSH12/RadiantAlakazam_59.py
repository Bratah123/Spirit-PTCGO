from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="83366c0e-ddc2-5065-b76d-ddb9dea45513",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RadiantAlakazam.Name",
    display_name="Radiant Alakazam",
    searchable_by=["Radiant Alakazam", "Basic", "Radiant", "RadiantAlakazam"],
    subtypes=["Basic", "Radiant"],
    collector_number=59,
    set_code="SWSH12",
    rarity=Rarities.RareRadiant,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=65,
    abilities=[
        Ability(
            title="Painful Spoons",
            game_text="Once during your turn, you may move up to 2 damage counters from 1 of your opponent's Pok\u00e9mon to another of their Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Mind Ruler",
            game_text="This attack does 20 damage for each card in your opponent's hand.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)
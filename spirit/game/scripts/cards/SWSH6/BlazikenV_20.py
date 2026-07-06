from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="54adf96b-050c-5de6-a9f9-0e3331b46549",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlazikenV.Name",
    display_name="Blaziken V",
    searchable_by=["Blaziken V", "Basic", "V", "Rapid Strike", "BlazikenV"],
    subtypes=["Basic", "V", "Rapid Strike"],
    collector_number=20,
    set_code="SWSH6",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=257,
    abilities=[
        Attack(
            title="High Jump Kick",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
        Attack(
            title="Fire Spin",
            game_text="Discard 2 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            damage=210,
            effect=unimplemented,
        ),
    ],
)
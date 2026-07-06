from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2d49019c-2d9f-53b1-92d0-688c6361a3c1",
    key="SWSH45",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MorpekoV.Name",
    display_name="Morpeko V",
    searchable_by=["Morpeko V", "Basic", "V", "MorpekoV"],
    subtypes=["Basic", "V"],
    collector_number=37,
    set_code="SWSH45",
    rarity=Rarities.RareHoloV,
    hp=170,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=877,
    abilities=[
        Attack(
            title="Spark",
            game_text="This attack also does 20 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Electro Wheel",
            game_text="Discard an Energy from this Pok\u00e9mon. If you do, switch it with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=unimplemented,
        ),
    ],
)
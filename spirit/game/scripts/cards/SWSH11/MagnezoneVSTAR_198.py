from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="18cacb06-b824-5a47-bd3c-e623e51bf3b4",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MagnezoneVSTAR.Name",
    display_name="Magnezone VSTAR",
    searchable_by=["Magnezone VSTAR", "VSTAR", "MagnezoneVSTAR"],
    subtypes=["VSTAR"],
    collector_number=198,
    set_code="SWSH11",
    rarity=Rarities.RareRainbow,
    hp=270,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.VSTAR,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MagnezoneV.Name",
    family_id=462,
    abilities=[
        Attack(
            title="Magnetic Grip",
            game_text="Search your deck for up to 2 Item cards, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=180,
            effect=unimplemented,
        ),
        Attack(
            title="Electro Star",
            game_text="This attack does 90 damage to 2 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) (You can't use more than 1 VSTAR Power in a game.)",
            cost={PokemonTypes.LIGHTNING: 2},
            effect=unimplemented,
        ),
    ],
)
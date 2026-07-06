from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="91ac4eab-73b5-5c97-9be7-3b8a8c56d66a",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MagnezoneV.Name",
    display_name="Magnezone V",
    searchable_by=["Magnezone V", "Basic", "V", "MagnezoneV"],
    subtypes=["Basic", "V"],
    collector_number=56,
    set_code="SWSH11",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=462,
    abilities=[
        Attack(
            title="Magnetic Tension",
            game_text="Switch 1 of your opponent's Benched Pok\u00e9mon with their Active Pok\u00e9mon. This attack does 40 damage to the new Active Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Splitting Beam",
            game_text="This attack also does 30 damage to 2 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=unimplemented,
        ),
    ],
)
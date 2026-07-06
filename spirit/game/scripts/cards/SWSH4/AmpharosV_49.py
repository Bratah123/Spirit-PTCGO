from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="484d8cc2-b2ee-5885-b55f-eb84ab1b52e6",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AmpharosV.Name",
    display_name="Ampharos V",
    searchable_by=["Ampharos V", "Basic", "V", "AmpharosV"],
    subtypes=["Basic", "V"],
    collector_number=49,
    set_code="SWSH4",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=181,
    abilities=[
        Attack(
            title="Dazzle Blast",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=unimplemented,
        ),
        Attack(
            title="Damaging Spark",
            game_text="This attack also does 30 damage to each of your opponent's Benched Pok\u00e9mon that has any damage counters on it. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=unimplemented,
        ),
    ],
)
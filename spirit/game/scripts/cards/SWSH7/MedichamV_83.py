from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="55a457fb-4cb9-5537-9c27-d2612cb5b714",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MedichamV.Name",
    display_name="Medicham V",
    searchable_by=["Medicham V", "Basic", "V", "Rapid Strike", "MedichamV"],
    subtypes=["Basic", "V", "Rapid Strike"],
    collector_number=83,
    set_code="SWSH7",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=308,
    abilities=[
        Attack(
            title="Yoga Loop",
            game_text="Put 2 damage counters on 1 of your opponent's Pok\u00e9mon. If your opponent's Pok\u00e9mon is Knocked Out by this attack, take another turn after this one. (Skip Pok\u00e9mon Checkup.) If 1 of your Pok\u00e9mon used Yoga Loop during your last turn, this attack can't be used.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
        Attack(
            title="Smash Uppercut",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=unimplemented,
        ),
    ],
)
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, damage_counters_on
from spirit.game.card_effects.passives_common import takes_less_passive

card = PokemonCardDef(
    guid="3fc8d7a1-d601-5b59-9dac-3e8e196f790c",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UrsalunaV.Name",
    display_name="Ursaluna V",
    searchable_by=["Ursaluna V", "Basic", "V", "UrsalunaV"],
    subtypes=["Basic", "V"],
    collector_number=102,
    set_code="SWSH12",
    rarity=Rarities.RareHoloV,
    hp=230,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    family_id=901,
    abilities=[
        Ability(
            title="Hard Coat",
            game_text="This Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            passive=takes_less_passive(30),
        ),
        Attack(
            title="Peat Shoulder",
            game_text="This attack does 10 less damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 3},
            damage=220,
            damage_operator="-",
            effect=damage_per(damage_counters_on("self"), -10, base=220),
        ),
    ],
)
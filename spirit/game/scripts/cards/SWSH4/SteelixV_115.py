from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, damage_counters_on, recoil_attack

card = PokemonCardDef(
    guid="48c48a83-8d29-5153-abdb-309f4776602e",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SteelixV.Name",
    display_name="Steelix V",
    searchable_by=["Steelix V", "Basic", "V", "SteelixV"],
    subtypes=["Basic", "V"],
    collector_number=115,
    set_code="SWSH4",
    rarity=Rarities.RareHoloV,
    hp=250,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=208,
    abilities=[
        Attack(
            title="Raging Hammer",
            game_text="This attack does 10 more damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=damage_per(damage_counters_on("self"), 10, base=30),
        ),
        Attack(
            title="Iron Tackle",
            game_text="This Pok\u00e9mon also does 30 damage to itself.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 4},
            damage=210,
            effect=recoil_attack(30),
        ),
    ],
)
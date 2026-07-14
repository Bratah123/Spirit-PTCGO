from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, damage_counters_on, recoil_attack

card = PokemonCardDef(
    guid="9f385d35-3e03-5e6f-a1e2-eb3802ff0fb6",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RegirockV.Name",
    display_name="Regirock V",
    searchable_by=["Regirock V", "Basic", "V", "RegirockV"],
    subtypes=["Basic", "V"],
    collector_number=104,
    set_code="SWSH1",
    rarity=Rarities.RareHoloV,
    hp=220,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=377,
    abilities=[
        Attack(
            title="Raging Hammer",
            game_text="This attack does 10 more damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=damage_per(damage_counters_on("self"), 10, base=30),
        ),
        Attack(
            title="Rocky Tackle",
            game_text="This Pok\u00e9mon also does 30 damage to itself.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=190,
            effect=recoil_attack(30),
        ),
    ],
)
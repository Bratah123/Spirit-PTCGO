from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, count_prizes_taken
from spirit.game.card_effects.passives_common import takes_less_passive

card = PokemonCardDef(
    guid="73d2df8d-aa04-534d-8635-f5882252efbb",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DubwoolV.Name",
    display_name="Dubwool V",
    searchable_by=["Dubwool V", "Basic", "V", "DubwoolV"],
    subtypes=["Basic", "V"],
    collector_number=153,
    set_code="SWSH2",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=832,
    abilities=[
        Ability(
            title="Soft Wool",
            game_text="This Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            passive=takes_less_passive(30),
        ),
        Attack(
            title="Revenge Blast",
            game_text="This attack does 30 more damage for each Prize card your opponent has taken.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=120,
            damage_operator="+",
            effect=damage_per(count_prizes_taken("opponent"), 30, base=120),
        ),
    ],
)
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, damage_counters_on, mill_attack

card = PokemonCardDef(
    guid="670fe908-b30f-5809-b4e7-473a9a7964a8",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CrabominableV.Name",
    display_name="Crabominable V",
    searchable_by=["Crabominable V", "Basic", "V", "CrabominableV"],
    subtypes=["Basic", "V"],
    collector_number=248,
    set_code="SWSH8",
    rarity=Rarities.RareUltra,
    hp=220,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.METAL,
    family_id=740,
    abilities=[
        Attack(
            title="Trigger Avalanche",
            game_text="Discard the top 2 cards of your opponent's deck.",
            cost={PokemonTypes.WATER: 1},
            effect=mill_attack(2),
        ),
        Attack(
            title="Destroyer Punch",
            game_text="This attack does 60 more damage for each damage counter on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            damage_operator="+",
            effect=damage_per(damage_counters_on("defender"), 60, base=90),
        ),
    ],
)
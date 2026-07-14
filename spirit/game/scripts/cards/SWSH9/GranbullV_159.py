from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import (
    damage_per, damage_counters_on, recoil_attack,
)

card = PokemonCardDef(
    guid="374a61e3-be20-59a8-993e-dcef02dbe786",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GranbullV.Name",
    display_name="Granbull V",
    searchable_by=["Granbull V", "Basic", "V", "GranbullV"],
    subtypes=["Basic", "V"],
    collector_number=159,
    set_code="SWSH9",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=210,
    abilities=[
        Attack(
            title="Chomp",
            game_text="This attack does 10 more damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=damage_per(damage_counters_on("self"), 10, base=30),
        ),
        Attack(
            title="Bull Dash",
            game_text="This Pok\u00e9mon also does 30 damage to itself.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=190,
            effect=recoil_attack(30),
        ),
    ],
)
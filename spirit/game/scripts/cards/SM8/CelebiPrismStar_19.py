from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import heal_attack

from spirit.game.card_effects.sm8 import (
    time_distortion,
)

card = PokemonCardDef(
    guid="85255362-5cac-58ce-ab08-53df0650013d",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CelebiPrismStar.Name",
    display_name="Celebi {*}",
    searchable_by=["Celebi {*}", "Basic", "Prism Star", "CelebiPrismStar"],
    subtypes=["Basic", "Prism Star"],
    collector_number=19,
    set_code="SM8",
    rarity=Rarities.Prism,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=251,
    abilities=[
        Attack(
            title="Time Distortion",
            game_text="Devolve any number of your Benched Pok\u00e9mon as many times as you like. Put each Evolution card removed this way into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=time_distortion
        ),
        Attack(
            title="Leech Seed",
            game_text="Heal 20 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=heal_attack(20),
        ),
    ],
)
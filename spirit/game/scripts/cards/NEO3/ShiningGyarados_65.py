from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import (
    damage_counters_on, damage_per, flip_or_nothing,
)
from spirit.game.card_effects.ecard import devastate


card = PokemonCardDef(
    guid="a874f692-62c0-55d2-8862-c23d5efa7bba",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ShiningGyarados.Name",
    display_name="Shining Gyarados",
    searchable_by=["Shining Gyarados", "Basic", "ShiningGyarados"],
    subtypes=["Basic"],
    collector_number=65,
    set_code="NEO3",
    rarity=Rarities.Shining,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=130,
    abilities=[
        Attack(
            title="Outrage",
            game_text="Flip a coin. If heads, this attack does 30 damage plus 10 more damage for each damage counter on Shining Gyarados. If tails, this attack does nothing.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.FIGHTING: 2},
            damage=30,
            damage_operator="+",
            effect=flip_or_nothing(
                then=damage_per(damage_counters_on("self"), 10, base=30)),
        ),
        Attack(
            title="Devastate",
            game_text="Discard 2 Fire Energy cards attached to Shining Gyarados or this attack does nothing. This attack does 10 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) Then, flip a coin. If heads, choose 1 Energy card attached to each of your opponent's Pok\u00e9mon that has any Energy cards attached to it and discard those Energy cards.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.FIRE: 2},
            damage=50,
            effect=devastate,
        ),
    ],
)

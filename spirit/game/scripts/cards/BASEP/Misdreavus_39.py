from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import (
    condition_attack, damage_counters_on, place_counters,
)


card = PokemonCardDef(
    guid="f3f91494-3610-59b5-9ca1-ddc8fa5dacc5",
    key="BASEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Misdreavus.Name",
    display_name="Misdreavus",
    searchable_by=["Misdreavus", "Basic", "Misdreavus"],
    subtypes=["Basic"],
    collector_number=39,
    set_code="BASEP",
    rarity=Rarities.RarePromo,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=200,
    abilities=[
        Attack(
            title="Pain Split",
            game_text="Put 1 damage counter on the Defending Pok\u00e9mon for each damage counter on Misdreavus.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=place_counters(damage_counters_on("self")),
        ),
        Attack(
            title="Confuse Ray",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=10,
            effect=condition_attack(SpecialConditions.CONFUSED, flip=True),
        ),
    ],
)

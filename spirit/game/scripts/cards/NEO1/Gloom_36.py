from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import sticky_nectar


card = PokemonCardDef(
    guid="9ee2706a-0995-55e5-b679-5eeb0df0ab4b",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gloom.Name",
    display_name="Gloom",
    searchable_by=["Gloom", "Stage 1", "Gloom"],
    subtypes=["Stage 1"],
    collector_number=36,
    set_code="NEO1",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Oddish.Name",
    family_id=43,
    abilities=[
        Attack(
            title="Strange Powder",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused. If tails, the Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=condition_attack(
                SpecialConditions.CONFUSED, flip=True,
                tails_conditions=(SpecialConditions.ASLEEP,),
            ),
        ),
        Attack(
            title="Sticky Nectar",
            game_text="Flip a coin. If heads, this attack does 20 damage plus 10 more damage and, until the end of your next turn, as long as Gloom is your Active Pok\u00e9mon, the Defending Pok\u00e9mon can't retreat, and if the effect of an attack, Pok\u00e9mon Power, or Trainer card would change that player's Active Pok\u00e9mon, that part of the effect does nothing. If tails, this attack does 20 damage.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=sticky_nectar(10),
        ),
    ],
)

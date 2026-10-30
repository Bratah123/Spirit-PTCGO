from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import allergic_pollen_passive


card = PokemonCardDef(
    guid="95a0dbf6-c06a-5695-a6c6-04239e93b8da",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Parasect.Name",
    display_name="Parasect",
    searchable_by=["Parasect", "Stage 1", "Parasect"],
    subtypes=["Stage 1"],
    collector_number=35,
    set_code="NEO3",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Paras.Name",
    family_id=46,
    abilities=[
        Ability(
            title="Allergic Pollen",
            game_text="As long as Parasect is in play, cards in any player's discard piles are not affected by attacks or Pok\u00e9mon Powers. This power stops working if Parasect becomes Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_POWER,
            passive=allergic_pollen_passive,
        ),
        Attack(
            title="Sleep Pinchers",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.GRASS: 2},
            damage=30,
            effect=condition_attack(SpecialConditions.ASLEEP, flip=True),
        ),
    ],
)

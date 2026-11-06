from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import hard_shell


card = PokemonCardDef(
    guid="474a45d9-8c09-5324-a023-77bb0a9ca25d",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shuckle.Name",
    display_name="Shuckle",
    searchable_by=["Shuckle", "Basic", "Shuckle"],
    subtypes=["Basic"],
    collector_number=51,
    set_code="NEO3",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=213,
    abilities=[
        Ability(
            title="Hard Shell",
            game_text="Whenever an attack (including your own) does 40 or less damage to Shuckle (after applying Weakness and Resistance), reduce that damage to 10. (Any other effects of attacks still happen.) This power stops working while Shuckle is Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_POWER,
            passive=hard_shell,
        ),
        Attack(
            title="Toxic Saliva",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Poisoned. It now takes 20 Poison damage instead of 10 after each player's turn (even if it was already Poisoned).",
            cost={PokemonTypes.GRASS: 2},
            effect=condition_attack(SpecialConditions.POISONED, flip=True, counters=2),
        ),
    ],
)

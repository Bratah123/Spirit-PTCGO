from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import (
    no_special_conditions,
    submerge,
    submerge_passive,
)


card = PokemonCardDef(
    guid="612c0e0b-93d6-518c-9834-f6abf9ea0ab1",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lanturn.Name",
    display_name="Lanturn",
    searchable_by=["Lanturn", "Stage 1", "Lanturn"],
    subtypes=["Stage 1"],
    collector_number=32,
    set_code="NEO3",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Chinchou.Name",
    family_id=170,
    abilities=[
        Ability(
            title="Submerge",
            game_text="Once during your turn (before your attack), you may change Lanturn's type to Water until the end of your turn. This power can't be used if Lanturn is Asleep, Confused, or Paralyzed. If Lanturn becomes Asleep, Confused, or Paralyzed after you have used this power, its type changes back to Lightning.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=no_special_conditions,
            passive=submerge_passive,
            effect=submerge,
        ),
        Attack(
            title="Blinding Light",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=condition_attack(SpecialConditions.CONFUSED, flip=True),
        ),
    ],
)

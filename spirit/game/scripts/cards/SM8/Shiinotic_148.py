from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

from spirit.game.card_effects.sm8 import (
    dreams_touch,
    effect_spore,
)

card = PokemonCardDef(
    guid="feaba974-af2a-55a7-b5f7-daeaf4a7814d",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shiinotic.Name",
    display_name="Shiinotic",
    searchable_by=["Shiinotic", "Stage 1", "Shiinotic"],
    subtypes=["Stage 1"],
    collector_number=148,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Morelull.Name",
    family_id=755,
    abilities=[
        Ability(
            title="Effect Spore",
            game_text="If this Pok\u00e9mon is your Active Pok\u00e9mon and is damaged by an opponent's attack (even if this Pok\u00e9mon is Knocked Out), the Attacking Pok\u00e9mon is now Asleep.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=effect_spore,
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
        ),
        Attack(
            title="Dream's Touch",
            game_text="If your opponent's Active Pok\u00e9mon is Asleep, your opponent shuffles all Energy from it into their deck.",
            cost={PokemonTypes.FAIRY: 2},
            damage=50,
            effect=dreams_touch
        ),
    ],
)
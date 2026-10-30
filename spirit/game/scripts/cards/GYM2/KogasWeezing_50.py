from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import spontaneous_explosion


card = PokemonCardDef(
    guid="24289720-f6af-502d-82ba-c75df3b24668",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KogasWeezing.Name",
    display_name="Koga's Weezing",
    searchable_by=["Koga's Weezing", "Stage 1", "KogasWeezing"],
    subtypes=["Stage 1"],
    collector_number=50,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.KogasKoffing.Name",
    family_id=109,
    abilities=[
        Attack(
            title="Spontaneous Explosion",
            game_text="Flip a coin. If heads, this attack does 10 damage plus 30 more damage and Koga's Weezing does 30 damage to itself; if tails, this attack does 10 damage.",
            cost={PokemonTypes.GRASS: 2},
            damage=10,
            damage_operator="+",
            effect=spontaneous_explosion,
        ),
        Attack(
            title="Toxic Cloud",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Poisoned. It now takes 20 Poison damage instead of 10 after each player's turn (even if it was already Poisoned).",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=condition_attack(
                SpecialConditions.POISONED, flip=True, counters=2),
        ),
    ],
)

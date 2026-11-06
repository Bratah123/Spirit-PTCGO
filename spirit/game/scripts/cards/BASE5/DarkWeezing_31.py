from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import mass_explosion


card = PokemonCardDef(
    guid="6472068c-0a36-5a6e-b3c9-d66856fcca93",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkWeezing.Name",
    display_name="Dark Weezing",
    searchable_by=["Dark Weezing", "Stage 1", "DarkWeezing"],
    subtypes=["Stage 1"],
    collector_number=31,
    set_code="BASE5",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Koffing.Name",
    family_id=109,
    abilities=[
        Attack(
            title="Mass Explosion",
            game_text="Does 20 damage times the total number of Koffings, Weezings, and Dark Weezings in play (Apply Weakness and Resistance.). Then, this attack does 20 damage to each Koffing, Weezing, and Dark Weezing (even your own). Don't apply Weakness and Resistance.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=mass_explosion,
        ),
        Attack(
            title="Stun Gas",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Poisoned; if tails, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.GRASS: 3},
            damage=20,
            effect=condition_attack(
                SpecialConditions.POISONED, flip=True,
                tails_conditions=(SpecialConditions.PARALYZED,),
            ),
        ),
    ],
)
